
print ("Welcome to Algorithms & Data Structures Assignment #1 \n")

print ("Please select function 1, 2, or 3. \n \n")

print ("-------------------------------")

print ("Algorithm #1 *Fast* \n")

print ("Algorithm #2 *Slow* \n")

print ("Algorithm #3 *Slowest*")

print ("-------------------------------")

def lisaAnn(): #This function will compute the values for algo #2.
    global i, n, q, Negative3Sum
    i = 1
    Negative3Sum = 0
    while (i <= 3*n):
        i = i + 1
        q = 1
            
        while (q <= 3):
            Negative3Sum = Negative3Sum - q*q
            #print (Negative3Sum)
            q = q + 1
            if (q == 3):
                q = 1
                break

def krissyLynn(): #This function will compute the values for algo #3.
    global i, n, j, NegativeSubSumSquare, NegativeSubSum
    i = 1
    j = 1
    NegativeSubSumSquare = 0
    NegativeSubSum = 0
    while (i <= n):
        i = i + 1
        while (j <= i):
            NegativeSubSum = NegativeSubSum - j*j
            #print (NegativeSubSum)
            j = j + 1
            if (j == i):
                j = 1
                break

#------------------------------------------------------------------

selection = int(input("Please select function 1, 2, or 3: \n \n"))
if selection == 1:
        print ("Running Algorithm #1 \n")
        n = int(input("Please enter a 'n' times difficulty: \n"))
        NegativeSumSuare = 0
        from datetime import datetime
        startTime = datetime.now()
        for i in range (1,n):
            Sum = 0
            Sum = Sum - i*i
            #print (Sum)
        processTime = datetime.now() - startTime
        print ("All iterations have been computed in: ")
        print (processTime)

elif selection == 2:
        print ("Running Algorithm #2 \n")
        n = int(input("Please enter a 'n' times difficulty: \n"))
        from datetime import datetime
        startTime = datetime.now()
        lisaAnn()
        print ("All iterations have been computed in: ")
        print (datetime.now() - startTime)

elif selection == 3:
        print ("Running algorithm #3 \n")
        n = int(input("Please enter a 'n' times difficulty: \n"))
        from datetime import datetime
        startTime = datetime.now()
        krissyLynn()
        print ("All iterations have been computed in: ")
        print (datetime.now() - startTime)

else:
        print ("No valid value was entered. Ending program... \n")


		

		
		
