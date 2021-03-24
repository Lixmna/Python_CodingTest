def solution(prices):
    answer = [0 for i in range(len(prices))]
    data = []
    data.append([prices[0],0])

    for i in range(1,len(prices)) :
        data.append([prices[i],i])

        for j in range(len(data)-2,-1,-1) :
            if data[j][0] > data[j+1][0] :
                answer[data[j][1]] = data[j+1][1] - data[j][1]
                del data[j]
            else :
                break
    
    for i in range(0, len(data)) :
        answer[data[i][1]] = len(prices)-1 - data[i][1]

    return answer

print(solution([1,2,3,2,3,1]))