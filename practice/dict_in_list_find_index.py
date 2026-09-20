
category_list = [{"type": "expense", "name": "식비"},
{"type": "expense", "name": "교통"},
{"type": "expense", "name": "주거"},
{"type": "expense", "name": "통신"},
{"type": "expense", "name": "쇼핑"},
{"type": "expense", "name": "여가"},
{"type": "expense", "name": "의료"},
{"type": "expense", "name": "기타"},
{"type": "income", "name": "급여"},
{"type": "income", "name": "부수입"},
{"type": "income", "name": "금융수입"},
{"type": "income", "name": "기타수입"}]

target = {"name":"급여"}


# list 안에 dict가 있어서 원하는 dict를 찾아내기 위해서는 어떻게 해야할지 고민이 되서 찾아봤다.
# enumerate를 사용해서 index와 dict를 for문으로 할당하고
# if dict["key"] == "value" 를 이용해서 원하는 인덱스를 사용가능하다.
# print(index)
for index, item in enumerate(category_list):
    print(f"index = {index} , item = {item}")

    if item["name"] == target["name"]:
        print(index)