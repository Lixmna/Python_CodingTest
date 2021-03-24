def soulution(fibo) :
    answer = []
    answer.append(0)
    answer.append(1)
    for i in range(2, int(fibo)+1) :
        answer.append(answer[i-1] + answer[i-2])
    print(answer[int(fibo)])


fibo = input()
soulution(fibo)
