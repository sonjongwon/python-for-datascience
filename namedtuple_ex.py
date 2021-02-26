# Tuple 형태로 Data 구조체를 저장하는 방법
# 저장되는 data의 variable을 사전에 지정해서 저장함
from collections import namedtuple

point = namedtuple('Point', ['x', 'y'])
p = point(11, y=22)
print(p[0] + p[1])

x, y = p
print(x, y)
print(p.x + p.y)
print(point(x=11, y=22))
