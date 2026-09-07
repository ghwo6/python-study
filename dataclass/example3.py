import random
import string
from dataclasses import dataclass

# 데이터클래스
# 아이스크림 클래스를 사용해서 이를 출력하는 프로그램
def generate_id() -> str:
    return "".join(random.choices(string.ascii_uppercase, k=12))


@dataclass
class Icecream:
    name: str
    flavor: str

    def __str__(self)->str:
        return f"{self.name} - {self.flavor}"


def main() -> None:
    icecream = Icecream(name="together", flavor="vanilla")
    print(icecream)


if __name__ == "__main__":
    main()