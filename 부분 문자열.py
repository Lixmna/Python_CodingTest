import re

def Solution(temp1, temp2) :

#    answer = []
#    temp = len(bubun[1])
#    a = temp1.find(temp2)

#    if  a != -1 :
#        print(1)
#    else :
#        print(0)
    if temp2 in temp1 :
        print(1)
    else :
        print(0)
    

"""
    if bubun[0] == bubun[1] :
        print("1")
        return

    for i in range(len(bubun[0])) :
        if len(bubun[0]) < len(bubun[1])+i :
            print("0")
            return

        if bubun[0][i] == bubun[1][0] :
            for j in range(len(bubun[1])) :
                if bubun[0][i+j] != bubun[1][j] :
                    break;

                if j == temp-1 :
                    print("1")
                    return

bubun = []

bubun.append(list(map(str, input().split())))
bubun.append(list(map(str, input().split())))
soulution(bubun)
"""


temp1=input()
temp2=input()

Solution(temp1, temp2)