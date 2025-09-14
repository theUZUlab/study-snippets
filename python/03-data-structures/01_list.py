# 1. 리스트 생성
fruits = ["apple", "banana", "cherry"]
numbers = [1, 2, 3, 4, 5]
mixed = [1, "python", True, 3.14]

print("리스트 생성:", fruits, numbers, mixed)

# 2. 인덱싱
print("첫 번째 과일:", fruits[0])  # apple
print("마지막 과일:", fruits[-1])  # cherry

# 2. 슬라이싱
nums = [10, 20, 30, 40, 50]
print("슬라이싱 1~3:", nums[1:4])  # [20, 30, 40]
print("처음부터 3개:", nums[:3])  # [10, 20, 30]
print("2번부터 끝까지:", nums[2:])  # [30, 40, 50]
print("2칸 간격:", nums[::2])  # [10, 30, 50]

# 3. 리스트 수정
fruits[1] = "grape"
print("수정 후 fruits:", fruits)

nums = [1, 2, 3]
nums.append(4)  # 맨 뒤 추가
nums.insert(1, 10)  # 특정 위치 추가
print("추가 후 nums:", nums)

nums = [1, 2, 3, 4]
del nums[1]  # 인덱스 삭제
nums.remove(3)  # 값 삭제
popped = nums.pop()  # 꺼내면서 삭제
print("삭제 후 nums:", nums)
print("pop된 값:", popped)

# 4. 주요 메서드
nums = [5, 2, 8, 1]
nums.sort()  # 정렬
nums.reverse()  # 뒤집기
print("정렬+뒤집기:", nums)
print("값 5 위치:", nums.index(5))
print("값 2 개수:", nums.count(2))

# 5. 리스트와 반복문
fruits = ["apple", "banana", "cherry"]
print("for문으로 값 출력:")
for f in fruits:
    print(f)

print("인덱스와 함께 출력:")
for i in range(len(fruits)):
    print(i, fruits[i])

# 6. 중첩 리스트
matrix = [[1, 2], [3, 4], [5, 6]]
print("matrix[0]:", matrix[0])
print("matrix[1][1]:", matrix[1][1])
