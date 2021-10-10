from matrix import Matrix

a = Matrix(3, 4, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
b = Matrix(4, 3, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
print(a)
print(b)

c = a * b
print(c)

print("Transposing A")
a.transpose()
print(a)

a.multiply(3, 3, 3, 3, show_steps=True)

d = Matrix(nrows=3, ncols=3, elements=[1, 2, 3, 4, 5, 6, 7, 8, 9])
e = Matrix(3, 3, [12, 11, 10, 130, 10, 9, 3, 87, 12])

d.power(4, show_steps=True)
print(d.beautify())

f = d * e
f.beautify()
