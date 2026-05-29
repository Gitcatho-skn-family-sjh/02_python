#논리형 Boolean

a = True
b = False
print(a, type(a))
print(b, type(b))

# 비교 연산
# A > B : A 가 B 보다 크면 True, 아니면 False
# A >= B : A 가 B 이상이면 True, 아니면 False

print("1 > 0.5:", 1 > 0.5)
print("1 < 0.5:", 1 < 0.5)
print("1 >= 0.5:", 1 >= 0.5)
print("1 <= 0.5:", 1 <= 0.5)
print("1 == 1:", 1 == 1)
print("1 != 1:", 1 != 1)

#논리 부정 연산(not)
print(not True)
print(not False)
print(True)
print(not True and True)
print(not True and False)
print(not True or True)