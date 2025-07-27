import random

quotes = [
    "삶이 있는 한 희망은 있다. - 키케로",
    "성공은 준비와 기회의 만남이다. - 세네카",
    "오늘 걷지 않으면 내일은 뛰어야 한다. - 독일 속담",
    "기회는 일어나는 것이 아니라 만들어내는 것이다. - 크리스 그로서",
    "행복은 방향이지 목적지가 아니다. - 로이 굿맨"
]

def show_random_quote():
    quote = random.choice(quotes)
    print("\n💬 오늘의 명언:")
    print(f"👉 {quote}")

if __name__ == "__main__":
    show_random_quote()