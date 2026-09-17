import argparse

def handle_build(args):
    print(f"[BUILD] 타겟 : {args.target}, 최적화 레벨 : {args.opt}")

def handle_flash(args):
    print(f"[FLASH] 포트: {args.port}, 전송 속도 : {args.baud}bps")

def main():
    # 1. 메인 파서 생성
    parser = argparse.ArgumentParser(description="하드웨어 빌드 & 플래시 CLI 도구")

    # 2. 서브파서 컨테이너 추가 (dest로 입력된 서브커맨드 이름 저장)
    subparsers = parser.add_subparsers(dest="command", required=True,help="실행할 하위 명령")

    # 3. 'build' 서브커맨드 파서 정의
    parser_build = subparsers.add_parser("build",help="펌웨어 빌드")
    parser_build.add_argument("target", choices=["esp32","stm32","rpi"],help="타겟 디바이스")
    parser_build.add_argument("-O","--opt",default="O2",help="최적화 레벨 (기본값: O2)")
        # 실행할 함수 매핑
    parser_build.set_defaults(func=handle_build)

    # 4. 'flash' 서브커맨드 파서 정의
    parser_flash = subparsers.add_parser("flash",help="디바이스에 바이너리 전송")
    parser_flash.add_argument("-p","--port",required=True, help="시리얼 포트 (예: /dev/ttyUSB0)")
    parser_flash.add_argument("-b","--baud",type=int,default=115200,help="전송 속도 (기본값 : 115200)")
    parser_flash.set_defaults(func=handle_flash)

    # 5. 파싱 및 실행
    args = parser.parse_args()
    args.func(args)

if __name__ =="__main__":
    main()
