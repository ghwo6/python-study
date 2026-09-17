## argparse의 subparseer를 이용한 예제이다.

### python ./argparse/run05.py --help
usage: run05.py [-h] {build,flash} ...

하드웨어 빌드 & 플래시 CLI 도구

positional arguments:
  {build,flash}  실행할 하위 명령
    build        펌웨어 빌드
    flash        디바이스에 바이너리 전송

options:
  -h, --help     show this help message and exit

### python ./argparse/run05.py build --help
usage: run05.py build [-h] [-O OPT] {esp32,stm32,rpi}

positional arguments:
  {esp32,stm32,rpi}  타겟 디바이스

options:
  -h, --help         show this help message and exit
  -O OPT, --opt OPT  최적화 레벨 (기본값: O2)

### python ./argparse/run05.py build esp32 -O Os
- [BUILD] 타겟 : esp32, 최적화 레벨 : 0s

### python tool.py flash -p /dev/ttyUSB0
- [FLASH] 포트: /dev/ttyUSB0, 전송 속도 : 115200bps