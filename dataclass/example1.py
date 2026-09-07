import random
import string

# 아이스크림 클래스를 사용해서 이를 출력하는 프로그램
def generate_id() -> str:
    # return "".join(random.choices(string.ascii_uppercase, k=12))
    return "".join(random.choices(string.ascii_uppercase, k=12))
    # 아래에서 사용예정


class Icecream:
    def __init__(self, name: str, flavor: str):
        self.name = name
        self.flavor = flavor


def main() -> None:
    icecream = Icecream(name="togegther", flavor="vanilla")
    print(icecream)


if __name__ == "__main__":
    # main()
    print(generate_id())