import json,os

FILE_DIR = os.path.dirname(__file__)

origin_dict = [
{'type': 'expense', 'name': '식비'},
{'type': 'expense', 'name': '교통'},
{'type': 'expense', 'name': '주거'},
{'type': 'expense', 'name': '통신'},
{'type': 'expense', 'name': '쇼핑'},
{'type': 'expense', 'name': '여가'},
{'type': 'expense', 'name': '의료'},
{'type': 'expense', 'name': '기타'},
{'type': 'income', 'name': '급여'},
{'type': 'income', 'name': '부수입'},
{'type': 'income', 'name': '금융수입'},
{'type': 'income', 'name': '기타수입'}
]



def load_jsonl(filename):

    filename = os.path.join(FILE_DIR,filename)

    try:
        with open(filename,"rt",encoding="utf-8") as f:
            for raw_line in f:
                # 에러 낫었음
                # line_jsonl = json.dumps(raw_line)
                line_jsonl = json.loads(raw_line)
                yield line_jsonl
    except UnicodeDecodeError:
        print(filename," 파일을 utf-8로 읽을 수 없습니다.")
    except FileNotFoundError:
        print(filename," 파일이 없습니다.")
    except json.JSONDecodeError:
        print(filename," 파일을 JSON으로 해독(Decode)할 수 없습니다.")

def save_jsonl(filename):
    # filename = os.path.join(FILE_DIR,filename)

    filename = os.path.join(FILE_DIR,"origin",filename)
    '''
    # FileNotFoundError 테스트
    filename = os.path.join(FILE_DIR,"origin",filename)
    
    ghwo61351@c6r3s6 python-study % /usr/local/bin/python3.12 /Users/ghwo61351/tasks_ghwo6/python-study/json/handle_jsonl.py
    /Users/ghwo61351/tasks_ghwo6/python-study/json/origin 경로(디렉토리가 존재하지 않습니다. 
    /Users/ghwo61351/tasks_ghwo6/python-study/json/origin/save_example.jsonl 을 쓰지 않겠습니다. (폴더를 먼저 만들어 주세요.)
    '''

    try:
        with open(filename,"wt",encoding="utf-8") as f:
            for d in origin_dict:
                f.write(f"{json.dumps(d,ensure_ascii=False)}\n")
    except PermissionError:
        print("권한이 없습니다.")
    except IsADirectoryError:
        print("폴더 입니다.")
    except FileNotFoundError:
        print(os.path.dirname(filename),"경로(디렉토리가 존재하지 않습니다.","\n",filename,"을 쓰지 않겠습니다. (폴더를 먼저 만들어 주세요.)")

if __name__ =="__main__":

    # generator jsonl 읽기 테스트
    # jsonl_gen = load_jsonl("categories.jsonl")
    # for line in jsonl_gen:
    #     print(line)

    # jsonl타입으로 저장하는 예제
    save_jsonl("save_example.jsonl")