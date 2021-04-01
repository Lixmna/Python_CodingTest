def solution(skill, skill_trees):
    answer = 0
    skill = list(map(str, skill))
    skill_check = 0

    answer_check = True

    for i in skill_trees :

        temp = list(map(str, i))
        skill_check = 0
        answer_check = True
        
        for j in range(0,len(temp)) : 
            if temp[j] in skill :
                if temp[j] == skill[skill_check] :
                    skill_check = skill_check + 1
                else :
                    answer_check = False
                    break

        if answer_check == True :
            answer += 1


    return answer
