def Solution(nums, target) :
    answer = []
    finish = 0
    for i in range(len(nums)) :
        if nums[i] > target :
            continue
        for j in range(i, len(nums)) :
            if nums[j] > target :
                continue
            if nums[i] + nums[j] == target :
                answer.append(i)
                answer.append(j)
                finish = 1
                break;
        if finish == 1 :
            break;
                
    return answer


nums=list(map(int, input().split()))
target = int(input())

print(Solution(nums,target))

"""
Two Sum은 nums리스트에 들어있는 두 변수값을 합하였을때 무조건 정답이 있다고 가정한 프로그램입니다.
현재 구현된 Solution함수는 nums값에서 모든경우의 수를 비교하며 더해 정답을 만들어내는 함수입니다. 
만약 nums의 변수가 target의 크기보다 크다면 continue하는 방식으로 경우의수를 최소화 하였습니다.

@function Solution

@param nums {list(int)}  int값으로 입력받아 구성되어있는 리스트입니다.
@param target {int}      우리가 합하여 구하고자하는 nums값의 int를 가지고있는 리스트입니다.

@var finish {int}         만약 target값을 찾았다면 불필요한 작업없이 프로그램을 끝내기 위하여 만든 변수입니다.
@var answer {int}         nums에서 찾아낸 두 변수의 위치를 저장히기 위해 만든 리스트입니다.

@return answer            nums에서 찾아낸 두 변수의 위치를 출력합니다.
"""