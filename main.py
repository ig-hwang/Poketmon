import math

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Division by zero!"
    return x / y

def square(x):
    return x * x

def sqrt(x):
    if x < 0:
        return "Error: Negative input!"
    return math.sqrt(x)

# 사용자 입력
num1 = float(input("첫 번째 숫자를 입력하세요: "))

print("연산을 선택하세요:")
print("1. 덧셈")
print("2. 뺄셈")
print("3. 곱셈")
print("4. 나눗셈")
print("5. 제곱")
print("6. 제곱근")

choice = input("선택 (1/2/3/4/5): ")

if choice == '1':
    num2 = float(input("두 번째 숫자를 입력하세요: "))
    print("결과:", add(num1, num2))
elif choice == '2':
    num2 = float(input("두 번째 숫자를 입력하세요: "))
    print("결과:", subtract(num1, num2))
elif choice == '3':
    num2 = float(input("두 번째 숫자를 입력하세요: "))
    print("결과:", multiply(num1, num2))
elif choice == '4':
    num2 = float(input("두 번째 숫자를 입력하세요: "))
    print("결과:", divide(num1, num2))
elif choice == '5':
    print("결과:", square(num1))
# 선택지에 조건 추가
elif choice == '6':
    print("결과:", sqrt(num1))
else:
    print("잘못된 선택입니다.")
