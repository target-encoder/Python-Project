import sys


def avgFirstThreeDigit(my_list):

    sumthreedigit=0
    SortedList=[]

    for numbers in my_list:
        for digit in str(numbers)[0:3]:
            sumthreedigit+=int (digit)
        #print(sumthreedigit)

        if sumthreedigit%3==0:
            SortedList.insert(0, int(sumthreedigit / 3))
        else:
            SortedList.insert(0,sumthreedigit/3)
        sumthreedigit=0
    return SortedList

ListIntegers=[]
TempList=[]


file=open("Integer.txt","r")
for line in file.readlines():
    ListIntegers=line.split(";")
for i in range(len(ListIntegers)):
    ListIntegers[i]=int(ListIntegers[i])

output=avgFirstThreeDigit(ListIntegers)
print(output)

file.close()