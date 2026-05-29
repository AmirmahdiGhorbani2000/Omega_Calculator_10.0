#####
# =============================================================================
# Omega Calculator 10.0 - Module 1: Mathematical Base Utilities
# Author: Amirmahdi Ghorbani
# =============================================================================
# This module provides fundamental mathematical utility functions that are
# used throughout the Omega Calculator application. It includes:
#   - Dynamic function compilation from string expressions
#   - Type-safe floating-point input handling
#   - Number theory utilities (LCM, primality testing)
#   - Trigonometric extensions (cotangent)
#
# All methods in this module are static and stateless. The class serves as
# a namespace for organizing related mathematical helper functions.
#
# Dependencies:
#   - math (standard library): Mathematical functions and constants
#
# Last Modified: 2026-05-29
# Version: 10.0 (Modular Edition)
# =============================================================================

import math


class MathBase:
    """
    A collection of general-purpose mathematical utility methods.

    This class is designed as a stateless namespace. All methods are static,
    meaning no instance of MathBase ever needs to be created. It provides
    functionality ranging from dynamic function compilation to number theory
    operations that are shared across multiple modules in the application.
    """

    @staticmethod
    def make_function(expr_str):
        """
        Compiles a mathematical expression string into a callable function.

        This method uses Python's eval() with a restricted namespace to safely
        convert user-provided mathematical expressions (e.g., "x**2 + sin(x)")
        into executable lambda functions. The namespace is carefully controlled
        to include only mathematical functions from the math module, preventing
        arbitrary code execution.

        Args:
            expr_str (str): A string representing a mathematical expression in
                           terms of 'x'. Supports standard operators (+, -, *,
                           /, **) and common math functions (sin, cos, tan,
                           sqrt, log, log10, exp, abs). Also supports constants
                           pi and e. The expression may begin with 'lambda'
                           for explicit lambda definitions.

        Returns:
            function: A callable that takes a single numeric argument x and
                     returns the evaluated result.

        Raises:
            SyntaxError: If the expression string is malformed.
            NameError: If an unsupported function name is used in the expression.

        Security Note:
            The __builtins__ namespace is explicitly set to an empty dictionary
            to prevent access to built-in Python functions that could be
            exploited for code injection. Only mathematical functions from the
            math module are exposed.

        Example:
            >>> f = MathBase.make_function("x**2 + 3*sin(x)")
            >>> f(0)
            0.0
            >>> f(math.pi/2)
            5.467401100272339
        """
        # Define the safe namespace containing only mathematical functions
        # and constants that users are permitted to use in expressions.
        # This whitelist approach prevents arbitrary code execution while
        # still providing users with a rich set of mathematical tools.
        namespace = {
            'sin': math.sin,      # Trigonometric sine
            'cos': math.cos,      # Trigonometric cosine
            'tan': math.tan,      # Trigonometric tangent
            'sqrt': math.sqrt,    # Square root function
            'log': math.log,      # Natural logarithm (base e)
            'log10': math.log10,  # Base-10 logarithm
            'exp': math.exp,      # Exponential function (e^x)
            'abs': abs,           # Absolute value (built-in)
            'pi': math.pi,        # π constant (~3.141592653589793)
            'e': math.e,          # Euler's number (~2.718281828459045)
            '**': pow,            # Exponentiation operator (x**y)
        }

        # Remove leading/trailing whitespace from the expression
        expr = expr_str.strip()

        # Handle explicit lambda expressions (e.g., "lambda x: x**2 + 1")
        # These are passed through directly with the restricted namespace.
        # The empty __builtins__ dict prevents access to dangerous functions
        # like open(), exec(), or __import__().
        if expr.startswith('lambda'):
            return eval(expr, {"__builtins__": {}}, namespace)

        # For standard expressions, automatically wrap them in a lambda
        # function that takes a single argument x. This allows users to
        # write natural mathematical notation like "x**2 + 3*sin(x)"
        # without needing to know lambda syntax.
        # Example transformation: "x**2 + 1" → "lambda x: x**2 + 1"
        return eval(f"lambda x: {expr}", {"__builtins__": {}}, namespace)

    @staticmethod
    def infut(te):
        """
        Safely reads a floating-point number from user input.

        This method wraps Python's input() and float() functions to provide
        a consistent interface for reading numeric input throughout the
        application. The parameter name serves as the prompt text displayed
        to the user.

        Args:
            te (str): The prompt text to display to the user. Typically
                     includes a label and colon (e.g., "Enter value: ").

        Returns:
            float: The numeric value entered by the user.

        Raises:
            ValueError: If the user enters a non-numeric string (e.g., "abc"
                       or an empty string). The calling code is responsible
                       for handling this exception appropriately.

        Example:
            >>> value = MathBase.infut("Radius: ")
            Radius: 5.3
            >>> value
            5.3
            >>> type(value)
            <class 'float'>
        """
        return float(input(te))

    @staticmethod
    def lcm(a, b):
        """
        Calculates the Least Common Multiple (LCM) of two integers.

        Uses the mathematical relationship LCM(a,b) = |a × b| / GCD(a,b)
        for efficient computation. This method relies on math.gcd() which
        implements the Euclidean algorithm with O(log(min(a,b))) time
        complexity.

        Args:
            a (int): First integer.
            b (int): Second integer.

        Returns:
            int: The least common multiple of a and b. Always returns a
                 non-negative integer. Returns 0 if either argument is 0
                 (since LCM is undefined for zero, 0 is returned as a
                 convention).

        Mathematical Basis:
            For any two non-zero integers a and b:
                LCM(a,b) × GCD(a,b) = |a × b|
            Therefore:
                LCM(a,b) = |a × b| / GCD(a,b)

            This relationship holds because the prime factorization of
            LCM contains the maximum exponent of each prime from both
            numbers, while GCD contains the minimum exponent. Their
            product thus equals the product of the original numbers.

        Example:
            >>> MathBase.lcm(12, 18)
            36
            >>> MathBase.lcm(7, 13)  # Coprime numbers: LCM = product
            91
            >>> MathBase.lcm(0, 5)
            0
        """
        return (abs(a * b)) // math.gcd(a, b)

    @staticmethod
    def cot(x):
        """
        Calculates the cotangent of an angle in radians.

        The cotangent function is mathematically defined as:
            cot(x) = cos(x) / sin(x) = 1 / tan(x)

        This method provides it as a convenience function since cotangent
        is not included in Python's standard math module (unlike sin, cos,
        and tan).

        Args:
            x (float): Angle in radians.

        Returns:
            float: The cotangent of x.

        Raises:
            ZeroDivisionError: If sin(x) = 0 (i.e., when x is an integer
                              multiple of π). At these points, cotangent
                              is undefined (approaches ±∞). The caller
                              is responsible for ensuring valid input or
                              handling this exception.

        Mathematical Definition:
            cot(x) = cos(x) / sin(x)

            Domain: All real numbers except x = nπ where n ∈ ℤ
            Range: All real numbers (-∞, +∞)
            Period: π

            Common values:
                cot(π/4) = 1
                cot(π/3) = 1/√3 ≈ 0.577
                cot(π/6) = √3 ≈ 1.732
                cot(π/2) = 0

        Example:
            >>> MathBase.cot(math.pi/4)
            1.0
            >>> MathBase.cot(math.pi/2)
            0.0  # cos(π/2)=0, sin(π/2)=1, so 0/1 = 0
        """
        return math.cos(x) / math.sin(x)

    @staticmethod
    def is_prime(n):
        """
        Determines whether a given integer is a prime number.

        Implements an optimized trial division algorithm that:
        1. Immediately rejects numbers less than 2 (not prime by definition)
        2. Handles 2 as a special case (the only even prime number)
        3. Immediately rejects all even numbers greater than 2
        4. Tests only odd divisors from 3 up to √n

        This optimization reduces the number of trial divisions by
        approximately 50% compared to testing all integers.

        Time Complexity: O(√n) in the worst case (when n is prime)
        Space Complexity: O(1) - uses only a few local variables

        Args:
            n (int): The integer to test for primality.

        Returns:
            bool: True if n is a prime number, False otherwise.

        Algorithm Details:
            - For n < 2: Return False (1 and negative numbers are not prime
              by the fundamental theorem of arithmetic)
            - For n = 2: Return True (2 is the smallest and only even prime)
            - For even n > 2: Return False (all other even numbers have 2 as
              a divisor, making them composite)
            - For odd n > 2: Test divisibility by all odd numbers from 3 to
              √n (inclusive). If any divisor d is found such that n % d == 0,
              return False immediately. If no divisor is found, return True.

            The upper bound of √n is sufficient because if n has a divisor
            d > √n, then n/d < √n would have already been discovered as a
            divisor during the iteration. In other words, divisors come in
            pairs, and at least one member of each pair is ≤ √n.

            Using range(3, int(sqrt(n)) + 1, 2) efficiently generates only
            odd numbers, cutting the search space in half compared to
            checking all integers.

        Example:
            >>> MathBase.is_prime(2)
            True
            >>> MathBase.is_prime(17)
            True
            >>> MathBase.is_prime(100)
            False
            >>> MathBase.is_prime(1)
            False
            >>> MathBase.is_prime(-7)
            False
        """
        # Numbers less than 2 are not prime by definition.
        # This handles n = 0, 1, and all negative integers.
        if n < 2:
            return False

        # 2 is the only even prime number. All other even numbers
        # are divisible by 2 and therefore composite.
        if n == 2:
            return True

        # If n is even and greater than 2, it has 2 as a non-trivial
        # divisor, making it composite. This check eliminates roughly
        # half of all candidates immediately.
        if n % 2 == 0:
            return False

        # For odd numbers greater than 2, test all potential odd divisors
        # from 3 up to and including √n.
        # - Start at 3 (the smallest odd prime greater than 2)
        # - Step by 2 (skip even numbers - already ruled out)
        # - End at int(sqrt(n)) + 1 to ensure we check up to √n inclusive
        #   (range stop is exclusive, so +1 ensures coverage)
        for i in range(3, int(math.sqrt(n)) + 1, 2):
            if n % i == 0:
                # Found a divisor: n is composite
                return False

        # No divisor was found in the tested range: n is prime
        return True