def solution(rows, columns, queries):
    answer = [99999 for i in range(len(queries))]
    data = [[0 for col in range(columns)] for row in range(rows)]

    cnt = 1
    point = 0

    x = [1,0,-1,0]
    y = [0,1,0,-1]

    q = []

    for i in range(0,rows) :
        for j in range(0, columns) :
            data[i][j] = cnt
            cnt += 1
    for k in range(len(queries)) :
        q = []
        cnt = 1
        point = 0
        q.append([queries[k][0]-1, queries[k][1]-1])
        q.append([queries[k][0]-1+y[point], queries[k][1]+x[point]-1])
        
        temp = data[q[0][0]][q[0][1]]
        
        while True :
            change = data[q[cnt][0]][q[cnt][1]]
            data[q[cnt][0]][q[cnt][1]] = temp
            temp = change

            if temp < answer[k] :
                answer[k] = temp
            
            if q[cnt][1] == queries[k][3]-1 and point == 0 :
                point += 1
            if q[cnt][0] == queries[k][2]-1 and point == 1 :
                point += 1
            if q[cnt][1] == queries[k][1]-1 and point == 2 :
                point += 1
            if q[cnt][0] == queries[k][0]-1 and point == 3 :
                break

            q.append([q[cnt][0]+y[point], q[cnt][1]+x[point]])
            cnt+=1

    return answer

print(solution(	6,	6,	[[2,2,5,4],[3,3,6,6],[5,1,6,3]]))