# console_io_examples.py
# [Python] 콘솔 입출력
# print, input, 형 변환, 여러 값 입력, 출력 포맷팅 예제

# 1. 출력 (print)
print("Hello Python")
print(10, 20, 30)  # 기본 공백 구분

# 1.1 sep
print("2025", "09", "14", sep="-")

# 1.2 end
print("Hello", end=" ")
print("Python")

# 1.3 f-string
name = "Yuju"
age = 22
print(f"My name is {name}, I am {age} years old.")

# 2. 입력 (input)
# name = input("이름을 입력하세요: ")
# print("안녕하세요,", name)

# 3. 입력값 변환
# age = int(input("나이를 입력하세요: "))
# print("내년 나이는", age + 1)

# 4. 여러 값 입력
# a, b = input("두 수를 입력하세요: ").split()
# print(a, b)

# a, b = map(int, input("두 수를 입력하세요: ").split())
# print(a + b)

# nums = list(map(int, input("여러 숫자 입력: ").split()))
# print(nums)

# 5. 출력 포맷팅
print("이름: {}, 나이: {}".format("Yuju", 22))
print("이름: %s, 나이: %d" % ("Yuju", 22))
