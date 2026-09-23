import functools
import time


# 1. 데코레이터 금형 (다이얼 역할: seconds 값을 받음)
def auto_delay(seconds=1.0):
    
    # 2. 실제 데코레이터
    def decorator(func):
        
        # 3. 유니버설 척이 장착된 하우징 (*args, **kwargs가 모든 형태의 인자를 흡수)
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            print(f"[시스템] {seconds}초 대기 중...")
            time.sleep(seconds)
            
            # 흡수한 인자를 원본 부품(func)에 그대로 전달하며 실행
            return func(*args, **kwargs) 
            
        return wrapper
    return decorator

# --- [실제 활용] ---

# 모터에는 0.5초 대기 껍데기를 씌움
@auto_delay(seconds=0.5)
def run_motor(rpm, direction="CW"):
    print(f"모터가 {direction} 방향으로 {rpm} RPM 회전합니다.")

# 센서에는 2초 대기 껍데기를 씌움
@auto_delay(seconds=2.0)
def read_sensor(sensor_id):
    print(f"[{sensor_id}] 센서값을 성공적으로 읽어왔습니다.")

# 실행
run_motor(3000, direction="CCW")
read_sensor("TEMP_01")