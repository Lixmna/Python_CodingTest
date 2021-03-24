
def Solution(digits) :
    digits = ''.join(map(str, digits))
    answer = list(map(int, str(int(digits) + 1)))
    return answer



digits=list(map(int, input()))
print(Solution(digits))
"""
입력받는 형식을 문제에 나온대로 int값 리스트로 받은후 변환하는 과정을 거쳤습니다.
문제에나온대로 출력을 하기위해 나온 값을 또 int값으로 변환하여 리스트로  출력해주었습니다.

@function Solution

@param digits {list(int)} int값으로 구성되어있는 리스트입니다.

@var answer {int}         int로 변환한 digits 다시 리스트로 변환하여 출력합니다.

@return answer            변환이 완성된 리스트를 출력합니다.

"""