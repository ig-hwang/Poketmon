import random

def guess_number():
    number = random.randint(1, 20)
    attempts = 0
    print("1부터 20까지의 숫자 중 하나를 맞춰보세요!")

    while True:
        try:
            guess = int(input("숫자를 입력하세요: "))
            attempts += 1
            if guess < number:
                print("너무 작아요!")
            elif guess > number:
                print("너무 커요!")
            else:
                print(f"정답입니다! 시도 횟수: {attempts}회")
                break
        except ValueError:
            print("숫자만 입력해주세요.")

if __name__ == "__main__":
    guess_number()