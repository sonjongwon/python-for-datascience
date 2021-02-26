# from collections import defaultdict
#
# d = defaultdict(object)  # Default dictionary를 생성
# d = defaultdict(lambda: 0)  # Default 값을 0으로 설정
# print(d["first"])

text = """A press release is the quickest and easiest way to get free
publicity. If well written, a press release can result in multiple
published articles about your firm and its products. And that can mean
new prospects contacting you asking you to sell to them. 
...""".lower().split()

print(text)

from collections import defaultdict
from collections import OrderedDict

word_count = defaultdict(object)  # Default dictionary를 생성
word_count = defaultdict(lambda: 0)  # Default 값을 0으로 설정

for word in text:
    word_count[word] += 1
for i, v in OrderedDict(sorted(word_count.items(), key=lambda t: t[1], reverse=True)).items():
    print(i, v)
