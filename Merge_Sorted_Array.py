def Solution(nums1,m, nums2, n) :
    answer = []
    nums1_counter = 0
    nums2_counter = 0
    while True :
        if nums1_counter == m :
            for i in range(nums2_counter, n) :
                answer.append(nums2[i])
            break

        if nums2_counter == n :
            for i in range(nums1_counter, m) :
                answer.append(nums1[i])
            break

        if nums1[nums1_counter] < nums2[nums2_counter] :
            answer.append(nums1[nums1_counter])
            nums1_counter = nums1_counter + 1
        else :
            answer.append(nums2[nums2_counter])
            nums2_counter = nums2_counter + 1

    return answer

nums1=list(map(int, input().split()))
nums2=list(map(int, input().split()))

print(Solution(nums1, len(nums1), nums2, len(nums2)))
"""
지금까지 짠 코드와 입력방식에 차이점이 있습니다. 변수의값이 1의자리수가 넘어갈수 있기때문에 스페이스바로써 변수를 구분하도록 하였습니다.

Merge Sort는 사실 재귀함수를 통하여 코드를 만드는것이 정석적인 방식이라고 생각하지만 본 프로그램 테스트에서는 두개의 정렬된 머지 리스트를 주어줌으로써 코드를 실행시킬수 있기때문에
재귀함수를 사용하지는 않았다. while문을 통해 두 리스트를 merge하는 과정을 수행하는 Solution 함수이다.
문제에서 nums1에 nums2리스트에 잇는값을 전부 넣을수 있는 공간이 존재한다는것을 가정한다고 하였기에 최선의 방법은 nums1 리스트에
추가하여 푸는것이였겟지만 쉽게 정답을 저장하는 리스트가 무엇인지 알아보기 쉽게 하기위하여 answer리스트를 새로 생성하여 풀게되엇다.

@function Solution

@param nums1 {list(int)} int값으로 구성되어있는 리스트입니다.
@param m {int}           nums1리스트의 구성개수를 나타내주는 변수입니다.
@param nums2 {list(int)} int값으로 구성되어있는 리스트입니다.
@param n {int}           nums2리스트의 구성개수를 나타내주는 변수입니다.

@var answer {int}        Merge하여 nums1 리스트와 nums2 리스트를 합해준 리스트입니다.

@return answer            변환이 완성된 리스트를 출력합니다.
"""