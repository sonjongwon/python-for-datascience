print(1, 2, 3)
print("a"+" "+"b"+" "+"c")
print("%d %d %d" % (1, 2, 3))
print("{} {} {}".format("a", "b", "c"))

print("="*50)
print('%s %s' % ('one', 'two'))
print('{} {}'.format('one', 'two'))
print('%d %d' % (1, 2))
print('{} {}'.format(1, 2))

print("="*50)
print("I eat %d apples." % 3)
print("I eat %s apples." % "five")
number = 3; day = "three"
print("I ate %d apples. I was sick for %s days." % (number, day))
print("Product: %s, Price per unit: %f." % ("Apple", 5.243))

print("="*50)
age = 36; name = "Jongwon Son"
print("I'm {0} years old".format(age))
print("My name is {0} and {1} years old.".format(name, age))

print("="*50)
print("Product: %5s, Price per unit: %.5f." % ("Apple", 5.243))
print("Product: {0:5s}, Price per unit: {1:.5f}.".format("Apple", 5.243))

print("="*50)
print("Product: %10s, Price per unit: %10.3f." % ("Apple", 5.243))
print("Product: {0:>10s}, Price per unit: {1:10.3f}.".format("Apple", 5.243))

print("="*50)
print("Product: %(name)5s, Price per unit: %(price)10.5f." % {"name": "Apple", "price": 5.243})
print("Product: {name:>10s}, Price per unit: {price:10.5f}.".format(name="Apple", price=5.243))
