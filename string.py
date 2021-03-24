
def Solution(Partial_String) :
    Partial_String = list(map(str, Partial_String))
    Back_Word = len(Partial_String)-1
    temp = Partial_String[0]
    for i in range(len(Partial_String)) :
        if Partial_String[i] == 'a' or Partial_String[i] == 'e' or Partial_String[i] =='i' or Partial_String[i] =='o'or Partial_String[i] =='u' :
            for j in range(Back_Word,i,-1) :
                temp = Partial_String[j]
                if Partial_String[j] == 'a' or Partial_String[j] == 'e' or Partial_String[j] == 'i' or Partial_String[j] == 'o' or Partial_String[j] == 'u' :
                    Partial_String[j] = Partial_String[i]
                    Partial_String[i] = temp
                    Back_Word = j-1
                    break
        if Back_Word <= i :
            break
    
    answer = (''.join(Partial_String))

    return answer


Partial_String=input()

print(Solution(Partial_String))

"""
Partial_String_Revers를 하기위하여 만든 Solution함수 이다. 
단어나 문장에 존재하는 모음을 앞에서부터 찾아 뒤쪽부터 시작한 모듬들과 바꿔주는 함수이다.

@fucntion Solution

@param Partial_String {str} 입력받은 단어를 저장해둔 string 변수이다.

@var Back_Word {int}        Partial_string의 값을 뒤에서부터 찾기위해 길이를 저장하고 후에 프로그램을 실행하면서 찾은값의 위치를 저장하는 변수이다.
@var temp      {str}        Partial_string의 값을저장하여 서로 바꿔주기 위해 선언한 변수이다.
@var  answer   {str}        답을 저장하기위헤 선언한 string 변수이다.

return answer               변환된 Partial_string을 합쳐서 출력해준다.
"""

