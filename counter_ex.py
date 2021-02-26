from collections import Counter

# c = Counter()  # a new, empty counter
c = Counter("gallahad")
print(c)

c = Counter({"red": 4, "blue": 2})  # a new counter from a mapping
print(c)
print(list(c.elements()))

c = Counter(cats=4, dog=8)  # a new counter from keyword args
print(c)
print(list(c.elements()))

c = Counter(a=4, b=2, c=0, d=-2)
d = Counter(a=1, b=2, c=3, d=4)
c.subtract(d)
print(c)
print(c + d)
print(c & d)
print(c | d)

text = """A press release is the quickest and easiest way to get free
publicity. If well written, a press release can result in multiple
published articles about your firm and its products. And that can mean
new prospects contacting you asking you to sell to them. 
...""".lower().split()

print(Counter(text))
print(Counter(text)["a"])
