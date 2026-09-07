import random
import string


# 아이스크림 클래스를 사용해서 이를 출력하는 프로그램 - 개선판
def generate_id() -> str:
    return "".join(random.choices(string.ascii_uppercase, k=12))


class Icecream:
    def __init__(self, name: str, flavor: str):
        self.name = name
        self.flavor = flavor

    def __str__(self) -> str:
        return f"{self.name} - {self.flavor} flavor"


def main() -> None:
    icecream = Icecream(name="together", flavor="vanilla")
    print(icecream)


if __name__ == "__main__":
    main()