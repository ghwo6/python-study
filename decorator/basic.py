# 1. 하우징(데코레이터) 제작
def add_sensor_log(func):
    def wrapper():
        print("[시스템] 작동을 준비합니다.")
        
        # 원본 함수(모터) 실행
        func()  
        
        print("[시스템] 작동이 안전하게 완료되었습니다.")
    return wrapper

# 2. 모터에 하우징 씌우기 (@ 기호 사용)
@add_sensor_log
def run_motor():
    # 이곳에 모터를 제어하는 핵심 로직(for/while 등)이 들어갑니다.
    print("모터가 3000 RPM으로 돕니다!")

# 3. 실행
run_motor()