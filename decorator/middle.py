import functools


def add_sensor_log(func):
    # 원래 함수(func)의 명판을 복사해서 바로 아래 wrapper에 붙임
    @functools.wraps(func) 
    def wrapper():
        print("[시스템] 작동 준비")
        func()
        print("[시스템] 작동 완료")
    return wrapper

@add_sensor_log
def run_motor():
    """이 함수는 3000 RPM으로 메인 모터를 돌립니다."""
    print("모터 가동!")

# 테스트: 부품의 이름과 설명서를 확인해보자
print(run_motor.__name__) 
# 출력: run_motor 
# (만약 @functools.wraps가 없었다면 'wrapper'라고 출력됨)

print(run_motor.__doc__)  
# 출력: 이 함수는 3000 RPM으로 메인 모터를 돌립니다.