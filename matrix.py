import copy
from typing import Union


class Matrix:
    def __init__(self, nrows: int, ncols: int, elements: list) -> None:
        """Creates a Matrix object.

        Args:
            nrows (int): The number of rows in the Matrix.
            ncols (int): The number of columns in the Matrix.
            elements (list): A list containing the elements of the Matrix.

        Example:
        >>> a = Matrix(nrows=3, ncols=4, elements=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
        >>> print(a)
        1 2 3 4
        5 6 7 8
        9 10 11 12

        Documentation: https://www.github.com/dark-dave007/Matrix/readme.md
        """
        if len(elements) != nrows * ncols:
            raise ValueError(
                f"Elements must be able to fit inside the Matrix. \nElements supported in this Matrix: {nrows * ncols}\nElements given: {len(elements)}"
            )
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

    def __repr__(self) -> str:
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

    def __mul__(self, other: Union["Matrix", int, float]) -> "Matrix":
        returnMatrix = Matrix(self.nrows, self.ncols, self.elements)
        returnMatrix.multiply(other)

        return returnMatrix

    def transpose(self) -> None:
        """Transpose the matrix. (columns become the rows and vice versa)."""
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
            raise ValueError("Matrices should be the same size.")

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

    def multiply(
        self, *other: Union["Matrix", int, float], show_steps: bool = False
    ) -> None:
        """Multiply a Matrix or an integer with this Matrix.

        Args:
            other (Matrix | int): The Matrix or integer to multiply by.
            show_steps (bool, optional): It will print out the steps of the multiplication. Defaults to False.
        """
        # TODO: Fix show_steps to make it more clear what is going on
        self.index = 1
        for otherElement in other:
            oldMatrix = Matrix(self.nrows, self.ncols, self.elements)
            self.elements = []

            if type(otherElement) == int or type(otherElement) == float:
                for i in range(self.nrows):
                    for j in range(self.ncols):
                        newElement = self.matrix[i][j] * otherElement
                        self.matrix[i][j] = newElement
                        self.elements.append(newElement)

                if show_steps:
                    if len(other) == 1:
                        print(oldMatrix)
                        print(otherElement)
                        print(50 * "-")
                        print(self)
                    elif self.index == 1:
                        print(oldMatrix)
                        print(otherElement)
                        print(50 * "-")
                    elif self.index == len(other):
                        print(self)
                    else:
                        print(self)
                        print(otherElement)
                        print(50 * "-")
                    self.index += 1

                continue

            if self.ncols != otherElement.nrows:
                raise ValueError(
                    "The number of columns of the 1st Matrix must equal the number of rows of the 2nd Matrix."
                )

            self.backup = copy.deepcopy(self.matrix)
            self.matrix = []
            for i in range(self.nrows):
                newRow = []
                for j in range(otherElement.ncols):
                    dotProduct = 0
                    for k in range(otherElement.nrows):
                        dotProduct += self.backup[i][k] * otherElement.matrix[k][j]
                    newRow.append(dotProduct)
                    self.elements.append(dotProduct)
                self.matrix.append(newRow)
            self.ncols = otherElement.ncols

            if show_steps:
                if len(other) == 1:
                    print(oldMatrix)
                    print(otherElement)
                    print(50 * "-")
                    print(self)
                elif self.index == 1:
                    print(oldMatrix)
                    print(otherElement)
                    print(50 * "-")
                elif self.index == len(other):
                    print(self)
                else:
                    print(self)
                    print(otherElement)
                    print(50 * "-")
                self.index += 1

    def power(self, powerOf: int, show_steps: bool = False) -> None:
        """Raise the Matrix to an exponent.

        Args:
            powerOf (int): The exponent to which to raise the Matrix.
            show_steps (bool, optional): It will print out the steps of the multiplication. Defaults to False.
        """
        if self.nrows != self.ncols:
            raise ValueError(
                "Matrix needs to be a square Matrix (Matrix with equal amount of rows and columns)."
            )

        originalMatrix = Matrix(self.nrows, self.ncols, self.elements)
        show = False
        if show_steps:
            show = True
        for x in range(1, powerOf):
            self.multiply(originalMatrix, show_steps=show)
            if show_steps and x < powerOf - 1:
                print(
                    """
  :::::
  :::::
  :::::
  :::::
  :::::
  :::::
  :::::
..:::::..
 ':::::'
   ':'
                """
                )

    def beautify(self) -> str:
        """Create a better version of the Matrix.

        Returns:
            str: The Matrix, but nicer :D.
        """
        longestNum = 0
        for i in range(self.nrows):
            for j in range(self.ncols):
                if len(str(self.matrix[i][j])) > longestNum:
                    longestNum = len(str(self.matrix[i][j]))

        endspace = " " * longestNum
        longestLine = 0
        lines = []
        for i in range(self.nrows):
            line = "│" + endspace
            for j in range(self.ncols):
                space = " " * (longestNum - len(str(self.matrix[i][j])))
                line += space + str(self.matrix[i][j]) + endspace
            line += "│"
            lines.append(line)

            if len(line) > longestLine:
                longestLine = len(line)

        longestLine -= 6
        beautified = "┌──" + longestLine * " " + "──┐\n"
        for line in lines:
            beautified += line + "\n"
        beautified += "└──" + longestLine * " " + "──┘\n"

        return beautified
