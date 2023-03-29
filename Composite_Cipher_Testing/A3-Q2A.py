import sys

OriginalValue = 2047

SqRValue = 45.2437841035

flag = False
LoopCount = 2
PresentMod = None
print ('Made it to: 1')
while flag != True:
    PresentMod = OriginalValue % LoopCount
    print (PresentMod)
    if PresentMod == 0:
        print ('Factor Found!', LoopCount)
        flag = True
    #if LoopCount < OriginalValue:
        #print ('No factor found!')
        #sys.exit()
    else:
        LoopCount = LoopCount + 1
