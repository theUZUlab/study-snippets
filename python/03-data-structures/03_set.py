# 1. 세트 생성
nums = {1, 2, 3, 4, 5}
fruits = {"apple", "banana", "cherry"}
print("세트 생성:", nums, fruits)

# 중복 제거 확인
nums = {1, 2, 2, 3, 3}
print("중복 제거 결과:", nums)  # {1, 2, 3}

# 2. 세트 생성 방법
s1 = {1, 2, 3}
s2 = set([1, 2, 3, 4])
s3 = set()
print("세트 생성:", s1, s2, type(s3))

# 3. 원소 추가
s = {1, 2, 3}
s.add(4)
s.update([5, 6, 7])
print("원소 추가:", s)

# 3. 원소 삭제
s = {1, 2, 3, 4}
s.remove(3)  # 값 3 삭제
s.discard(5)  # 없는 값 삭제 → 오류 없음
popped = s.pop()  # 임의 원소 제거
print("원소 삭제:", s, "제거된 값:", popped)

# 4. 집합 연산
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}
print("합집합:", A | B)
print("교집합:", A & B)
print("차집합:", A - B)
print("대칭차집합:", A ^ B)

# 5. 기타 메서드
s = {1, 2, 3}
print("길이:", len(s))
print("2 포함 여부:", 2 in s)
s.clear()
print("clear() 후:", s)

# 6. 활용 예시 (리스트 중복 제거)
nums = [1, 2, 2, 3, 3, 4]
unique = list(set(nums))
print("리스트 중복 제거:", unique)
