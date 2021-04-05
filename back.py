def solution(lottos, win_nums):
    answer = [0,0]
    howmany = lottos.count(0)

    for i in win_nums :
        if i in lottos :
            answer[1] += 1
    
    answer[0]  = answer[1] + howmany

    for i in range (0,2) :
        if answer[i] == 6 :
            answer[i] = 1
        elif answer[i] == 5 :
            answer[i] = 2
        elif answer[i] == 4 :
            answer[i] = 3
        elif answer[i] == 3 :
            answer[i] = 4
        elif answer[i] == 2 :
            answer[i] = 5
        else :
            answer[i] = 6

    return answer

a = [44,1,0,0,31,25]
b = [31,10,45,1,6,19]

print(solution(a,b))