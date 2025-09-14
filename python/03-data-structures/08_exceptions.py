# 1. SyntaxError & RuntimeError
# SyntaxError는 실행 전에 코드 해석 단계에서 발생하므로 실제 실행 시 주석 처리
# print("Hello"    # SyntaxError 예시

print(10 / 2)  # 정상 실행
# print(10 / 0)    # RuntimeError: ZeroDivisionError


# 2. try ~ except 기본 구조
try:
    x = int(input("숫자를 입력하세요: "))
    print(10 / x)
except ZeroDivisionError:
    print("0으로 나눌 수 없습니다.")
except ValueError:
    print("숫자가 아닙니다.")


# 3. 예외 종류별 처리
try:
    data = [1, 2, 3]
    print(data[5])  # IndexError
except IndexError:
    print("인덱스 범위를 벗어났습니다.")


# 4. 다중 except와 예외 묶음
try:
    num = int("python")  # ValueError 발생
except (ValueError, TypeError):
    print("잘못된 형 변환입니다.")


# 5. else와 finally
try:
    print("정상 실행")
except:
    print("예외 발생")
else:
    print("예외 없이 끝남")
finally:
    print("항상 실행되는 finally 블록")


# 6. 예외 객체와 as
try:
    1 / 0
except ZeroDivisionError as e:
    print("예외 메시지:", e)


# 7. 사용자 정의 예외
class NegativeNumberError(Exception):
    pass


def check_positive(num):
    if num < 0:
        raise NegativeNumberError("음수는 허용되지 않습니다.")


try:
    check_positive(-5)
except NegativeNumberError as e:
    print("사용자 정의 예외 발생:", e)
