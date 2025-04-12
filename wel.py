letter = " hello and welcome"
message = """hello and welcome
hello and welcome
hello and welcome"""

letter = " hello and welcome"
message = "good morning"
print(letter + message)
print(letter * 5)
print(len(letter))

letter = "hello and welcome"
print(letter[0])
print(letter[-1])

letter = "hello and welcome"
print(letter[0:8])

name = "kishor"
print(f"hello Mr.{name}")
reversedname = name[::-1]
print(f"reversedname is {reversedname}")
print(f"length of name is {len(name)}")

name = "kishor"
upp = name. upper()
print(upp)
low = name. lower()
print(low)
cap = name. capitalize()
print(cap)
title = name. title()
print(title)

name = "kishor kumar"
print(name. strip ())
print(name. count ("r"))
print("kumar" in name)

age = 18
if age >= 18:
    print(f"your age is{age} so eligible to vote")
age = 17
if age >= 17:
    print(f"your age is {age} so not eligible to vote")

mark = 95
if mark >= 90:
    print("A")
elif mark >= 80:
    print("B")
elif mark >= 70:
    print("C")
elif mark >= 60:
     print("D")
else:
    print("F") 


a = 15
b = 20
larger = a if a > b else b
print(f"the larger number is {larger}")

colors = ["red", "blue", "yellow", "green"]
print(colors)

mixedlist = ["red",1,3.24,"true"]
print(mixedlist)

number = [1,2,3,4,5,[6,7,8,9]]
print(number)
print(len(colors))
print(colors[0])
print(colors[-1])
print(colors[1:3])
print(colors[1:])
print("orange" in colors)
listreverse = colors[::-1]
print(listreverse)

colors[1] = "white"
print(colors)
colors.append("brown")
print(colors)
moreItems = ["banana", "apple"]
colors.extend(moreItems)
print(colors)
print(colors.index("red"))
print(colors.count("purple"))
print(colors.pop())
print(colors)
print(colors.pop(2))

  #tuple
tuple1 = (1, 2, 3, 4)
tuple2 = ("a", "b", "c")
print(tuple1 + tuple2)
print(tuple1 * 4)

numbers = (0, 1, 2, 3, 4, 5)
subset = numbers[2:7]
print(subset)

reversedtuple = numbers[::-1]
print(reversedtuple)
print(min(numbers))
print(max(numbers))

repeattuple = (1,2,2,3,3)
print(repeattuple.count(3))

person = ("John Doe", 30, "software")
name, age, profession = person
print(name)
print(age)
print(profession)

a, b = 10, 20
print(f"before swap: a = {a}, b = {b}")
a, b = b, a
print(f"after swap: a = {a}, b = {b}")



      
















































































tuple1 = (1, 2, 3)
tuple2 = ("a", "b", "c",)
print(tuple1 + tuple2)
print(tuple1 * 4)

                                                      