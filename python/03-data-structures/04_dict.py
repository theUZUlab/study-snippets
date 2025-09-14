# 1. 딕셔너리 생성
student = {"name": "Yuju", "age": 22, "major": "AI Engineering"}
print("딕셔너리 생성:", student)

# 2. 키와 값 접근
print(student["name"])  # Yuju
print(student.get("age"))  # 22

# 3. 값 변경
student["age"] = 23
print("값 변경:", student)

# 3. 새 키-값 추가
student["grade"] = "A"
print("새 키 추가:", student)

# 3. 키 삭제
del student["major"]
grade = student.pop("grade")
print("삭제 후:", student, "꺼낸 값:", grade)

student.clear()
print("clear() 후:", student)

# 4. 주요 메서드
person = {"name": "Yuju", "age": 22}
print("keys:", person.keys())
print("values:", person.values())
print("items:", person.items())

for k, v in person.items():
    print(k, ":", v)

# 5. 빈도수 계산
text = "banana"
counter = {}
for ch in text:
    counter[ch] = counter.get(ch, 0) + 1
print("빈도수 계산:", counter)

# 6. 중첩 딕셔너리
students = {
    "1001": {"name": "Yuju", "major": "AI"},
    "1002": {"name": "HyeWon", "major": "CS"},
}
print("중첩 딕셔너리 접근:", students["1001"]["name"])
