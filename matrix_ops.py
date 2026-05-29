# =============================================================================
# Omega Calculator 10.0 - Module 4: Matrix Operations
# Author: Amirmahdi Ghorbani
# =============================================================================
# This module provides fundamental matrix algebra operations including:
#   - Matrix input parsing from string format
#   - Formatted matrix display with colored output
#   - Matrix addition (element-wise)
#   - Matrix multiplication (triple-loop algorithm)
#   - Determinant calculation (1×1, 2×2, 3×3 via closed-form formulas)
#   - Inverse matrix computation (2×2 only)
#
# The matrix data structure used throughout is list[list[float]]: a list
# of rows, where each row is a list of column values.
#
# Input Format:
#   Matrices are entered as strings in the format "1,2,3;4,5,6;7,8,9"
#   where semicolons (;) separate rows and commas (,) separate columns.
#
# Limitations:
#   - Determinant: Supports up to 3×3 matrices only
#   - Inverse: Supports 2×2 matrices only
#   These limitations are clearly communicated to users through error
#   messages displayed in the application's UI layer.
#
# Dependencies:
#   - color (local module): Terminal text coloring functions
#
# Last Modified: 2026-05-29
# Version: 10.0 (Modular Edition)
# =============================================================================

from color import *


class MatrixOperations:
    """
    Matrix algebra operations: addition, multiplication, determinant, inverse.

    All methods are static for direct access without instantiation. Matrices
    are represented as list[list[float]] (rows of columns). Input parsing
    from the application's standard string format is handled by the matrix()
    method, which converts semicolon/comma-separated strings to 2D lists.
    """

    @staticmethod
    def matrix(s):
        """
        Parses a string representation of a matrix into a 2D list of floats.

        The expected input format is:
            "a₁₁,a₁₂,...,a₁ₙ; a₂₁,a₂₂,...,a₂ₙ; ...; aₘ₁,aₘ₂,...,aₘₙ"

        where:
            - Semicolons (;) separate rows
            - Commas (,) separate columns within each row
            - All values are converted to float

        This format allows users to easily enter matrices in a natural
        row-by-row format without needing to understand Python's list
        syntax.

        Args:
            s (str): String representation of the matrix in the format
                    "row1col1,row1col2;row2col1,row2col2;..."

        Returns:
            list[list[float]]: A 2D list where:
                - The outer list represents rows (index i)
                - Each inner list represents columns within that row (index j)
                - Individual elements are accessed as result[i][j]

        Raises:
            ValueError: If any cell contains a non-numeric value (e.g.,
                       letters, empty cells, or malformed numbers).

        Example:
            >>> MatrixOperations.matrix("1,2,3;4,5,6")
            [[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]]
            >>> MatrixOperations.matrix("1.5,2.5;3.5,4.5")
            [[1.5, 2.5], [3.5, 4.5]]
        """
        # Split the input string on semicolons to separate rows.
        # strip() removes any leading/trailing whitespace.
        rows = s.strip().split(";")

        # Initialize the result matrix as an empty list
        matrix = []

        # Process each row: split on commas and convert each cell to float.
        # This two-level parsing (first by ;, then by ,) creates the 2D
        # list structure expected by all other matrix methods.
        for row in rows:
            nums = [float(x) for x in row.split(",")]
            matrix.append(nums)

        return matrix

    @staticmethod
    def print_matrix(mat):
        """
        Prints a matrix to the console with formatted alignment and coloring.

        Each element is displayed with exactly 8 characters of width and
        2 decimal places (format specifier: {val:8.2f}). The matrix is
        displayed row by row with square brackets and purple coloring
        applied via the color module's purple() function.

        This method is used for displaying results of matrix operations
        in a visually clear and organized manner.

        Args:
            mat (list[list[float]]): The matrix to display. Can be of any
                                    dimensions.

        Example Output:
            [    1.00     2.00     3.00 ]
            [    4.00     5.00     6.00 ]
            [    7.00     8.00     9.00 ]

        Note:
            The purple() function from the color module adds ANSI escape
            codes for terminal coloring. The end="" parameter keeps output
            on the same line until the row is complete.
        """
        for row in mat:
            # Print opening bracket for this row
            purple("  [", end="")

            # Print each element with consistent 8-character width and
            # 2 decimal places. A space is printed before each element
            # except the first in each row for visual separation.
            for i, val in enumerate(row):
                if i > 0:
                    purple(" ", end="")
                purple(f"{val:8.2f}", end="")

            # Close the bracket and move to the next line
            purple(" ]")

    @staticmethod
    def matrix_add(A, B):
        """
        Adds two matrices of identical dimensions element-wise.

        Matrix addition is defined only for matrices of the same size.
        If A and B are both m × n matrices, their sum C = A + B is also
        an m × n matrix where:
            C[i][j] = A[i][j] + B[i][j]

        Time Complexity: O(m × n) where m = number of rows, n = number of columns
        Space Complexity: O(m × n) for the result matrix

        Args:
            A (list[list[float]]): First matrix (m rows × n columns).
            B (list[list[float]]): Second matrix (m rows × n columns).
                                  Must have exactly the same dimensions as A.

        Returns:
            list[list[float]]: The sum matrix C = A + B, with the same
                              dimensions as the inputs.

        Raises:
            ValueError: If the matrices have different dimensions (different
                       number of rows or different number of columns).
                       The error message is in Persian: "ماتریس‌ها هم‌اندازه
                       نیستند!" which means "Matrices are not the same size!"

        Example:
            >>> A = [[1, 2], [3, 4]]
            >>> B = [[5, 6], [7, 8]]
            >>> MatrixOperations.matrix_add(A, B)
            [[6, 8], [10, 12]]
            >>> # Visual verification:
            >>> # [1 2]   [5 6]   [1+5  2+6]   [6  8]
            >>> # [3 4] + [7 8] = [3+7  4+8] = [10 12]
        """
        # Validate that both matrices have the same dimensions.
        # len(A) returns the number of rows in A.
        # len(A[0]) returns the number of columns (assuming rectangular).
        # Both must match for addition to be defined.
        if len(A) != len(B) or len(A[0]) != len(B[0]):
            raise ValueError("ماتریس‌ها هم‌اندازه نیستند!")

        # Perform element-wise addition by iterating through all positions.
        # This creates a new matrix rather than modifying either input,
        # preserving the original matrices.
        result = []
        for i in range(len(A)):
            row = []
            for j in range(len(A[0])):
                row.append(A[i][j] + B[i][j])
            result.append(row)

        return result

    @staticmethod
    def matrix_multiply(A, B):
        """
        Multiplies two matrices: computes C = A × B.

        Matrix multiplication is defined only when the number of columns
        in A equals the number of rows in B. If A is m×n and B is n×p,
        the product C = AB will be m×p.

        The element C[i][j] is computed as the dot product of the i-th
        row of A with the j-th column of B:
            C[i][j] = Σ(k=1 to n) A[i][k] × B[k][j]

        This implementation uses the straightforward triple-loop algorithm
        with O(m × n × p) time complexity. For the matrix sizes used in
        this calculator (typically small, educational examples), this
        performance is more than adequate.

        Time Complexity: O(m × n × p) for m×n and n×p matrices
        Space Complexity: O(m × p) for the result matrix

        Args:
            A (list[list[float]]): First matrix with dimensions m × n.
            B (list[list[float]]): Second matrix with dimensions n × p.
                                  The number of rows in B must equal the
                                  number of columns in A.

        Returns:
            list[list[float]]: The product matrix C = AB with dimensions
                              m × p.

        Raises:
            ValueError: If the inner dimensions do not match (cols_A ≠
                       rows_B). The error message is in Persian: "تعداد
                       ستون‌های A باید برابر تعداد سطرهای B باشد!" which
                       means "The number of columns in A must equal the
                       number of rows in B!"

        Example:
            >>> A = [[1, 2, 3], [4, 5, 6]]     # 2×3 matrix
            >>> B = [[7, 8], [9, 10], [11, 12]] # 3×2 matrix
            >>> MatrixOperations.matrix_multiply(A, B)
            [[58, 64], [139, 154]]              # 2×2 result
            >>>
            >>> # Verification of C[0][0]:
            >>> # 1×7 + 2×9 + 3×11 = 7 + 18 + 33 = 58 ✓
            >>> # Verification of C[0][1]:
            >>> # 1×8 + 2×10 + 3×12 = 8 + 20 + 36 = 64 ✓
        """
        # Extract dimensions for clarity and validation
        rows_A = len(A)       # Number of rows in matrix A (m)
        cols_A = len(A[0])    # Number of columns in matrix A (n)
        rows_B = len(B)       # Number of rows in matrix B (must equal n)
        cols_B = len(B[0])    # Number of columns in matrix B (p)

        # Validate that the inner dimensions are compatible.
        # Matrix multiplication A×B requires: columns of A = rows of B.
        if cols_A != rows_B:
            raise ValueError("تعداد ستون‌های A باید برابر تعداد سطرهای B باشد!")

        # Initialize the result matrix with zeros.
        # Dimensions: m × p (rows_A × cols_B).
        # Each element is initialized to 0 and accumulated through the
        # summation loop.
        result = [[0 for _ in range(cols_B)] for _ in range(rows_A)]

        # Perform the multiplication using the standard triple-loop algorithm.
        # - Outer loop (i): iterates over rows of A (and result)
        # - Middle loop (j): iterates over columns of B (and result)
        # - Inner loop (k): summation index over columns of A / rows of B
        for i in range(rows_A):
            for j in range(cols_B):
                for k in range(cols_A):
                    result[i][j] += A[i][k] * B[k][j]

        return result

    @staticmethod
    def determinant(mat):
        """
        Computes the determinant of a square matrix.

        Supports 1×1, 2×2, and 3×3 matrices using closed-form formulas.
        For larger matrices, a ValueError is raised as they are not
        currently supported by this calculator.

        Formulas Used:
            1×1 matrix [a]:
                det = a

            2×2 matrix [[a, b], [c, d]]:
                det = ad - bc
                (The area scaling factor of the linear transformation)

            3×3 matrix [[a,b,c], [d,e,f], [g,h,i]]:
                det = a(ei - fh) - b(di - fg) + c(dh - eg)
                (Laplace expansion along the first row)

        Args:
            mat (list[list[float]]): A square matrix of size n×n where
                                    1 ≤ n ≤ 3.

        Returns:
            float: The determinant of the matrix. For invertible matrices,
                  det ≠ 0. For singular matrices, det = 0.

        Raises:
            ValueError: If the matrix has more than 3 rows/columns.
                       The error message is in Persian: "فعلاً فقط تا
                       ۳×۳ پشتیبانی می‌شود!" which means "Currently only
                       up to 3×3 is supported!"

        Example:
            >>> MatrixOperations.determinant([[1, 2], [3, 4]])
            -2.0
            >>> MatrixOperations.determinant([[2]])
            2.0
            >>> MatrixOperations.determinant([[1,0,0],[0,1,0],[0,0,1]])
            1.0  # Identity matrix has determinant 1
        """
        n = len(mat)

        # 1×1 matrix: The determinant is simply the single element.
        # This is the base case of the recursive determinant definition.
        if n == 1:
            return mat[0][0]

        # 2×2 matrix: Use the direct formula ad - bc.
        # This is the simplest non-trivial case and appears frequently
        # in applications (2D transformations, 2×2 systems, etc.)
        if n == 2:
            return mat[0][0] * mat[1][1] - mat[0][1] * mat[1][0]

        # 3×3 matrix: Use Laplace expansion along the first row.
        # Extract elements with descriptive names for readability.
        # The formula:
        #   det = a₁₁·det(M₁₁) - a₁₂·det(M₁₂) + a₁₃·det(M₁₃)
        # where Mᵢⱼ is the 2×2 minor matrix obtained by deleting row i
        # and column j from the original 3×3 matrix.
        if n == 3:
            # Extract the nine elements for clear reference
            a, b, c = mat[0]  # First row
            d, e, f = mat[1]  # Second row
            g, h, i = mat[2]  # Third row

            # Compute using the Sarrus-like expanded formula:
            # a(ei - fh) - b(di - fg) + c(dh - eg)
            #
            # Where:
            #   (ei - fh) is the determinant of the minor M₁₁ (remove row 1, col 1)
            #   (di - fg) is the determinant of the minor M₁₂ (remove row 1, col 2)
            #   (dh - eg) is the determinant of the minor M₁₃ (remove row 1, col 3)
            return a * (e * i - f * h) - b * (d * i - f * g) + c * (d * h - e * g)

        # Matrices larger than 3×3 are not currently supported.
        # The error message is in Persian to match the application's
        # bilingual interface design.
        raise ValueError("فعلاً فقط تا ۳×۳ پشتیبانی می‌شود!")

    @staticmethod
    def inverse_2x2(mat):
        """
        Computes the inverse of a 2×2 matrix.

        For a non-singular 2×2 matrix:
            A = [[a, b], [c, d]]

        The inverse is given by:
            A⁻¹ = (1/det) × [[d, -b], [-c, a]]

        where det = ad - bc is the determinant. The inverse exists if
        and only if det ≠ 0 (the matrix is non-singular/invertible).

        This formula can be verified by direct multiplication:
            A × A⁻¹ = [[a,b],[c,d]] × (1/det)[[d,-b],[-c,a]]
                    = (1/det)[[ad-bc, -ab+ba], [cd-dc, -bc+ad]]
                    = [[1, 0], [0, 1]] = I

        Args:
            mat (list[list[float]]): A 2×2 matrix [[a, b], [c, d]].

        Returns:
            list[list[float]]: The inverse matrix A⁻¹, also 2×2.

        Raises:
            ValueError: If the determinant is zero (singular matrix).
                       The error message is in Persian: "ماتریس معکوس
                       ندارد!" which means "Matrix has no inverse!"

        Example:
            >>> A = [[1, 2], [3, 4]]
            >>> inv_A = MatrixOperations.inverse_2x2(A)
            >>> inv_A
            [[-2.0, 1.0], [1.5, -0.5]]
            >>>
            >>> # Verify: A × A⁻¹ should equal identity
            >>> MatrixOperations.matrix_multiply(A, inv_A)
            [[1.0, 0.0], [0.0, 1.0]]  # ✓ Identity matrix
        """
        # Extract the four elements for the formula
        a, b = mat[0]  # First row
        c, d = mat[1]  # Second row

        # Compute the determinant: det = ad - bc
        # If det = 0, the matrix is singular (non-invertible).
        # Geometrically, this means the linear transformation collapses
        # the plane into a line or point, so no inverse exists.
        det = a * d - b * c

        if det == 0:
            raise ValueError("ماتریس معکوس ندارد!")

        # Construct and return the inverse using the 2×2 formula.
        # Each element is divided by the determinant.
        # The pattern: swap a and d, negate b and c.
        return [[d / det, -b / det], [-c / det, a / det]]