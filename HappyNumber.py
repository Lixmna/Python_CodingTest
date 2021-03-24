def Solution(happy) :
    answer = []
    temp = int(happy)
    answer.append(str(temp))
    while True :
        sum_happy = 0
        for i in happy :
            sum_happy = sum_happy + int(i)*int(i)
        happy = str(sum_happy)
        if sum_happy == 1 :
            return str(temp) + " is a happy number"
        for i in answer :
            if sum_happy == int(i) :
                return str(temp) + "is a unhappy number"

        answer.append(str(sum_happy))


happy = input()
print(Solution(happy))

"""
HappyNumber를 찾기위한 코드입니다. HappyNumber가맞다면 숫자 + is a happy number를  retrun  하고
unHappy라면 숫자 + is a unHappyNumber를 return 합니다.

function Solution

param happy {str} 사용자게에 입력받은 숫자를 가지고있는 변수입니다.

var answer {str}    각 단계에서 나온 sum_happy를 저장하는 리스트입니다.
var sum_happy {int} happy가  happy한 숫자인지 처리함에  있어서 각 자리수별로 제곱을 하게되는데 제곱을 저장하는 변수입니다.
var temp {int}      happy의 초기값을 저장하여 후에 출력할때  사용하고자 만든 변수입니다.

return 숫자 + "is a happynumber" or 숫자 + "is a nuhappynumver" 입력받은 숫자가 happynumber인지 출력합니다.
"""
"""
HappyNumber는 계산을 계속할때 1로 딱 떨어지거나 루프를통해 무한히 증식하는특징을 지니고있습니다.
고로 계산동안 같은숫자가 나오면 break출력을 해주는 while문을 만들고 sum_happy변수에 happy의 자리값을 제곱하여 입력해줍니다.
그렇게 계산한 sum_happy값은 answer리스트에 저장한후 한번의 과정을 거칠때마다 answer리스트에  현재의 sum_happy값과 동일한 값이 있는지
확인해줍니다. 만약 같은 값이 존재한다면 break하고 unhappy구문을 출력, 1로 출력된다면 happy 구문을 출력합니다.
"""