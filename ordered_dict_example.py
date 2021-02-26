# d = {}
#
# d['x'] = 100
# d['y'] = 200
# d['z'] = 300
# d['l'] = 500
#
# for k, v in d.items():
#     print(k, v)

from collections import OrderedDict

d = OrderedDict()
d['x'] = 100
d['y'] = 200
d['z'] = 300
d['l'] = 500

# for k, v in d.items():
#     print(k, v)
#
# Dict type의 값을 value 또는 key 값으로 정렬할 때 사용
for k, v in OrderedDict(sorted(d.items(), key=lambda t: t[0])).items():
    print(k, v)

for k, v in OrderedDict(sorted(d.items(), key=lambda t: t[1])).items():  # reverse = True 추가시 역순
    print(k, v)
