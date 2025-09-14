# 1. 문자열 생성
text1 = "Hello Python"
text2 = "AI Engineering"
print(text1, text2)

# 2. 인덱싱과 슬라이싱
text = "Python"
print(text[0])  # P
print(text[-1])  # n

word = "Artificial"
print(word[0:4])  # Arti
print(word[:6])  # Artifi
print(word[3:])  # ificial
print(word[::2])  # Atfca

# 3. 문자열 연산
a = "Hello"
b = "World"
print(a + b)  # HelloWorld
print(a * 3)  # HelloHelloHello
print("H" in a)  # True

# 4. 주요 메서드
text = "  python programming  "
print(text.upper())  # 대문자
print(text.lower())  # 소문자
print(text.strip())  # 공백 제거
print(text.replace("python", "AI"))  # 치환
print(text.split())  # 분리

# 5. 탐색 관련 메서드
txt = "banana"
print(txt.find("na"))  # 2
print(txt.rfind("na"))  # 4
print(txt.count("a"))  # 3

# 6. 문자열 포맷팅
name = "Yuju"
age = 22
print(f"My name is {name}, I am {age} years old.")  # f-string
print("My name is {}, I am {} years old.".format("Yuju", 22))  # format
print("My name is %s, I am %d years old." % ("Yuju", 22))  # % 연산자

# 7. 반복문과 문자열
for ch in "AI":
    print(ch)

# 8. 불변성
s = "Python"
# s[0] = "J"   # 오류 발생
s = "J" + s[1:]
print(s)  # Jython
