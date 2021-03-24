def solution(n):
    answer = ''

    binary = []

    while n > 3 :
        temp = n % 3;
        if temp == 0 :
            binary.append(3)
            n = int(n / 3) - 1;
        else :
            binary.append(n % 3)
            n = int(n / 3)
    
    binary.append(n)
    
    while len(binary) != 0 :
        num = binary.pop()
        if num == 3 :
            answer += '4'
        else :
            answer += str(num)
    
    return answer
