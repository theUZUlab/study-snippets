# 1. 튜플 생성
fruits = ("apple", "banana", "cherry")
nums = (1, 2, 3, 4, 5)
mixed = (1, "python", True, 3.14)

print("튜플 생성:", fruits, nums, mixed)

# 2. 인덱싱
print("첫 번째 과일:", fruits[0])  # apple
print("마지막 과일:", fruits[-1])  # cherry

# 2. 슬라이싱
nums = (10, 20, 30, 40, 50)
print("슬라이싱 1~3:", nums[1:4])  # (20, 30, 40)
print("처음부터 3개:", nums[:3])  # (10, 20, 30)
print("2번부터 끝까지:", nums[2:])  # (30, 40, 50)

# 3. 튜플 불변성
t = (1, 2, 3)
# t[0] = 100  # TypeError 발생 → 주석 처리
print("불변성 확인:", t)

# 튜플 안의 리스트는 수정 가능
nested = (1, [2, 3], 4)
nested[1][0] = 99
print("튜플 안 리스트 수정:", nested)

# 4. 튜플 메서드
nums = (1, 2, 2, 3, 4)
print("2의 개수:", nums.count(2))
print("3의 위치:", nums.index(3))


# 5. 활용 예시
# 함수에서 여러 값 반환
def get_position():
    return (100, 200)


x, y = get_position()
print("좌표 반환:", x, y)

# 언패킹 활용
person = ("Yuju", 22, "AI Student")
name, age, major = person
print("언패킹 결과:", name, age, major)
