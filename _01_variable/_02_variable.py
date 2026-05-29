#변수(variable)
# - 값(literal)을 저장하는 메모리상의 공간
# - 각 변수마다 이름이 지정되어 있음 (이름이 불러서 사용)

# 변수 선언방법
# 변수명 = 값
a = 10
b = "홍길동"

print("a =", a)
print("b =", b)

#대입 연산자(=)
# - 우항의 값을 좌항의 변수에 대입
num = 100
print("num =", num)

num = "abc"
print("num =", num)


#변수 명은 대소문자 구분함
#변수명은 소문자 추천 단 대문자도 가능은함
team_name = "오지라퍼스"
print(team_name)    # 오지라퍼스

Team_name = "Ohgiraffers"
print(team_name)    # 오지라퍼스
print(Team_name)    # Ohgiraffers

팀명 = "3조"
print("밥조: ",팀명)

#변수명은 숫자로 시작해서는 안된다(문법오류)
name_1 ="콩쥐"
# 1_name ="팥쥐" #문접 에러
_1_name ="신데렐라"
#_제외한 특수문자는 사용불가
# team-name = "오지라퍼스" #error

# 예약어는 변수명으로 사용불가
# if for 등등
import keyword
print(keyword.kwlist)
