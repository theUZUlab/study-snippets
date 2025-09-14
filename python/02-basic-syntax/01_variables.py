# 변수는 데이터를 저장하는 이름표다.
# 파이썬은 동적 타입이므로 할당 시 자료형이 결정된다.
x = 10  # int
y = 3.14  # float
name = "Yuju"  # str
print(x, y, name)
print(type(x), type(y), type(name))

# 같은 변수에 다른 자료형 재할당 가능
a = 100
print(type(a))  # <class 'int'>
a = "Hello"
print(type(a))  # <class 'str'>

# 변수 이름 규칙 예시
user_name = "theUZUlab"  # 가능
# 1st_value = 100   # 숫자로 시작 불가 (주석 처리)
