def diffnum_sum(one, two, three):
    res = one + three + two
    print("Result is", res)

def all_same(one, two, three):
    res = one * two * three
    print("Result is", res)

def onetwo_same(one, two, three):
    res = (one * two) + three
    print("Result is", res)

def onethree_same(one, two, three):
    res = (one * three) + two
    print("Result is", res)

def twothree_same(one, two, three):
    res = (two * three) + one
    print("Result is", res)

one = int(input("Enter first number:"))
two = int(input("Enter second number:"))
three = int(input("Enter third number:"))

if one == two == three:
    all_same(one, two, three)

elif one == two:
    onetwo_same(one, two, three)

elif one == three:
    onethree_same(one, two, three)

elif two == three:
    twothree_same(one, two, three)

else:
    diffnum_sum(one, two, three)