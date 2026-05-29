# number(숫자형)
# - 정수
# - 실수
# - 복소수



#type(변수명 | 값) 함수 : 변수 또는 값의 타입을 확인

#정수 (int)
n = 123
print(n, type(n))

price = 10_000_000_000; #정수 자릿수 구분
print(price, type(price))

# 정수의 최대값
import sys
print(sys.maxsize, type(sys.maxsize))

#2진법, 8진법, 16진법
a = 0b100 # 4
print(a, type(a))
b = 0o23 # 19
print(b, type(b))
c = 0xff # 255
print(c, type(c))

#실수float
f1 = 123.456
print(f1, type(f1))

f2 = -99999.99999
print(f2, type(f2))

f3 = 1.0123456789012345
print(f3, type(f3))

#---------------------------
#복소수 (complex)
c =2j
print(c, type(c))
d = 3 + 4j
print(d, type(d))

#------------
# 산술 연산 ( +, -, *, /, //(몫), %(나머지))

print("산술연산")
print(1+2) # 3
print(1-2) # -1
print(1*2) # 2
print(1/2) # 0.5
print(1//2) # 0
print(1%2) # 1

print(3**2)
print(3**3)
print(2**63)
