import functools
from pathlib import Path
import os

FOLDER = Path(__file__).parent

def atomic_box_swap(box_attr_memo:str):
    def decorator(func):

        @functools.wraps(func)
        def wrapper(self,*args,**kwargs):

            current_box:Path = FOLDER / getattr(self,box_attr_memo)
            temp_box = current_box.with_suffix(".tmp")

            parts_generator = func(self,*args,**kwargs)

            if parts_generator is None:
                print("작업할 내용이 없습니다.")
                return False

            print(f"[시스템] 임시 상자({temp_box})에 정상 부품을 담기 시작합니다.")

            # 임시 파일(상자)에 하나씩 기록
            with open(temp_box,"w",encoding="utf-8") as f:
                f.writelines(part + "\n" for part in parts_generator)

            os.replace(temp_box,current_box)
            print(f"[시스템] {current_box} 교체가 안전하게 완료되었습니다.")
            return True

        return wrapper
    return decorator

class FactoryLine:
    def __init__(self):
        self.target_file = "parts_box.txt"

        # 테스트용 초기 데이터 생성
        with open(self.target_file,"wt",encoding="utf-8") as f:
            f.write('정상기어\n불량모터\n정상벨트\n')

    #데코레이터에게 "내 target_file 속성을 찾아서 덮어써라" 라고 지시
    @atomic_box_swap("target_file")
    def remove_defect(self,name:str):
        """불량품을 제외한 정상품만 하나씩 컨베이어 벨트(yield)로 흘려보냅니다."""
        with open(self.target_file,"r",encoding="utf-8") as f:
            for line in f:
                part = line.strip()
                # name 이면 건너띄고, name이 아니면 yield로 데코레이터에게 보낸다.
                if part != name:
                    yield part


factory = FactoryLine()
if __name__ =="__main__":
    factory.remove_defect("불량모터")
