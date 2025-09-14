# 지역 변수와 전역 변수 (scope)
x = 10  # 전역 변수


def local_example():
    x = 5  # 지역 변수 (함수 내부 전용)
    print("함수 내부:", x)


local_example()
print("함수 외부:", x)


# global 키워드 사용 (권장하지 않음)
def global_example():
    global x
    x = 20
    print("함수 내부(global):", x)


global_example()
print("함수 외부(global):", x)
