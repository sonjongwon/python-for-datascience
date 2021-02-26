import csv


def get_key(item):  # 정렬을 위한 함수
    return item[1]  # 신경 쓸 필요 없음


command_data = []

# 파일 읽어오기
with open("command_data.csv", "r", encoding="utf8") as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
    for row in spamreader:
        command_data.append(row)

command_counter = {}  # dict 생성, 아이디를 key 값, 입력 줄 수를 value 값
for data in command_data:  # list 데이터를 dict로 변경
    if data[1] in command_counter.keys():  # 아이디가 이미 key 값으로 변경 되었을 때
        command_counter[data[1]] += 1  # 기존 출현한 아이디
    else:
        command_counter[data[1]] = 1  # 처음 나온 아이디

dict_list = []  # dict 를 list 로 변경
for key, value in command_counter.items():
    temp = [key, value]
    dict_list.append(temp)

sorted_dict = sorted(dict_list, key=get_key, reverse=True)  # list를 입력 줄 수로 정렬
print(sorted_dict[:100])  # List의 상위 10개 값만 출력
