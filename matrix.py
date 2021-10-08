import copy
from typing import Union


class Matrix:
    def __init__(self, nrows: int, ncols: int, elements: list = None) -> None:
        """Creates a Matrix object.

        Args:
            nrows (int): The number of rows in the Matrix.
            ncols (int): The number of columns in the Matrix.
            elements (list, optional): A list containing the elements of the matrix. Defaults to None.

        Example:
        >>> a = Matrix(3, 4, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
        >>> print(a)
        1 2 3 4
        5 6 7 8
        9 10 11 12
        """
        self.nrows = nrows
        self.ncols = ncols
        self.elements = elements
        self.index = 0
        self.matrix = []
        if elements is not None:
            for _ in range(self.nrows):
                self.row = []
                for _ in range(self.ncols):
                    self.row.append(elements[self.index])
                    self.index += 1
                self.matrix.append(self.row)

    def __str__(self) -> str:
        string_form = ""
        for i in range(self.nrows):
            for j in range(self.ncols):
                string_form += str(self.matrix[i][j]) + " "
            string_form += "\n"

        return string_form

    def __deepcopy__(self) -> "Matrix":
        """Deepcopies the matrixs contents.

        Returns:
            Matrix: A deepcopy of the matrix.
        """
        return Matrix(copy.deepcopy(list(self)))

    def __add__(self, other: "Matrix") -> "Matrix":
        if self.nrows != other.nrows or self.ncols != other.ncols:
            raise ValueError("Matrices should be the same size")

        returnMatrix = Matrix(self.nrows, self.ncols, self.elements)
        returnMatrix.add(other)

        return returnMatrix

    def __sub__(self, other: "Matrix") -> "Matrix":
        if self.nrows != other.nrows or self.ncols != other.ncols:
            raise ValueError("Matrices should be the same size")

        returnMatrix = Matrix(self.nrows, self.ncols, self.elements)
        returnMatrix.subtract(other)

        return returnMatrix

    def __mul__(self, other: "Matrix") -> "Matrix":
        returnMatrix = Matrix(self.nrows, self.ncols)
        returnMatrix.matrix = self.matrix
        returnMatrix.multiply(other)

        return returnMatrix

    def transpose(self) -> None:
        self.backup = copy.deepcopy(self.matrix)
        self.matrix = []
        self.elements = []

        # Append all columns instead of rows to transpose. Update elements list.
        for i in range(self.ncols):
            self.row = []
            self.index = 0
            for j in range(self.nrows):
                if (i + j) < self.nrows:
                    newElement = self.backup[self.index][i]
                    self.row.append(newElement)
                    self.elements.append(newElement)
                else:  # This means we reached the last column
                    newElement = self.backup[j][i]
                    self.row.append(newElement)
                    self.elements.append(newElement)
                self.index += 1
            self.matrix.append(self.row)

        self.nrows = len(self.matrix)
        # need number of columns, so I used the first row
        self.ncols = len(self.matrix[0])

    def add(self, other: "Matrix") -> None:
        """Add another Matrix to this Matrix.

        Args:
            other (Matrix): The Matrix to add.
        """
        if self.nrows != other.nrows or self.ncols != other.ncols:
            raise ValueError("Matrices should be the same size")

        self.elements = []
        for i in range(self.nrows):
            for j in range(self.ncols):
                newElement = self.matrix[i][j] + other.matrix[i][j]
                self.matrix[i][j] = newElement
                self.elements.append(newElement)

    def subtract(self, other: "Matrix") -> None:
        """Subtract another Matrix from this Matrix.

        Args:
            other (Matrix): The Matrix to subtract.
        """
        if self.nrows != other.nrows or self.ncols != other.ncols:
            raise ValueError("Matrices should be the same size")

        self.elements = []
        for i in range(self.nrows):
            for j in range(self.ncols):
                newElement = self.matrix[i][j] - other.matrix[i][j]
                self.matrix[i][j] = newElement
                self.elements.append(newElement)

    def multiply(self, other: Union["Matrix", int]) -> None:
        """Multiply a Matrix or an integer with this Matrix.

        Args:
            other (Matrix | int): The Matrix or integer to multiply by.
        """
        if type(other) == int:
            self.elements = []
            for i in range(self.nrows):
                for j in range(self.ncols):
                    newElement = self.matrix[i][j] * other
                    self.matrix[i][j] = newElement
                    self.elements.append(newElement)
            return

        if self.ncols != other.nrows:
            raise ValueError(
                "The number of columns of the 1st Matrix must equal the number of rows of the 2nd Matrix."
            )

        self.elements = []
        self.backup = copy.deepcopy(self.matrix)
        self.matrix = []
        for i in range(self.nrows):
            newRow = []
            for j in range(other.ncols):
                dotProduct = 0
                for k in range(other.nrows):
                    dotProduct += self.backup[i][k] * other.matrix[k][j]
                newRow.append(dotProduct)
                self.elements.append(dotProduct)
            self.matrix.append(newRow)
        self.ncols = other.ncols

    def beautify(self) -> str:
        # TODO: Make ascii art of matrix when i feel like it
        pass


a = Matrix(3, 4, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
print(a)
print("Transposing A")
a.transpose()
print(a)

b = Matrix(4, 3, [2, 34, 53, 13, 7, 4, 41, 13, 98, 5, 8, 19])
print("B")
print(b)

a.add(b)
print("A = A  + B")
print(a)

d = b - a
print("D = B - A")
print(d)

c = a - b
print("C = A - B")
print(c)
c.transpose()

a -= b
a.multiply(3)
print(a)

d = a * c
print(d)

print(a)
print(c)
a.multiply(c)
print(a)
print(f"a: {a.nrows}x{a.ncols}")
print(a.elements)
