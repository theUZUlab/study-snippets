# file_io_examples.py
# [Python] 파일 입출력
# 파일 열기, 쓰기, 읽기, with문, 포인터, 복사 예제

# 1. 파일 열기와 닫기
f = open("example.txt", "w", encoding="utf-8")
f.write("Hello File I/O")
f.close()

# 2. with문 사용
with open("example.txt", "w", encoding="utf-8") as f:
    f.write("Hello with")

# 3. 파일 쓰기
# 3.1 한 줄 쓰기
with open("example.txt", "w", encoding="utf-8") as f:
    f.write("첫 번째 줄\n")
    f.write("두 번째 줄\n")

# 3.2 여러 줄 쓰기
lines = ["Python\n", "AI\n", "IoT\n"]
with open("example.txt", "w", encoding="utf-8") as f:
    f.writelines(lines)

# 4. 파일 읽기
# 4.1 전체 읽기
with open("example.txt", "r", encoding="utf-8") as f:
    data = f.read()
    print(data)

# 4.2 한 줄씩 읽기
with open("example.txt", "r", encoding="utf-8") as f:
    line1 = f.readline()
    line2 = f.readline()
    print(line1, line2)

# 4.3 모든 줄 읽기
with open("example.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()
    for line in lines:
        print(line.strip())

# 5. 파일 포인터
with open("example.txt", "r", encoding="utf-8") as f:
    print(f.tell())  # 현재 위치
    f.seek(0)  # 처음으로 이동
    print(f.readline())

# 6. 파일 복사
with open("07_source.txt", "r", encoding="utf-8") as src:
    with open("copy.txt", "w", encoding="utf-8") as dst:
        for line in src:
            dst.write(line)
