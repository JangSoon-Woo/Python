#
"""
주석
주석
주석
"""

# 1

import random
print("Hello, World!")

# 2

if 5 > 2:
    print("Five is greater than two!")

# 3
x = 4
y = "test"
z = 1j
print(x)
print(y)
print(z)
print(type(x))
print(type(y))
print(type(z))

# 4


print(random.randrange(1, 100))

# 5

a = "Hello"

print(a)
print(type(a))

# 6

b = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(b)

i = 5
j = 10

print(i + j)
print(i - j)
print(i * j)
print(i % j)
print(i / j)

aa, ab, ac = "Orange", "Banana", "Cherry"
print(aa)
print(ab)
print(ac)

aaa = "awesome"


def myfunc():
    print("Python is " + aaa)


myfunc()
