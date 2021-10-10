# Matrices

At school I got bored of calculating matrices so I decided to create a script for it.

- [Matrices](#matrices)
  - [Prerequisites](#prerequisites)
  - [Examples](#examples)
  - [What's to come](#whats-to-come)
  - [Author](#author)
  - [License](#license)

## Prerequisites

Requirements are Python3+.

## Examples

- [Create a Matrix](#create-a-matrix)
- [Transpose a Matrix](#transpose-a-matrix)
- [Adding matrices](#adding-matrices)
- [Subtracting matrices](#subtracting-matrices)
- [Multiplying a Matrix by another Matrix](#multiplying-a-matrix-by-another-matrix)
- [Multiplying a Matrix by an integer](#multiplying-a-matrix-by-an-integer)
- [Get a nicer Matrix](#get-a-nicer-matrix)

### **Create a Matrix**

Create a matrix by specifying the number of rows and columns, and passing it a list containing the elements of the Matrix.

```python
>>> from matrix import Matrix
>>> exampleMatrix = Matrix(nrows=3, ncols=4, elements=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
>>> print(exampleMatrix)
1 2 3 4
5 6 7 8
9 10 11 12
```

### **Transpose a Matrix**

Transpose a Matrix by using `.transpose()`. This means the rows become the columns and vice versa.

```python
>>> from matrix import Matrix
>>> exampleMatrix = Matrix(nrows=3, ncols=4, elements=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
>>> print(exampleMatrix) # before .transpose()
1 2 3 4
5 6 7 8
9 10 11 12
>>> exampleMatrix.transpose()
>>> print(exampleMatrix) # after .transpose()
1 5 9
2 6 10
3 7 11
4 8 12
```

### **Adding matrices**

You can add two matrices together using `.add()` or by using the `+` operator.

```python
>>> from matrix import Matrix
>>> a = Matrix(nrows=3, ncols=4, elements=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
>>> b = Matrix(nrows=3, ncols=4, elements=[12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1])
>>> a.add(b) # Using .add()
>>> print(a)
13 13 13 13
13 13 13 13
13 13 13 13
>>> a + b # Using the + operator
25 24 23 22
21 20 19 18
17 16 15 14
```

### **Subtracting matrices**

You can subtract a Matrix from another Matrix using `.subtract()` or by using the `-` operator.

```python
>>> from matrix import Matrix
>>> a = Matrix(nrows=3, ncols=4, elements=[24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13])
>>> b = Matrix(nrows=3, ncols=4, elements=[12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1])
>>> a.subtract(b) # Using .subtract()
>>> print(a)
12 12 12 12
12 12 12 12
12 12 12 12
>>> a - b # Using the - operator
0 1 2 3
4 5 6 7
8 9 10 11
```

### **Multiplying a Matrix by another Matrix**

You can multiply a Matrix by another Matrix using `.multiply()` or by using the `*` operator. This also supports printing the steps. (Note that the code follows the rules for multiplying matrices.)

```python
>>> from matrix import Matrix
>>> a = Matrix(nrows=3, ncols=4, elements=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
>>> b = Matrix(nrows=4, ncols=3, elements=[12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1])
>>> a.multiply(b, show_steps=True) # Using .multiply(), show_steps is optional
1 2 3 4
5 6 7 8
9 10 11 12

12 11 10
9 8 7
6 5 4
3 2 1

--------------------------------------------------
60 50 40
180 154 128
300 258 216
>>> b * a # Using the * operator
5700 4874 4048
4080 3488 2896
2460 2102 1744
840 716 592
```

### **Multiplying a Matrix by an integer**

You can multiply a Matrix by an integer using `.multiply()` or by using the `*` operator. This also supports printing the steps.

```python
>>> from matrix import Matrix
>>> a = Matrix(nrows=3, ncols=4, elements=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
>>> a.multiply(3, show_steps=True) # Using .multiply(), show_steps is optional
1 2 3 4
5 6 7 8
9 10 11 12

3
--------------------------------------------------
3 6 9 12
15 18 21 24
27 30 33 36
>>> a * 3 # Using the * operator
9 18 27 36
45 54 63 72
81 90 99 108
```

### **Raising a Matrix to a power**

Raise a Matrix to any power using `.power()`. This also supports showing steps.

```python
>>> from matrix import Matrix
>>> a = Matrix(nrows=3, ncols=3, elements=[1, 2, 3, 4, 5, 6, 7, 8, 9])
>>> a.power(2, show_steps=False) # show_steps is optional
>>> print(a)
30 36 42
66 81 96
102 126 150
```

### **Get a nicer Matrix**

Get a nicer printable version of the Matrix using `.beautify()`.

```python
>>> from matrix import Matrix
>>> a = Matrix(nrows=3, ncols=3, elements=[1, 2, 3, 4, 5, 6, 7, 8, 9])
>>> nicerMatrix = a.beautify()
>>> print(nicerMatrix)
┌──   ──┐
│ 1 2 3 │
│ 4 5 6 │
│ 7 8 9 │
└──   ──┘
```

## What's to come

I would like to add more functionality to this script, starting by being able to do division.

## Author

- [**David Eitan Lesman**](https://github.com/dark-dave007)

## License

This project is licensed under the [MIT License](license.md)
