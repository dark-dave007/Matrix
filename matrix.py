import copy


class Matrix:
    def __init__(self, nrows: int, ncols: int, elements: list) -> None:
        self.nrows = nrows
        self.ncols = ncols
        self.elements = elements
        self.index = 0
        self.matrix = []
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
        returnMatrix.elements = []
        for i in range(self.nrows):
            for j in range(self.ncols):
                newElement = returnMatrix.matrix[i][j] + other.matrix[i][j]
                returnMatrix.matrix[i][j] = newElement
                returnMatrix.elements.append(newElement)

        return returnMatrix

    def __sub__(self, other: "Matrix") -> "Matrix":
        if self.nrows != other.nrows or self.ncols != other.ncols:
            raise ValueError("Matrices should be the same size")

        returnMatrix = Matrix(self.nrows, self.ncols, self.elements)
        returnMatrix.elements = []
        for i in range(self.nrows):
            for j in range(self.ncols):
                newElement = returnMatrix.matrix[i][j] - other.matrix[i][j]
                returnMatrix.matrix[i][j] = newElement
                returnMatrix.elements.append(newElement)

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

    def multiply(self):
        """Multiply another Matrix with this Matrix.

        Args:
            other (Matrix): The Matrix to multiply by.
        """
        # TODO: multiply with an integer or another matrix
        pass

    def beautify(self):
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

c = a + b
print("C = A  + B")
print(c)

d = b - a
print("D = B - A")
print(d)

a.subtract(b)
print("A = A - B")
print(a)
