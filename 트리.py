
answer_check = [0 for i in range(0,10001)]

def solution(enroll, referral, seller, amount):
    answer = []

    for i in range(0,len(seller)) :
        amount[i] = amount[i] * 100

        enroll_index = enroll.index(seller[i])
        checker(enroll, referral, seller, amount[i], enroll_index)

    for i in range(0,len(enroll)) :
        answer.append(answer_check[i])


    return answer

def checker(enroll, referral, seller, amount, enroll_index) :
    answer_check[enroll_index] += amount - int(amount/10)
    if referral[enroll_index] == '-' :
        return    

    enroll_index = enroll.index(referral[enroll_index])

    checker(enroll, referral, seller, int(amount/10), enroll_index) 


print(solution(["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"],	["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"],	["young", "john", "tod", "emily", "mary"],	[12, 4, 2, 5, 10]))