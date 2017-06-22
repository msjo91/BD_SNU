# ARITHMETIC OPERATORS
print("ARITHMETIC OPERATORS\n")
a = 10
b = 5
c = 3
# addition
print("addition(+): {a} + {b} == {add}".format(a=a, b=b, add=a + b))
# substraction
print("substractiona(-): {a} - {b} == {sub}".format(a=a, b=b, sub=a - b))
# multiplication
print("multiplication(*): {a} * {b} == {mul}".format(a=a, b=b, mul=a * b))
# division
print("divistion(/): {a} / {b} == {div}".format(a=a, b=b, div=a / b))
# modulus
print("modulus(%): {a} % {c} == {mod}".format(a=a, c=c, mod=a % c))
# exponent
print("exponent(**): {a} ** {c} == {exp}".format(a=a, c=c, exp=a ** c))
# floor division
print("floor division(//): {a} // {c} == {flo}\n\n".format(a=a, c=c, flo=a // c))

# ASSIGMENT OPERATORS
print("ASSIGNMENT OPERATORS\n")
# add AND
print("add AND(+=): (a += b) == (a = a + b)")
# subtract AND
print("subtract AND(-=): (a -= b) == (a = a - b)")
# multiply AND
print("multiply AND(*-): (a *= b) == (a = a * b)")
# divide AND
print("divide AND(/=): (a /= b) == (a = a / b)")
# modulus AND
print("modulus AND(%=): (a %= b) == (a = a % b)")
# exponent AND
print("exponent AND(**=): (a **= b) == (a = a ** b)")
# floor division AND
print("floor division AND(//=): (a //= b) == (a = a // b)\n\n")

# STRING ALGEBRA?
print("STRING ALBEGRA?\n")
# concatenation
print("concatenation(+): 'a' + 'b' == {}".format('a' + 'b'))
# repetition
print("repetition(*): 'a' * 3 == {}".format("a" * 3))
# string comparision
print("string comparision: 'a' > 'b' == {}".format('a' > 'b'))
print("string comparision: 'ab' > 'b' == {}".format('ab' > 'b'))
print("string comparision: 'ab' > 'a' == {}\n\n".format('ab' > 'a'))

# BOOLEAN ALGEBRA
print("BOOLEAN ALGEBRA")
# note
print("""
note:
Logical operators use and return boolean values (T and F).
0 and anything empty(string, list, etc.) are always False.\n
""")
# AND
print("""
Only True if everything is True:
'a' and 'b' is True
0 and 1 is False
""")
# OR
print("""
True if even one is true:
'a' or '' is True
[] or {} is False
""")
# distribution
print("""
Both AND and OR are distributive:
a or (b and c) == (a or b) and (a or c)
a and (b or c) == (a and b) or (a and c)
""")
# double negatives
print(""""
Double negatives cancel out:
not(not a) == a
""")
# DeMorgan's laws
print(""""
DeMorgan's laws:
not(a or b) == (not a) and (not b)
not(a and b) == (not a) or (not b)\n\n
""")

# SET OPERATIONS
print("SET OPERATIONS\n")
s1 = {1, 2, 3, 4}
s2 = {3, 4, 5, 6}
# intersection
print("intersection(&): {s1} & {s2} == {int}".format(s1=s1, s2=s2, int=s1 & s2))
# union
print("union(|): {s1} | {s2} == {uni}".format(s1=s1, s2=s2, uni=s1 | s2))
# difference
print("difference(-): {s1} - {s2} == {dif}".format(s1=s1, s2=s2, dif=s1 - s2))
