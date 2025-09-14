# 문자열 : 작은따옴표, 큰따옴표, 삼중따옴표
s1 = "Hello"
s2 = "World"
s3 = """멀티라인
문자열"""
print(s1, s2)
print(s3)

# 시퀀스 성질 : 인덱싱, 슬라이싱
word = "Python"
print(word[0])  # 'P'
print(word[-1])  # 'n'
print(word[0:3])  # 'Pyt'
print(word[::2])  # 'Pto'
print(word[::-1])  # 역순
