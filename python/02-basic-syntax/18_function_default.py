# 기본값 매개변수
def greet(name="Guest"):
    print(f"안녕하세요, {name}님")


greet()  # 인자 생략 → 기본값 "Guest"
greet("UZU")  # 인자 전달 → "UZU"
