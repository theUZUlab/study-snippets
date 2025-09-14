# break
for i in range(10):
    if i == 5:
        break
    print(i)

# continue
for i in range(5):
    if i % 2 == 0:
        continue
    print("홀수:", i)

# else
for i in range(3):
    print("i =", i)
else:
    print("반복 정상 종료")
