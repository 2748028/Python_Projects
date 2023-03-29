#Module Library
import multiprocessing
import datetime     #time!
import time         #sleep!
import binascii     #hexa to ascii!

# Lock for printing to the screen
lock = multiprocessing.Lock()

#---------------------------------------#
#Formats information into a usable format
class Info:
    def __init__(self, packet): #Packet constructor

        self.VLAN = ""
        self.desMAC = ""
        self.srcMAC = ""
        self.payload = ""

        # Get date using datetime library
        self.stamp = str(datetime.datetime.now())

        # Positions 45, 46, 47 contain VLAN tag #.
        for i in range(3):
            self.VLAN += (packet[45 + i])

        # Positions 16 to 27 contain destination MAC
        for i in range(12):
            self.desMAC += (packet[16 + i])

        # Positions 28 to 39 contain source MAC
        for i in range(12):
            self.srcMAC += (packet[28 + i])

        i = 52
        # Position 52 onwards contain payload information
        while ((packet[i] != "/n") & (packet[i] != " ")):
            self.payload += (packet[i])
            i += 1

        self.payload = self.payload[:-8]  # remove the last 8 bits, as they are the checksum
        self.payload = str(binascii.unhexlify(self.payload)) #Change from hexadecimal to ascii
        self.payload = self.payload.replace("b\'","")   #Strip unnecessary characters
        self.payload = self.payload.replace("\'", "")   #Strip unnecessary characters
        return
#---------------------------------------#

#---------------------------------------#
class Node:
    def __init__(self, packet, priority):
        self.packet = packet
        self.priority  = priority
        self.next = None
        self.prev = None
#---------------------------------------#

#---------------------------------------#
class Queue:
    # Initialize queue
    def __init__(self):
        self.length = 0
        self.front = None
        self.back = None

    #Adds to the queue in the assigned priority
    def enqueue(self, packet, priority = 0):
        node = Node(packet, priority)
        temp = self.front

        #If the queue is empty, doesn't exist
        if ((self.front == None) & (self.back == None)):
            self.front = node
            self.back = node
        else:
            #If low priority, insert at back
            if (node.priority == 0):
                self.back.prev = node
                node.next = self.back
                self.back = node

            #If high priority, locate position to append
            elif (node.priority == 2):
                #Just before the low priority packets
                if (temp.prev != None):
                    while (temp.prev.priority != 0):
                        if(temp.prev == None):
                            break
                        temp = temp.prev

                if (temp.next == None):
                    self.front.next = node
                    node.prev = self.front
                    self.front = node
                    self.front.next = None

                # Insert at position using temp node
                elif (temp.prev == None):
                    self.back.prev = node
                    node.next = self.back
                    self.back = node
                    self.back.prev = None
                # If end of queue is reached (broke out of while loop)
                else:
                    temp.prev.next = node
                    node.prev = temp.prev
                    node.next = temp
                    temp.prev = node

        self.length += 1
        return

    #Removes the front of a queue, as expected
    #Returns the top of the queue before dequeuing
    def dequeue (self):
        #If queue is not just a single node
        if (self.front != self.back):
            head = self.front
            self.front = self.front.prev
            self.front.next = None
            self.length -= 1
            return head.packet
        else:
            head = self.front
            self.front = None
            self.back = None
            self.length = 0
            return head.packet


    #Returns size of queue
    def size(self):
        return self.length

#---------------------------------------#

#---------------------------------------#
#Thread 1
class Switch():
    def __init__(self):
        # All packets are saved in this un-sorted queue.
        self.unsortedQueue = Queue()
        # Priority queues for both VLANs
        self.queueVLAN100 = Queue()
        self.queueVLAN101 = Queue()

        # Lock delimiters are for when there is no more of other VLAN packets
        # This enables printing/logging even when the semaphore is locked
        self.lockDelimiter100 = 0
        self.lockDelimiter101 = 0

        # Semaphore for ensuring rotation of VLAN packets
        self.semaphore = 0

        #Reliable counter for packet processing
        self.packetsProcessed = 0

    def thread1Queuing(self):
        # Pool is a collection of processes, and can be appended to
        packetCapture = open("packets.capture", "r")  # Opens capture file
        pool = multiprocessing.Pool()
        packetsProcessed = 0
        # Append "packet" to unsorted queue
        for line in packetCapture:
            self.unsortedQueue.enqueue(line)    # Insert line of capture file into queue
        packetCapture.close()                   # Close the capture file
        totalPackets = self.unsortedQueue.size()# For the size of the queue

        while (self.packetsProcessed) != (totalPackets):
            if (self.unsortedQueue.size() > 0):
                packet = self.unsortedQueue.dequeue()   # Saves front of queue to packet variable
                packetInfo = Info(packet)              # Generates object about the packet info
                # Position 44 is the priority tag
                if packet[44] == "0":  #Low priority
                    if packetInfo.VLAN == "100":
                        self.queueVLAN100.enqueue(packet, 0)  # If priority 0, then insert at back of queue of 100
                        pool.Process(self.thread3Output())
                    elif packetInfo.VLAN == "101":
                        self.queueVLAN101.enqueue(packet, 0)  # If priority 0, then insert at back of queue of 101
                        pool.Process(self.thread3Output())

                elif packet[44] == "2": #High priority
                    pool.Process(self.thread2Interrupt(packet))  # Child process for interrupt handler
                    if packetInfo.VLAN == "100":
                        self.queueVLAN100.enqueue(packet, 2)  # If priority 2, then insert at front of queue
                        pool.Process(self.thread3Output())
                    elif packetInfo.VLAN == "101":
                        self.queueVLAN101.enqueue(packet, 2)
                        pool.Process(self.thread3Output())
                else:
                    print("Unsupported Priority")  # Base case

            elif (self.unsortedQueue.size() == 0):
                    pool.Process(self.thread3Output())
        print("Process finished at " + str(datetime.datetime.now()))
        return

    #---------------------------------------#

    #---------------------------------------#
    #Interrupt Handler
    def thread2Interrupt(self, packet):
        lock.acquire()
        info = Info(packet)
        output = ("##############################################"
                  "##############################################"
                  "##############################################\n"
                  "Priority Packet Destined For MAC " + info.desMAC
                  + " | Originated: " + info.srcMAC
                  + " | Received At Time: " + info.stamp + "\n")
        # To Screen
        print(output)  # Print output variable to screen.

        # To File
        logFile = open("log.txt", "a")  # Text log file to append information
        logFile.write(output)  # Append output variable to the log file.
        logFile.close()
        lock.release()
        return
    #---------------------------------------#

    #---------------------------------------#
    #Screen output and file logging
    def thread3Output(self):  # Print to screen and log file.
        # Print VLAN 100 packets, then alternate to VLAN 101
        if (self.semaphore == 0):
            if (self.queueVLAN100.size() != 0):
                # Get the front packet from VLAN 100 queue
                log = Info(self.queueVLAN100.dequeue())
                self.packetOutput(log)
                self.lockDelimiter100 = 0
                self.packetsProcessed += 1
                self.semaphore = 1
            elif (self.lockDelimiter100 >= 100):
                self.semaphore = 1
            self.lockDelimiter100 = + 1

        # Print VLAN 101 packets after VLAN 100
        elif (self.semaphore == 1):
            # If there something available to print, else skip
            if (self.queueVLAN101.size() != 0):
                # Get the front packet from VLAN 101 queue
                log = Info(self.queueVLAN101.dequeue())
                self.packetOutput(log)
                self.lockDelimiter101 = 0
                self.packetsProcessed +=1
                self.semaphore = 0
                # As per requirement, sleep for a second
                time.sleep(1)
            elif(self.lockDelimiter101 >= 100):
                self.semaphore = 0
            self.lockDelimiter101 += 1
        return
    #---------------------------------------#

    #---------------------------------------#
    def packetOutput(self, log):
        lock.acquire()
        # Setup packet information into a readable format
        output = ("Packet Received at " + log.stamp
                  + " | Source Mac: " + log.srcMAC
                  + " | Destination Mac: " + log.desMAC
                  + " | Payload: " + log.payload
                  + " | VLAN: " + log.VLAN + "\n")
        # To Screen
        print(output)  # Print output variable to screen.

        # To File
        logFile = open("log.txt", "a")  # Text log file to append information
        logFile.write(output)  # Append output variable to the log file.
        logFile.close()
        lock.release()
        return

#---------------------------------------#

#---------------------------------------#
def main():
    switch = Switch()
    # For new processes to properly execute, this statement is necessary
    if __name__ == "__main__":
        multiprocessing.Process(switch.thread1Queuing()) #Initializes queuing process
    return
main()

