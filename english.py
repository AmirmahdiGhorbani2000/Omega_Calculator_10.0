# =============================================================================
# Omega Calculator 10.0 - Module 8: English User Interface
# Author: Amirmahdi Ghorbani
# =============================================================================
# This module implements the complete English-language user interface for
# the Omega Calculator. It contains the CalculatorAppEN class which handles
# all user interaction, menu navigation, input prompting, and result display
# in English.
#
# Architecture:
#   The class composes (uses) all core engine modules through instance
#   attributes initialized in __init__(). It does NOT inherit from them.
#   This composition-over-inheritance design keeps the UI layer cleanly
#   separated from the computation layer.
#
# Menu Structure (9 main categories):
#   1. Basic Operations (arithmetic, powers, absolute value, factorial)
#   2. Algebra & Equations (linear through decic, matrices)
#   3. Geometry & Measurement (shapes, volume, trigonometry, unit conversion)
#   4. Number Theory (GCD/LCM, primes, patterns, number bases)
#   5. Statistics (mean/median/mode, distributions, random numbers)
#   6. Calculus (derivatives, integrals)
#   7. Physics (8 subfields, 69 formulas, 17 constants)
#   8. Periodic Table (118 elements)
#   9. Exit
#
# Dependencies:
#   - color (local): Terminal text coloring
#   - math_base (local): MathBase class
#   - equations (local): EquationSolver class
#   - calculus (local): Calculus class
#   - matrix_ops (local): MatrixOperations class
#   - formulas (local): PhysicsFormulas class
#   - constants (local): PhysicalConstants class
#   - periodic_table (local): PeriodicTable class
#   - random, math, os, time (standard library)
#
# Last Modified: 2026-05-29
# Version: 10.0 (Modular Edition)
# =============================================================================

from color import *
import random
from math import *
import os
import time

# Import all core engine modules
from math_base import MathBase
from equations import EquationSolver
from calculus import Calculus
from matrix_ops import MatrixOperations
from formulas import PhysicsFormulas
from constants import PhysicalConstants
from periodic_table import PeriodicTable


class CalculatorAppEN:
    """
    English-language user interface for Omega Calculator.

    This class encapsulates all interactive functionality for the
    English language mode. It composes the core mathematical engine
    classes and provides the menu-driven interface that users interact
    with. The class is designed to be instantiated once per application
    session.
    """

    def __init__(self):
        """
        Initializes the English UI by creating references to all core
        engine components. Each engine component is a stateless utility
        class; instances are created for convenient access but no state
        is maintained.
        """
        self.math_base = MathBase()
        self.eq_solver = EquationSolver()
        self.calculus = Calculus()
        self.matrix_ops = MatrixOperations()
        self.physics = PhysicsFormulas()
        self.constants = PhysicalConstants()
        self.periodic = PeriodicTable()

    # =========================================================================
    # UTILITY METHODS
    # =========================================================================

    def mabna(self):
        """Handles number base (radix) conversion operations."""
        red("Number Radixes")
        blue("A) Decimal to...")
        blue("B) ... to decimal")
        dec = input("Which one do you want? ")
        time.sleep(0.2)
        os.system("clear")
        if dec == "A":
            blue("1.Decimal to binary\n 2.Decimal to octal\n 3.Decimal to hexadecimal")
            d = int(input("Which one do you want? "))
            num = int(input("Decimal number: "))
            if d == 1:
                purple(f"{num} = {bin(num)}")
            elif d == 2:
                purple(f"{num} = {oct(num)}")
            elif d == 3:
                purple(f"{num} = {hex(num)}")
        elif dec == "B":
            num = input("Number: ")
            INT = int(num)
            purple(f"{num} = {INT}")

    def lcm(self, a, b):
        """Calculates Least Common Multiple of two integers."""
        return (abs(a * b)) // gcd(a, b)

    def cot(self, x):
        """Calculates cotangent of an angle in radians."""
        return cos(x) / sin(x)

    def is_prime(self, n):
        """Determines whether a given integer is prime."""
        if n < 2:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        for i in range(3, int(sqrt(n)) + 1, 2):
            if n % i == 0:
                return False
        return True

    # =========================================================================
    # MENU 1: BASIC OPERATIONS
    # =========================================================================

    def bf(self):
        """Evaluates a user-provided mathematical expression."""
        red("Four Basic Operations")
        yellow("Write a mathematical expression like 2+4×9÷7")
        express = input("").replace("×", "*").replace("÷", "/")
        express = str(eval(express))
        result = "Result is " + express
        purple(result)

    def moshtagh(self):
        """Computes numerical derivative at a point."""
        red("Derivative")
        expr = input("Function (like 2^x): ")
        x = float(input("Dot: "))
        expr = expr.replace("^", "**").replace("×", "*").replace("÷", "/")
        i = self.calculus.der(expr, x)
        purple(f"Result is {i}")

    def pr(self):
        """Handles power and root calculations."""
        red("Powers and Radicals")
        blue("A)Power\n B)Radical")
        powerORradical = input("Write A or B:  ")
        if powerORradical == "A":
            power = input("Write something like 4^3:  ")
            power = "Result is " + str(eval(power.replace("^", "**")))
            purple(power)
        elif powerORradical == "B":
            r1 = float(input("Write number: "))
            r2 = float(input("Write root: "))
            result = "Result is " + str(r1 ** (1 / r2))
            purple(result)
        else:
            red("Not found. Please write A or B.")

    def tri(self):
        """Evaluates trigonometric function expressions."""
        red("Trigonometric Functions")
        yellow("Please write sin(x),cos(x),tan(x) or cot(x).")
        tri = "Result is " + str((eval(input(""))))
        purple(tri)

    def gcdlcm(self):
        """Computes GCD or LCM of two numbers."""
        red("GCD & LCM")
        yellow("Please write gcd(x,y) or lcm(x,y).")
        query = "Result is " + str(eval(input("")))
        purple(query)

    def Abs(self):
        """Computes absolute value of a number."""
        red("Absolute Value")
        result = "Result is " + str(abs(float(input("Write number: "))))
        purple(result)

    def taghrib(self):
        """Rounds a number up (ceil) or down (floor)."""
        red("Approximation")
        up_down = input(
            "Which approximation do you want? To up or down? Write U for up and write D for down: ")
        number = float(input("Write the number: "))
        if up_down in ["U", "D"]:
            if up_down == "U":
                result = "Result is " + str(ceil(number))
            elif up_down == "D":
                result = "Result is " + str(floor(number))
            purple(result)
        else:
            red("Your command not found.")

    def fis(self):
        """Calculates hypotenuse using Pythagorean theorem."""
        red("Pythagorean Relation")
        sides = input("Write the other sides like 9 10: ").split()
        Xside = ((float(sides[0]) ** 2) + (float(sides[1]) ** 2)) ** (1 / 2)
        result = "Result is " + str(Xside)
        purple(result)

    def svm(self):
        """Solves a single-variable linear equation: ax + b = cx + d."""
        red("Single-Variable Equation")
        blue("ax+b=c+d")
        if 2 > 0:
            abcd = input("Write a,b,c,d like 4-8-12-23: ").split("-")
            a = float(abcd[0])
            b = float(abcd[1])
            c = float(abcd[2])
            d = float(abcd[3])
            a = a - c
            d = d - b
            x = d / a
            result = "X is " + str(x)
            purple(result)
        else:
            red("NOT FOUND")

    def Int(self):
        """Computes definite integral using Simpson's rule."""
        red("Integral")
        expr = input("Function (like x^2): ")
        a = float(input("Minimum: "))
        b = float(input("Maximum: "))
        expr = expr.replace("^", "**").replace("×", "*").replace("÷", "/")
        i = self.calculus.integral(expr, a, b)
        purple(f"∫ = {i}")

    def fact(self):
        """Calculates factorial of a non-negative integer."""
        red("Factorial")
        num = int(input("Write the number: "))
        F = factorial(num)
        purple(f"{num}! = {F}")

    def rn(self):
        """Generates a random number in a specified range."""
        red("Make A Random Number")
        yellow("Please write start,stop and step like 1-100-5")
        sss = input("").split("-")
        s1 = int(sss[0])
        s2 = int(sss[1])
        s3 = int(sss[2])
        number = random.randrange(s1, s2, s3)
        result = "Random number is " + str(number)
        purple(result)

    def unit(self):
        """Handles unit conversion for length, temperature, and weight."""
        red("Unit Conversion")
        blue("A) Length (cm,m,km,inch,foot)")
        blue("B) Temperature (C,F,K)")
        blue("C) Weight (g,kg,pound)")
        unit_choice = input("Write A, B or C: ")
        if unit_choice == "A":
            yellow("Write: value from_unit to_unit")
            yellow("Example: 100 cm m")
            parts = input("").split()
            value = float(parts[0])
            from_u = parts[1]
            to_u = parts[2]
            meter_values = {"cm": 0.01, "m": 1, "km": 1000, "inch": 0.0254, "foot": 0.3048}
            in_meters = value * meter_values[from_u]
            result_value = in_meters / meter_values[to_u]
            purple(f"Result is {result_value} {to_u}")
        elif unit_choice == "B":
            yellow("Write: value from_unit to_unit")
            yellow("Example: 100 C F")
            parts = input("").split()
            value = float(parts[0])
            from_u = parts[1]
            to_u = parts[2]
            if from_u == "C":
                if to_u == "F":
                    result_value = (value * 9 / 5) + 32
                elif to_u == "K":
                    result_value = value + 273.15
                else:
                    result_value = value
            elif from_u == "F":
                if to_u == "C":
                    result_value = (value - 32) * 5 / 9
                elif to_u == "K":
                    result_value = (value - 32) * 5 / 9 + 273.15
                else:
                    result_value = value
            elif from_u == "K":
                if to_u == "C":
                    result_value = value - 273.15
                elif to_u == "F":
                    result_value = (value - 273.15) * 9 / 5 + 32
                else:
                    result_value = value
            else:
                result_value = value
            purple(f"Result is {result_value} {to_u}")
        elif unit_choice == "C":
            yellow("Write: value from_unit to_unit")
            yellow("Example: 5 kg pound")
            parts = input("").split()
            value = float(parts[0])
            from_u = parts[1]
            to_u = parts[2]
            gram_values = {"g": 1, "kg": 1000, "pound": 453.592}
            in_grams = value * gram_values[from_u]
            result_value = in_grams / gram_values[to_u]
            purple(f"Result is {result_value} {to_u}")
        else:
            red("Not found.")

    def pa(self):
        """Calculates perimeter and area for geometric shapes."""
        red("Perimeter & Area")
        blue("A) Square")
        blue("B) Rectangle")
        blue("C) Circle")
        blue("D) Triangle")
        shape_choice = input("Write A, B, C or D: ")
        if shape_choice == "A":
            side = float(input("Write side length: "))
            perimeter = 4 * side
            area = side ** 2
            purple(f"Perimeter = {perimeter} , Area = {area}")
        elif shape_choice == "B":
            l = float(input("Write length: "))
            w = float(input("Write width: "))
            perimeter = 2 * (l + w)
            area = l * w
            purple(f"Perimeter = {perimeter} , Area = {area}")
        elif shape_choice == "C":
            r = float(input("Write radius: "))
            perimeter = 2 * pi * r
            area = pi * r ** 2
            purple(f"Circumference = {perimeter} , Area = {area}")
        elif shape_choice == "D":
            yellow("A) Equilateral   B) Right   C) Arbitrary")
            tri_type = input("Write A, B or C: ")
            if tri_type == "A":
                s = float(input("Write side: "))
                perimeter = 3 * s
                area = (sqrt(3) / 4) * s ** 2
                purple(f"Perimeter = {perimeter} , Area = {area}")
            elif tri_type == "B":
                a = float(input("Write first leg: "))
                b = float(input("Write second leg: "))
                c = sqrt(a ** 2 + b ** 2)
                perimeter = a + b + c
                area = 0.5 * a * b
                purple(f"Perimeter = {perimeter} , Area = {area}")
            elif tri_type == "C":
                s1 = float(input("Write side 1: "))
                s2 = float(input("Write side 2: "))
                s3 = float(input("Write side 3: "))
                perimeter = s1 + s2 + s3
                sp = perimeter / 2
                area = sqrt(sp * (sp - s1) * (sp - s2) * (sp - s3))
                purple(f"Perimeter = {perimeter} , Area = {area}")
            else:
                red("Not found.")
        else:
            red("Not found.")

    def numg(self):
        """Number-guessing game with 10 attempts."""
        red("Number-guessing Game")
        yellow("I have a number between 1 and 100. Can you guess it?")
        secret = random.randint(1, 100)
        attempts = 0
        guessed = False
        while attempts < 10 and not guessed:
            try:
                guess = int(input(f"Attempt {attempts + 1}/10 - Your guess: "))
                attempts += 1
                if guess == secret:
                    green("🎉 Correct! You guessed it!")
                    guessed = True
                elif guess < secret:
                    yellow("Go higher!")
                else:
                    yellow("Go lower!")
            except:
                red("Please enter a valid number.")
        if not guessed:
            purple(f"Game over! The number was {secret}.")

    def td(self):
        """Calculates volume of 3D shapes."""
        red("Volume of 3D shapes")
        blue("A) Cube")
        blue("B) Sphere")
        blue("C) Cylinder")
        blue("D) Cone")
        shape_3d = input("Write A, B, C or D: ")
        if shape_3d == "A":
            side = float(input("Write side length: "))
            volume = side ** 3
            purple(f"Volume = {volume}")
        elif shape_3d == "B":
            r = float(input("Write radius: "))
            volume = (4 / 3) * pi * r ** 3
            purple(f"Volume = {volume}")
        elif shape_3d == "C":
            r = float(input("Write radius: "))
            h = float(input("Write height: "))
            volume = pi * r ** 2 * h
            purple(f"Volume = {volume}")
        elif shape_3d == "D":
            r = float(input("Write radius: "))
            h = float(input("Write height: "))
            volume = (1 / 3) * pi * r ** 2 * h
            purple(f"Volume = {volume}")
        else:
            red("Not found.")

    def Fo(self):
        """Displays famous mathematical patterns."""
        red("Famous Patterns")
        blue("A) Fibonacci sequence")
        blue("B) Pascal's triangle")
        blue("C) Multiplication pattern")
        pat_choice = input("Write A, B or C: ")
        if pat_choice == "A":
            n = int(input("How many terms? "))
            a, b = 0, 1
            result = ""
            for i in range(n):
                result += str(a) + " "
                a, b = b, a + b
            purple(result)
        elif pat_choice == "B":
            rows = int(input("How many rows? "))
            for i in range(rows):
                row_val = 1
                line = ""
                for j in range(i + 1):
                    line += str(row_val) + " "
                    row_val = row_val * (i - j) // (j + 1)
                purple(line.center(50))
        elif pat_choice == "C":
            n = int(input("Write a number: "))
            for i in range(1, n + 1):
                line = ""
                for j in range(1, n + 1):
                    line += str(i * j) + "\t"
                purple(line)
        else:
            red("Not found.")

    def matris(self):
        """Matrix operations: add, multiply, determinant, inverse."""
        red("Matrix")
        blue("1.Add")
        blue("2.Multiply")
        blue("3.Determinant")
        blue("4.Inverse (2x2)")
        mat = int(input("Which one do you want? "))
        time.sleep(0.2)
        os.system("clear")
        if mat == 1:
            print("Write matrixes like 1,2,3;4,5,6;7,8,9")
            a = input("Write first matrix: ")
            b = input("Write second matrix: ")
            A = self.matrix_ops.matrix(a)
            B = self.matrix_ops.matrix(b)
            add = self.matrix_ops.matrix_add(A, B)
            purple("Result:")
            purple(f"{add}")
        elif mat == 2:
            print("Write matrixes like 1,2,3;4,5,6;7,8,9")
            a = input("Write first matrix: ")
            b = input("Write second matrix: ")
            A = self.matrix_ops.matrix(a)
            B = self.matrix_ops.matrix(b)
            add = self.matrix_ops.matrix_multiply(A, B)
            purple("Result:")
            purple(add)
        elif mat == 3:
            print("Write matrix like 1,2,3;4,5,6;7,8,9")
            a = input("Write matrix: ")
            A = self.matrix_ops.matrix(a)
            add = self.matrix_ops.determinant(A)
            purple("Result:")
            purple(f"{add}")
        elif mat == 4:
            print("Write matrixes like 1,2,3;4,5,6;7,8,9")
            a = input("Write matrix: ")
            A = self.matrix_ops.matrix(a)
            add = self.matrix_ops.inverse_2x2(A)
            purple("Result:")
            purple(f"{add}")

    def jadval(self):
        """Displays multiplication tables."""
        red("Multiplication Table")
        blue("A) Single number")
        blue("B) Range of numbers")
        mul_choice = input("Write A or B: ")
        if mul_choice == "A":
            num = int(input("Write a number: "))
            limit = int(input("Up to: "))
            for i in range(1, limit + 1):
                purple(f"{num} × {i} = {num * i}")
        elif mul_choice == "B":
            start = int(input("Write start: "))
            end = int(input("Write end: "))
            for i in range(start, end + 1):
                line = ""
                for j in range(1, 11):
                    line += f"{i}×{j}={i * j}  "
                purple(line)
        else:
            red("Not found.")

    def tvm(self):
        """Solves a system of two linear equations using Cramer's rule."""
        red("Two-Variable Equations")
        cyan("Form:")
        yellow("ax+by=c\n dx+ey=f")
        yellow("Write a,b,c,d,e,f separated by -")
        yellow("Example: 2-3-8-1-2-5")
        parts = input("").split("-")
        a1 = float(parts[0])
        b1 = float(parts[1])
        c1 = float(parts[2])
        a2 = float(parts[3])
        b2 = float(parts[4])
        c2 = float(parts[5])
        det = a1 * b2 - a2 * b1
        if det == 0:
            red("No unique solution (determinant is zero).")
        else:
            x = (c1 * b2 - c2 * b1) / det
            y = (a1 * c2 - a2 * c1) / det
            purple(f"x = {x} , y = {y}")

    def d2m(self):
        """Solves a quadratic equation using the quadratic formula."""
        red("Quadratic Equation")
        yellow("Form: ax² + bx + c = 0")
        yellow("Write a,b,c separated by -")
        yellow("Example: 1-5-6")
        parts = input("").split("-")
        a = float(parts[0])
        b = float(parts[1])
        c = float(parts[2])
        if a == 0:
            red("This is not a quadratic equation (a cannot be zero).")
        else:
            delta = b ** 2 - 4 * a * c
            if delta > 0:
                x1 = (-b + sqrt(delta)) / (2 * a)
                x2 = (-b - sqrt(delta)) / (2 * a)
                purple(f"Two real roots: x1 = {x1} , x2 = {x2}")
            elif delta == 0:
                x = -b / (2 * a)
                purple(f"Double root: x = {x}")
            else:
                real = -b / (2 * a)
                imag = sqrt(abs(delta)) / (2 * a)
                purple(f"Complex roots: x1 = {real}+{imag}i , x2 = {real}-{imag}i")

    def m(self):
        """Calculates statistical measures: mean, median, mode."""
        red("Statistical Mean")
        blue("A) Mean (average)")
        blue("B) Median")
        blue("C) Mode")
        stat_choice = input("Write A, B or C: ")
        yellow("Write numbers separated by space (example: 5 8 12 3 9)")
        nums = list(map(float, input("").split()))
        nums.sort()
        if stat_choice == "A":
            mean_val = sum(nums) / len(nums)
            purple(f"Mean = {mean_val}")
        elif stat_choice == "B":
            n = len(nums)
            if n % 2 == 0:
                median_val = (nums[n // 2 - 1] + nums[n // 2]) / 2
            else:
                median_val = nums[n // 2]
            purple(f"Median = {median_val}")
        elif stat_choice == "C":
            freq = {}
            for num in nums:
                freq[num] = freq.get(num, 0) + 1
            max_freq = max(freq.values())
            modes = [k for k, v in freq.items() if v == max_freq]
            if len(modes) == len(nums):
                purple("No mode (all values appear once).")
            else:
                purple(f"Mode(s) = {modes}")
        else:
            red("Not found.")

    def Variate(self):
        """Generates random numbers from 10 probability distributions."""
        red("Statistical Distributions")
        blue("A) Uniform (random between a and b)")
        blue("B) Normal (Gaussian)")
        blue("C) Triangular")
        blue("D) Exponential")
        blue("E) Beta")
        blue("F) Gamma")
        blue("G) Lognormal")
        blue("H) Pareto")
        blue("I) Weibull")
        blue("J) Von Mises")
        dist_choice = input("Write a letter (A to J): ")
        try:
            if dist_choice == "A":
                a = float(input("Write min: "))
                b = float(input("Write max: "))
                result = random.uniform(a, b)
                purple(f"Uniform random value: {result}")
            elif dist_choice == "B":
                mu = float(input("Write mean (mu): "))
                sigma = float(input("Write standard deviation (sigma): "))
                result = random.gauss(mu, sigma)
                purple(f"Normal random value: {result}")
            elif dist_choice == "C":
                low = float(input("Write low: "))
                high = float(input("Write high: "))
                mode = float(input("Write mode: "))
                result = random.triangular(low, high, mode)
                purple(f"Triangular random value: {result}")
            elif dist_choice == "D":
                lam = float(input("Write lambda (rate parameter): "))
                result = random.expovariate(lam)
                purple(f"Exponential random value: {result}")
            elif dist_choice == "E":
                alpha = float(input("Write alpha: "))
                beta = float(input("Write beta: "))
                result = random.betavariate(alpha, beta)
                purple(f"Beta random value: {result}")
            elif dist_choice == "F":
                alpha = float(input("Write alpha: "))
                beta = float(input("Write beta: "))
                result = random.gammavariate(alpha, beta)
                purple(f"Gamma random value: {result}")
            elif dist_choice == "G":
                mu = float(input("Write mu: "))
                sigma = float(input("Write sigma: "))
                result = random.lognormvariate(mu, sigma)
                purple(f"Lognormal random value: {result}")
            elif dist_choice == "H":
                alpha = float(input("Write alpha: "))
                result = random.paretovariate(alpha)
                purple(f"Pareto random value: {result}")
            elif dist_choice == "I":
                alpha = float(input("Write alpha: "))
                beta = float(input("Write beta: "))
                result = random.weibullvariate(alpha, beta)
                purple(f"Weibull random value: {result}")
            elif dist_choice == "J":
                mu = float(input("Write mu: "))
                kappa = float(input("Write kappa: "))
                result = random.vonmisesvariate(mu, kappa)
                purple(f"Von Mises random value: {result}")
            else:
                red("Not found.")
        except:
            red("Error in generating distribution. Check your parameters.")

    def prime(self):
        """Prime number detection and generation."""
        red("Prime Number Detection")
        blue("A) Check if a number is prime")
        blue("B) Find all primes up to N")
        prime_choice = input("Write A or B: ")
        if prime_choice == "A":
            n = int(input("Write a number: "))
            if self.is_prime(n):
                green(f"{n} is a prime number! ✅")
            else:
                red(f"{n} is NOT a prime number. ❌")
        elif prime_choice == "B":
            limit = int(input("Write limit N: "))
            primes = []
            for i in range(2, limit + 1):
                if self.is_prime(i):
                    primes.append(i)
            purple(f"Prime numbers up to {limit}:")
            purple(str(primes))
            green(f"Total: {len(primes)} primes found.")
        else:
            red("Not found.")

    def jabr(self):
        """Basic algebraic operations."""
        red("Basic Algebra")
        blue("A) (a+b)^2 and (a-b)^2 expansion")
        blue("B) a^2 - b^2 factorization")
        blue("C) Simple quadratic factoring")
        blue("D) Evaluate polynomial at x")
        alg_choice = input("Write A, B, C or D: ")
        if alg_choice == "A":
            a = float(input("Write a: "))
            b = float(input("Write b: "))
            sum_sq = a ** 2 + 2 * a * b + b ** 2
            diff_sq = a ** 2 - 2 * a * b + b ** 2
            purple(f"(a+b)^2 = {sum_sq}")
            purple(f"(a-b)^2 = {diff_sq}")
        elif alg_choice == "B":
            a = float(input("Write a: "))
            b = float(input("Write b: "))
            result = a ** 2 - b ** 2
            purple(f"a^2 - b^2 = {result}")
            purple(f"Factored form: ({a}+{b})({a}-{b}) = {result}")
        elif alg_choice == "C":
            yellow("Form: x^2 + px + q = 0")
            p = float(input("Write p: "))
            q = float(input("Write q: "))
            delta_fact = p ** 2 - 4 * q
            if delta_fact < 0:
                red("Cannot factor with real numbers.")
            else:
                r1 = (-p + sqrt(delta_fact)) / 2
                r2 = (-p - sqrt(delta_fact)) / 2
                purple(f"Factored form: (x - {r1})(x - {r2})")
        elif alg_choice == "D":
            yellow("Write coefficients from highest degree (space-separated)")
            yellow("Example: 1 -3 2  means x^2 - 3x + 2")
            coeffs = list(map(float, input("Coefficients: ").split()))
            x_val = float(input("Write x value: "))
            result = 0
            n = len(coeffs) - 1
            for c in coeffs:
                result = result * x_val + c
            purple(f"P({x_val}) = {result}")
        else:
            red("Not found.")

    # =========================================================================
    # POLYNOMIAL EQUATION SOLVERS
    # =========================================================================

    def quartic_equation(self):
        """Solves a quartic (4th degree) equation."""
        red("Quartic Equation (Degree 4)")
        blue("ax⁴+bx³+cx²+dx+e=0")
        a = self.math_base.infut("a: ")
        b = self.math_base.infut("b: ")
        c = self.math_base.infut("c: ")
        d = self.math_base.infut("d: ")
        e = self.math_base.infut("e: ")
        roots = self.eq_solver.solve_quartic(a, b, c, d, e)
        purple(f"Roots = {roots}")

    def quintic_equation(self):
        """Solves a quintic (5th degree) equation numerically."""
        red("Quintic Equation (Degree 5)")
        blue("ax⁵+bx⁴+cx³+dx²+ex+f=0")
        parts = input("Write a,b,c,d,e,f like 1;2;3;4;5;6: ").split(";")
        coeffs = [float(p) for p in parts]
        roots = self.eq_solver.solve_polynomial_general(coeffs)
        purple(f"Roots = {roots}")

    def sextic_equation(self):
        """Solves a sextic (6th degree) equation numerically."""
        red("Sextic Equation (Degree 6)")
        blue("ax⁶+bx⁵+cx⁴+dx³+ex²+fx+g=0")
        parts = input("Write a,b,c,d,e,f,g like 1;2;3;4;5;6;7: ").split(";")
        coeffs = [float(p) for p in parts]
        roots = self.eq_solver.solve_polynomial_general(coeffs)
        purple(f"Roots = {roots}")

    def septic_equation(self):
        """Solves a septic (7th degree) equation numerically."""
        red("Septic Equation (Degree 7)")
        blue("ax⁷+bx⁶+cx⁵+dx⁴+ex³+fx²+gx+h=0")
        parts = input("Write a,b,c,d,e,f,g,h like 1;2;3;4;5;6;7;8: ").split(";")
        coeffs = [float(p) for p in parts]
        roots = self.eq_solver.solve_polynomial_general(coeffs)
        purple(f"Roots = {roots}")

    def octic_equation(self):
        """Solves an octic (8th degree) equation numerically."""
        red("Octic Equation (Degree 8)")
        blue("ax⁸+bx⁷+cx⁶+dx⁵+ex⁴+fx³+gx²+hx+i=0")
        parts = input("Write a,b,c,d,e,f,g,h,i like 1;2;3;4;5;6;7;8;9: ").split(";")
        coeffs = [float(p) for p in parts]
        roots = self.eq_solver.solve_polynomial_general(coeffs)
        purple(f"Roots = {roots}")

    def nonic_equation(self):
        """Solves a nonic (9th degree) equation numerically."""
        red("Nonic Equation (Degree 9)")
        blue("ax⁹+bx⁸+cx⁷+dx⁶+ex⁵+fx⁴+gx³+hx²+ix+j=0")
        parts = input("Write coefficients (10 numbers): ").split(";")
        coeffs = [float(p) for p in parts]
        roots = self.eq_solver.solve_polynomial_general(coeffs)
        purple(f"Roots = {roots}")

    def decic_equation(self):
        """Solves a decic (10th degree) equation numerically."""
        red("Decic Equation (Degree 10)")
        blue("ax¹⁰+bx⁹+cx⁸+dx⁷+ex⁶+fx⁵+gx⁴+hx³+ix²+jx+k=0")
        parts = input("Write coefficients (11 numbers): ").split(";")
        coeffs = [float(p) for p in parts]
        roots = self.eq_solver.solve_polynomial_general(coeffs)
        purple(f"Roots = {roots}")

    # =========================================================================
    # PHYSICS SUB-MENUS (English)
    # =========================================================================

    def _physics_kinematics_en(self):
        """Kinematics formulas menu."""
        purple("Kinematics")
        cyan("1.Final velocity [v=v0+at]")
        cyan("2.Position [x=x0+v0t+0.5at²]")
        cyan("3.Final velocity [v²=v0²+2aΔx]")
        cyan("4.Average velocity [v_avg=Δx/Δt]")
        cyan("5.Average acceleration [a_avg=Δv/Δt]")
        cyan("6.Free fall velocity [v=gt]")
        cyan("7.Free fall height [h=0.5gt²]")
        cyan("8.Projectile range [R=v0²sin(2θ)/g]")
        cyan("9.Projectile max height [H=v0²sin²θ/(2g)]")
        cyan("10.Projectile time of flight [T=2v0sinθ/g]")
        cin = int(input("Which one do you want? "))
        time.sleep(0.2)
        os.system("clear")
        infut = self.math_base.infut
        if cin == 1:
            red("v = v0 + at")
            v0 = infut("v0: "); a = infut("a: "); t = infut("t: ")
            purple(f"v = {self.physics.velocity_final_1(v0, a, t)}")
        elif cin == 2:
            red("x = x0 + v0t + 0.5at²")
            x0 = infut("x0: "); v0 = infut("v0: "); a = infut("a: "); t = infut("t: ")
            purple(f"x = {self.physics.position_2(x0, v0, a, t)}")
        elif cin == 3:
            red("v² = v0² + 2aΔx")
            v0 = infut("v0: "); a = infut("a: "); dx = infut("dx: ")
            purple(f"v = {self.physics.velocity_final_3(v0, a, dx)}")
        elif cin == 4:
            red("v_avg = Δx/Δt")
            dx = infut("dx: "); dt = infut("dt: ")
            purple(f"v_avg = {self.physics.velocity_average(dx, dt)}")
        elif cin == 5:
            red("a_avg = Δv/Δt")
            dv = infut("dv: "); dt = infut("dt: ")
            purple(f"a_avg = {self.physics.acceleration_average(dv, dt)}")
        elif cin == 6:
            red("v = gt")
            g = infut("g: "); t = infut("t: ")
            purple(f"v = {self.physics.free_fall_velocity(t, g)}")
        elif cin == 7:
            red("h = 0.5gt²")
            g = infut("g: "); t = infut("t: ")
            purple(f"h = {self.physics.free_fall_height(t, g)}")
        elif cin == 8:
            red("R = v0²sin(2θ)/g")
            v0 = infut("v0: "); theta = infut("theta (degrees): "); g = infut("g: ")
            purple(f"Range = {self.physics.projectile_range(v0, theta, g)}")
        elif cin == 9:
            red("H = v0²sin²θ/(2g)")
            v0 = infut("v0: "); theta = infut("theta (degrees): "); g = infut("g: ")
            purple(f"Max Height = {self.physics.projectile_max_height(v0, theta, g)}")
        elif cin == 10:
            red("T = 2v0sinθ/g")
            v0 = infut("v0: "); theta = infut("theta (degrees): "); g = infut("g: ")
            purple(f"Time of flight = {self.physics.projectile_time_of_flight(v0, theta, g)}")

    def _physics_dynamics_en(self):
        """Dynamics formulas menu."""
        purple("Dynamics")
        cyan("1.Force [F=ma]"); cyan("2.Weight [w=mg]")
        cyan("3.Normal force on incline [N=mgcosθ]")
        cyan("4.Kinetic friction [f_k=μ_k N]")
        cyan("5.Max static friction [f_s=μ_s N]")
        cyan("6.Net force 1D [F_net=ΣF]"); cyan("7.Momentum [p=mv]")
        cyan("8.Impulse [J=FΔt]"); cyan("9.Hooke's law [F=-kx]")
        cin = int(input("Which one do you want? "))
        time.sleep(0.2); os.system("clear")
        infut = self.math_base.infut
        if cin == 1:
            red("F = ma"); m = infut("m: "); a = infut("a: ")
            purple(f"F = {self.physics.force_newton(m, a)}")
        elif cin == 2:
            red("w = mg"); m = infut("m: "); g = infut("g: ")
            purple(f"w = {self.physics.weight(m, g)}")
        elif cin == 3:
            red("N = mgcosθ"); m = infut("m: "); theta = infut("theta (degrees): "); g = infut("g: ")
            purple(f"N = {self.physics.normal_incline(m, theta, g)}")
        elif cin == 4:
            red("f_k = μ_k N"); mu_k = infut("μ_k: "); N = infut("N: ")
            purple(f"f_k = {self.physics.friction_kinetic(mu_k, N)}")
        elif cin == 5:
            red("f_s_max = μ_s N"); mu_s = infut("μ_s: "); N = infut("N: ")
            purple(f"f_s_max = {self.physics.friction_static_max(mu_s, N)}")
        elif cin == 6:
            red("F_net = ΣF")
            forces = list(map(float, input("Forces separated by space: ").split()))
            purple(f"F_net = {self.physics.net_force_1d(forces)}")
        elif cin == 7:
            red("p = mv"); m = infut("m: "); v = infut("v: ")
            purple(f"p = {self.physics.momentum(m, v)}")
        elif cin == 8:
            red("J = FΔt"); F = infut("F: "); dt = infut("Δt: ")
            purple(f"J = {self.physics.impulse(F, dt)}")
        elif cin == 9:
            red("F = -kx"); k = infut("k: "); x = infut("x: ")
            purple(f"F = {self.physics.hooke_law(k, x)}")

    def _physics_work_energy_en(self):
        """Work, Energy & Power formulas menu."""
        purple("Work, Energy & Power")
        cyan("1.Work [W=Fdcosθ]"); cyan("2.Kinetic energy [KE=0.5mv²]")
        cyan("3.Gravitational PE [PE=mgh]"); cyan("4.Elastic PE [PE=0.5kx²]")
        cyan("5.Work-energy theorem [W_net=ΔKE]"); cyan("6.Mechanical energy [E=KE+PE]")
        cyan("7.Average power [P_avg=W/t]"); cyan("8.Instantaneous power [P=Fvcosθ]")
        cyan("9.Efficiency [η=(W_out/W_in)×100]")
        cin = int(input("Which one do you want? "))
        time.sleep(0.2); os.system("clear")
        infut = self.math_base.infut
        if cin == 1:
            red("W = Fd cosθ"); F = infut("F: "); d = infut("d: "); theta = infut("theta (degrees): ")
            purple(f"W = {self.physics.work(F, d, theta)}")
        elif cin == 2:
            red("KE = 0.5mv²"); m = infut("m: "); v = infut("v: ")
            purple(f"KE = {self.physics.kinetic_energy(m, v)}")
        elif cin == 3:
            red("PE = mgh"); m = infut("m: "); g = infut("g: "); h = infut("h: ")
            purple(f"PE = {self.physics.potential_energy_gravity(m, h, g)}")
        elif cin == 4:
            red("PE = 0.5kx²"); k = infut("k: "); x = infut("x: ")
            purple(f"PE = {self.physics.potential_energy_spring(k, x)}")
        elif cin == 5:
            red("W_net = KE_final - KE_initial"); KE_i = infut("KE_initial: "); KE_f = infut("KE_final: ")
            purple(f"W_net = {self.physics.work_energy_theorem(KE_i, KE_f)}")
        elif cin == 6:
            red("E = KE + PE"); KE = infut("KE: "); PE = infut("PE: ")
            purple(f"E = {self.physics.mechanical_energy(KE, PE)}")
        elif cin == 7:
            red("P_avg = W/t"); W = infut("W: "); t = infut("t: ")
            purple(f"P_avg = {self.physics.power_average(W, t)}")
        elif cin == 8:
            red("P = Fv cosθ"); F = infut("F: "); v = infut("v: "); theta = infut("theta (degrees): ")
            purple(f"P = {self.physics.power_instantaneous(F, v, theta)}")
        elif cin == 9:
            red("η = (W_out / W_in) × 100"); W_out = infut("W_out: "); W_in = infut("W_in: ")
            purple(f"Efficiency = {self.physics.efficiency(W_out, W_in)}%")

    def _physics_fluids_en(self):
        """Fluid Mechanics formulas menu."""
        purple("Fluid Mechanics")
        cyan("1.Density [ρ=m/V]"); cyan("2.Pressure [P=F/A]")
        cyan("3.Pressure at depth [P=P0+ρgh]"); cyan("4.Buoyant force [F_b=ρ_fluid V_sub g]")
        cyan("5.Bernoulli equation [P2=P1+0.5ρ(v1²-v2²)+ρg(h1-h2)]")
        cyan("6.Continuity equation [v2=A1v1/A2]")
        cin = int(input("Which one do you want? "))
        time.sleep(0.2); os.system("clear")
        infut = self.math_base.infut
        if cin == 1:
            red("ρ = m/V"); m = infut("m: "); V = infut("V: ")
            purple(f"ρ = {self.physics.density(m, V)}")
        elif cin == 2:
            red("P = F/A"); F = infut("F: "); A = infut("A: ")
            purple(f"P = {self.physics.pressure(F, A)}")
        elif cin == 3:
            red("P = P0 + ρgh"); P0 = infut("P0: "); rho = infut("ρ: "); h = infut("h: "); g = infut("g: ")
            purple(f"P = {self.physics.pressure_depth(P0, rho, h, g)}")
        elif cin == 4:
            red("F_b = ρ_fluid × V_sub × g"); rho_f = infut("ρ_fluid: "); V_sub = infut("V_submerged: "); g = infut("g: ")
            purple(f"F_b = {self.physics.buoyant_force(rho_f, V_sub, g)}")
        elif cin == 5:
            red("P2 = P1 + 0.5ρ(v1²-v2²) + ρg(h1-h2)")
            P1 = infut("P1: "); v1 = infut("v1: "); h1 = infut("h1: ")
            v2 = infut("v2: "); h2 = infut("h2: "); rho = infut("ρ: "); g = infut("g: ")
            purple(f"P2 = {self.physics.bernoulli_simple(P1, v1, h1, v2, h2, rho, g)}")
        elif cin == 6:
            red("A1v1 = A2v2 → v2 = A1v1/A2"); A1 = infut("A1: "); v1 = infut("v1: "); A2 = infut("A2: ")
            purple(f"v2 = {self.physics.continuity_equation(A1, v1, A2)}")

    def _physics_electricity_en(self):
        """Electricity & Magnetism formulas menu."""
        purple("Electricity & Magnetism")
        cyan("1.Ohm's law - Voltage [V=IR]"); cyan("2.Ohm's law - Current [I=V/R]")
        cyan("3.Ohm's law - Resistance [R=V/I]"); cyan("4.Electric power [P=VI]")
        cyan("5.Electric power [P=I²R]"); cyan("6.Electric power [P=V²/R]")
        cyan("7.Resistors series [R_total=R1+R2+...]"); cyan("8.Resistors parallel [1/R_total=1/R1+1/R2+...]")
        cyan("9.Voltage from energy [V=W/q]"); cyan("10.Current [I=Δq/Δt]")
        cyan("11.Coulomb's law [F=kq1q2/r²]"); cyan("12.Electric field [E=F/q]")
        cyan("13.Electric field parallel plate [E=V/d]")
        cin = int(input("Which one do you want? "))
        time.sleep(0.2); os.system("clear")
        infut = self.math_base.infut
        if cin == 1:
            red("V = IR"); I = infut("I: "); R = infut("R: ")
            purple(f"V = {self.physics.ohms_law_voltage(I, R)}")
        elif cin == 2:
            red("I = V/R"); V = infut("V: "); R = infut("R: ")
            purple(f"I = {self.physics.ohms_law_current(V, R)}")
        elif cin == 3:
            red("R = V/I"); V = infut("V: "); I = infut("I: ")
            purple(f"R = {self.physics.ohms_law_resistance(V, I)}")
        elif cin == 4:
            red("P = VI"); V = infut("V: "); I = infut("I: ")
            purple(f"P = {self.physics.electric_power_vi(V, I)}")
        elif cin == 5:
            red("P = I²R"); I = infut("I: "); R = infut("R: ")
            purple(f"P = {self.physics.electric_power_i2r(I, R)}")
        elif cin == 6:
            red("P = V²/R"); V = infut("V: "); R = infut("R: ")
            purple(f"P = {self.physics.electric_power_v2r(V, R)}")
        elif cin == 7:
            red("R_total = R1 + R2 + ...")
            resistors = list(map(float, input("Resistors separated by space: ").split()))
            purple(f"R_total = {self.physics.resistors_series(resistors)}")
        elif cin == 8:
            red("1/R_total = 1/R1 + 1/R2 + ...")
            resistors = list(map(float, input("Resistors separated by space: ").split()))
            purple(f"R_total = {self.physics.resistors_parallel(resistors)}")
        elif cin == 9:
            red("V = W/q"); W = infut("W: "); q = infut("q: ")
            purple(f"V = {self.physics.voltage_energy(W, q)}")
        elif cin == 10:
            red("I = Δq/Δt"); q = infut("Δq: "); t = infut("Δt: ")
            purple(f"I = {self.physics.current_rate(q, t)}")
        elif cin == 11:
            red("F = k q1 q2 / r²"); q1 = infut("q1: "); q2 = infut("q2: "); r = infut("r: ")
            k = infut("k (default 8.99e9): ")
            if k == 0: F = self.physics.coulomb_law(q1, q2, r)
            else: F = self.physics.coulomb_law(q1, q2, r, k)
            purple(f"F = {F}")
        elif cin == 12:
            red("E = F/q"); F = infut("F: "); q = infut("q: ")
            purple(f"E = {self.physics.electric_field(F, q)}")
        elif cin == 13:
            red("E = V/d"); V = infut("V: "); d = infut("d: ")
            purple(f"E = {self.physics.electric_field_parallel_plate(V, d)}")

    def _physics_heat_en(self):
        """Heat & Thermodynamics formulas menu."""
        purple("Heat & Thermodynamics")
        cyan("1.Sensible heat [Q=mcΔT]"); cyan("2.Latent heat of fusion [Q=mL_f]")
        cyan("3.Latent heat of vaporization [Q=mL_v]"); cyan("4.Linear expansion [ΔL=αL0ΔT]")
        cyan("5.Area expansion [ΔA=βA0ΔT]"); cyan("6.Volume expansion [ΔV=γV0ΔT]")
        cyan("7.Ideal gas pressure [P=nRT/V]"); cyan("8.Ideal gas volume [V=nRT/P]")
        cyan("9.First law of thermodynamics [ΔU=Q-W]"); cyan("10.Heat engine efficiency [η=1-Q_c/Q_h]")
        cin = int(input("Which one do you want? "))
        time.sleep(0.2); os.system("clear")
        infut = self.math_base.infut
        if cin == 1:
            red("Q = mcΔT"); m = infut("m: "); c = infut("c: "); delta_T = infut("ΔT: ")
            purple(f"Q = {self.physics.heat_sensible(m, c, delta_T)}")
        elif cin == 2:
            red("Q = mL_f"); m = infut("m: "); L_f = infut("L_f: ")
            purple(f"Q = {self.physics.heat_latent_fusion(m, L_f)}")
        elif cin == 3:
            red("Q = mL_v"); m = infut("m: "); L_v = infut("L_v: ")
            purple(f"Q = {self.physics.heat_latent_vaporization(m, L_v)}")
        elif cin == 4:
            red("ΔL = α L0 ΔT"); L0 = infut("L0: "); alpha = infut("α: "); delta_T = infut("ΔT: ")
            purple(f"ΔL = {self.physics.thermal_expansion_linear(L0, alpha, delta_T)}")
        elif cin == 5:
            red("ΔA = β A0 ΔT"); A0 = infut("A0: "); beta = infut("β: "); delta_T = infut("ΔT: ")
            purple(f"ΔA = {self.physics.thermal_expansion_area(A0, beta, delta_T)}")
        elif cin == 6:
            red("ΔV = γ V0 ΔT"); V0 = infut("V0: "); gamma = infut("γ: "); delta_T = infut("ΔT: ")
            purple(f"ΔV = {self.physics.thermal_expansion_volume(V0, gamma, delta_T)}")
        elif cin == 7:
            red("P = nRT/V"); n = infut("n: "); R = infut("R: "); T = infut("T: "); V = infut("V: ")
            purple(f"P = {self.physics.ideal_gas_law_pressure(n, R, T, V)}")
        elif cin == 8:
            red("V = nRT/P"); n = infut("n: "); R = infut("R: "); T = infut("T: "); P = infut("P: ")
            purple(f"V = {self.physics.ideal_gas_law_volume(n, R, T, P)}")
        elif cin == 9:
            red("ΔU = Q - W"); Q = infut("Q: "); W = infut("W: ")
            purple(f"ΔU = {self.physics.first_law_thermodynamics(Q, W)}")
        elif cin == 10:
            red("η = 1 - Q_c/Q_h"); Q_c = infut("Q_c: "); Q_h = infut("Q_h: ")
            purple(f"Efficiency = {self.physics.heat_engine_efficiency(Q_h, Q_c)}")

    def _physics_optics_en(self):
        """Light & Optics formulas menu."""
        purple("Light & Optics")
        cyan("1.Wave speed [c=fλ]"); cyan("2.Refractive index [n=c/v]")
        cyan("3.Snell's law [θ2=arcsin(n1 sinθ1/n2)]"); cyan("4.Lens maker equation [1/f=1/p+1/q]")
        cyan("5.Magnification [M=-q/p]"); cyan("6.Lens power [P=1/f]")
        cyan("7.Critical angle [θ_c=arcsin(n2/n1)]")
        cin = int(input("Which one do you want? "))
        time.sleep(0.2); os.system("clear")
        infut = self.math_base.infut
        if cin == 1:
            red("c = fλ"); f = infut("f: "); lam = infut("λ: ")
            purple(f"c = {self.physics.wave_speed(f, lam)}")
        elif cin == 2:
            red("n = c/v"); c = infut("c: "); v = infut("v: ")
            purple(f"n = {self.physics.refractive_index(c, v)}")
        elif cin == 3:
            red("θ2 = arcsin(n1 sinθ1 / n2)"); n1 = infut("n1: "); theta1 = infut("θ1 (degrees): "); n2 = infut("n2: ")
            purple(f"θ2 = {self.physics.snells_law_angle2(n1, theta1, n2)} degrees")
        elif cin == 4:
            red("1/f = 1/p + 1/q"); p = infut("p: "); q = infut("q: ")
            purple(f"f = {self.physics.lens_maker_equation(0, p, q)}")
        elif cin == 5:
            red("M = -q/p"); p = infut("p: "); q = infut("q: ")
            purple(f"M = {self.physics.magnification(p, q)}")
        elif cin == 6:
            red("P = 1/f"); f = infut("f (meters): ")
            purple(f"P = {self.physics.lens_power(f)} D")
        elif cin == 7:
            red("θ_c = arcsin(n2/n1)"); n1 = infut("n1: "); n2 = infut("n2: ")
            purple(f"θ_c = {self.physics.critical_angle(n1, n2)} degrees")

    def _physics_modern_en(self):
        """Modern Physics formulas menu."""
        purple("Modern Physics")
        cyan("1.Mass-energy equivalence [E=mc²]"); cyan("2.Photon energy [E=hf]")
        cyan("3.Photon energy from wavelength [E=hc/λ]"); cyan("4.de Broglie wavelength [λ=h/mv]")
        cyan("5.Lorentz factor [γ=1/√(1-v²/c²)]"); cyan("6.Time dilation [Δt=γΔt₀]")
        cyan("7.Length contraction [L=L₀/γ]")
        cin = int(input("Which one do you want? "))
        time.sleep(0.2); os.system("clear")
        infut = self.math_base.infut
        if cin == 1:
            red("E = mc²"); m = infut("m: "); c = infut("c (default 3e8): ")
            if c == 0: E = self.physics.mass_energy_equivalence(m)
            else: E = self.physics.mass_energy_equivalence(m, c)
            purple(f"E = {E}")
        elif cin == 2:
            red("E = hf"); f = infut("f: "); h = infut("h (default 6.626e-34): ")
            if h == 0: E = self.physics.photon_energy(f)
            else: E = self.physics.photon_energy(f, h)
            purple(f"E = {E}")
        elif cin == 3:
            red("E = hc/λ"); lam = infut("λ: "); h = infut("h (default 6.626e-34): "); c = infut("c (default 3e8): ")
            if h == 0 and c == 0: E = self.physics.photon_energy_wavelength(lam)
            elif h == 0: E = self.physics.photon_energy_wavelength(lam, c=c)
            elif c == 0: E = self.physics.photon_energy_wavelength(lam, h=h)
            else: E = self.physics.photon_energy_wavelength(lam, h, c)
            purple(f"E = {E}")
        elif cin == 4:
            red("λ = h/mv"); m = infut("m: "); v = infut("v: "); h = infut("h (default 6.626e-34): ")
            if h == 0: lam = self.physics.de_broglie_wavelength(m, v)
            else: lam = self.physics.de_broglie_wavelength(m, v, h)
            purple(f"λ = {lam}")
        elif cin == 5:
            red("γ = 1/√(1-v²/c²)"); v = infut("v: "); c = infut("c (default 3e8): ")
            if c == 0: gamma = self.physics.lorentz_factor(v)
            else: gamma = self.physics.lorentz_factor(v, c)
            purple(f"γ = {gamma}")
        elif cin == 6:
            red("Δt = γ Δt₀"); dt0 = infut("Δt₀: "); v = infut("v: "); c = infut("c (default 3e8): ")
            if c == 0: dt = self.physics.time_dilation(dt0, v)
            else: dt = self.physics.time_dilation(dt0, v, c)
            purple(f"Δt = {dt}")
        elif cin == 7:
            red("L = L₀/γ"); L0 = infut("L₀: "); v = infut("v: "); c = infut("c (default 3e8): ")
            if c == 0: L = self.physics.length_contraction(L0, v)
            else: L = self.physics.length_contraction(L0, v, c)
            purple(f"L = {L}")

    def _physics_constants_en(self):
        """Physical Constants display menu."""
        purple("Physical Constants")
        cyan("1.g = 9.8 m/s²"); cyan("2.G = 6.674×10⁻¹¹ N·m²/kg²")
        cyan("3.c = 3×10⁸ m/s"); cyan("4.h = 6.626×10⁻³⁴ J·s")
        cyan("5.ħ = 1.054×10⁻³⁴ J·s"); cyan("6.k_B = 1.38×10⁻²³ J/K")
        cyan("7.e = 1.6×10⁻¹⁹ C"); cyan("8.ε₀ = 8.85×10⁻¹² C²/N·m²")
        cyan("9.μ₀ = 4π×10⁻⁷ N/A²"); cyan("10.m_e = 9.11×10⁻³¹ kg")
        cyan("11.m_p = 1.67×10⁻²⁷ kg"); cyan("12.N_A = 6.022×10²³ mol⁻¹")
        cyan("13.R = 8.314 J/(mol·K)"); cyan("14.σ = 5.67×10⁻⁸ W/m²·K⁴")
        cyan("15.R_∞ = 1.097×10⁷ m⁻¹"); cyan("16.μ_B = 9.274×10⁻²⁴ J/T")
        cyan("17.a0 = 5.29×10⁻¹¹ m")
        cin = int(input("Which constant do you want? "))
        time.sleep(0.2); os.system("clear")
        if cin == 1: purple(f"g = {self.constants.constant_g()} m/s²")
        elif cin == 2: purple(f"G = {self.constants.constant_G()} N·m²/kg²")
        elif cin == 3: purple(f"c = {self.constants.constant_c()} m/s")
        elif cin == 4: purple(f"h = {self.constants.constant_h()} J·s")
        elif cin == 5: purple(f"ħ = {self.constants.constant_hbar()} J·s")
        elif cin == 6: purple(f"k_B = {self.constants.constant_k_B()} J/K")
        elif cin == 7: purple(f"e = {self.constants.constant_e()} C")
        elif cin == 8: purple(f"ε₀ = {self.constants.constant_epsilon0()} C²/N·m²")
        elif cin == 9: purple(f"μ₀ = {self.constants.constant_mu0()} N/A²")
        elif cin == 10: purple(f"m_e = {self.constants.constant_m_e()} kg")
        elif cin == 11: purple(f"m_p = {self.constants.constant_m_p()} kg")
        elif cin == 12: purple(f"N_A = {self.constants.constant_N_A()} mol⁻¹")
        elif cin == 13: purple(f"R = {self.constants.constant_R()} J/(mol·K)")
        elif cin == 14: purple(f"σ = {self.constants.constant_sigma()} W/m²·K⁴")
        elif cin == 15: purple(f"R_∞ = {self.constants.constant_Rydberg()} m⁻¹")
        elif cin == 16: purple(f"μ_B = {self.constants.constant_mu_B()} J/T")
        elif cin == 17: purple(f"a0 = {self.constants.constant_a0()} m")

    # =========================================================================
    # MAIN APPLICATION LOOP
    # =========================================================================

    def run(self):
        """
        Executes the main application loop for the English interface.

        Displays the main menu with 9 options in an infinite loop.
        The user selects a category, then a specific operation within
        that category. After each operation completes, the user presses
        Enter to return to the main menu. Selecting option 9 exits the
        program.
        """
        while True:
            cyan("Omega Calculator 10.0\n")
            purple("Menu")
            yellow("1.Basic Operations")
            yellow("2.Algebra and Equations")
            yellow("3.Geometry and Measurement")
            yellow("4.Number Theory")
            yellow("5.Statistics")
            yellow("6.Calculus")
            yellow("7.Physics")
            yellow("8.Periodic Table")
            yellow("9.Exit")
            menu = int(input("Which one do you want? "))
            os.system("clear")
            time.sleep(0.25)
            red("Abilities:")
            if menu == 1:
                green("1.Four Basic Operations\n 2.Powers and Radicals")
                green("3.Absolute Value\n 4.Approximation\n 5.Factorial")
                green("6.Multiplication Table")
                A1 = int(input("Which ability do you want? "))
                time.sleep(0.2); os.system("clear")
                if A1 == 1: self.bf()
                elif A1 == 2: self.pr()
                elif A1 == 3: self.Abs()
                elif A1 == 4: self.taghrib()
                elif A1 == 5: self.fact()
                elif A1 == 6: self.jadval()
            elif menu == 2:
                green("1.Basic Algebra\n 2.One-Variable Equation\n 3.Two-Variable Equation\n 4.Quadratic Equation\n 5.Cubic Equation\n 6.Quartic Equation\n 7.Quintic Equation\n 8.Sextic Equation\n 9.Septic Equation\n 10.Octic Equation\n 11.Nonic Equation\n 12.Decic Equation\n 13.Matrix")
                A2 = int(input("Which ability do you want? "))
                time.sleep(0.2); os.system("clear")
                if A2 == 1: self.jabr()
                elif A2 == 2: self.svm()
                elif A2 == 3: self.tvm()
                elif A2 == 4: self.d2m()
                elif A2 == 5:
                    red("Cubic Equation"); blue("ax³+bx²+cx+d=0")
                    n = input("Write a,b,c,d like 5-8-12-39: ").split("-")
                    a = float(n[0]); b = float(n[1]); c = float(n[2]); d = float(n[3])
                    m = self.eq_solver.cubic_equation(a, b, c, d)
                    purple(f"Roots are {m[0]} and {m[1]} and {m[2]}")
                elif A2 == 6: self.quartic_equation()
                elif A2 == 7: self.quintic_equation()
                elif A2 == 8: self.sextic_equation()
                elif A2 == 9: self.septic_equation()
                elif A2 == 10: self.octic_equation()
                elif A2 == 11: self.nonic_equation()
                elif A2 == 12: self.decic_equation()
                elif A2 == 13: self.matris()
            elif menu == 3:
                green("1.Perimeter and Area\n 2.Volume of 3D Shapes\n 3.Pythagorean Relation\n 4.Trigonometric Functions\n 5.Unit Conversion")
                c = int(input("Which ability do you want? "))
                time.sleep(0.2); os.system('clear')
                if c == 1: self.pa()
                elif c == 2: self.td()
                elif c == 3: self.fis()
                elif c == 4: self.tri()
                elif c == 5: self.unit()
            elif menu == 4:
                green("1.GCD,LCM\n 2.Prime Number Detection\n 3.Famous Patterns\n 4.Number Radix")
                d = int(input("Which ability do you want? "))
                time.sleep(0.2); os.system('clear')
                if d == 1: self.gcdlcm()
                elif d == 2: self.prime()
                elif d == 3: self.Fo()
                elif d == 4: self.mabna()
            elif menu == 5:
                green("1.Statistical Mean\n 2.Statistical Distributions\n 3.Make a Random Number\n 4.Number Guessing Game")
                e = int(input("Which ability do you want? "))
                time.sleep(0.2); os.system("clear")
                if e == 1: self.m()
                elif e == 2: self.Variate()
                elif e == 3: self.rn()
                elif e == 4: self.numg()
            elif menu == 6:
                green("1.Integral\n 2.Derivative")
                f = int(input("Which ability do you want? "))
                time.sleep(0.2); os.system("clear")
                if f == 1: self.Int()
                elif f == 2: self.moshtagh()
            elif menu == 7:
                green("1.Kinematics\n 2.Dynamics\n 3.Work, Energy & Power\n 4.Fluid Mechanics\n 5.Electricity & Magnetism\n 6.Heat & Thermodynamics\n 7.Light & Optics\n 8.Modern Physics\n 9.Physical Constants")
                ph = int(input("Which ability do you want? "))
                time.sleep(0.2); os.system("clear")
                if ph == 1: self._physics_kinematics_en()
                elif ph == 2: self._physics_dynamics_en()
                elif ph == 3: self._physics_work_energy_en()
                elif ph == 4: self._physics_fluids_en()
                elif ph == 5: self._physics_electricity_en()
                elif ph == 6: self._physics_heat_en()
                elif ph == 7: self._physics_optics_en()
                elif ph == 8: self._physics_modern_en()
                elif ph == 9: self._physics_constants_en()
            elif menu == 8:
                purple("Periodic Table")
                num = int(input("Enter element number (1-118): "))
                e = self.periodic.element_info(num)
                if e:
                    cyan("Element Information:")
                    yellow(f"Persian name: {e['fa']}")
                    yellow(f"English name: {e['en']}")
                    yellow(f"Symbol: {e['symbol']}")
                    yellow(f"Atomic number: {e['atomic']}")
                    yellow(f"Atomic mass: {e['mass']} g/mol")
                    yellow(f"Group: {e['group']}")
                    yellow(f"Period: {e['period']}")
                    yellow(f"Category: {e['category']}")
                    yellow(f"Melting point: {e['mp']} °C")
                    yellow(f"Boiling point: {e['bp']} °C")
                    yellow(f"Electron configuration: {e['config']}")
                    if e['year'] == 0:
                        yellow("Discovery year: Unknown (known since ancient times)")
                    else:
                        yellow(f"Discovery year: {e['year']}")
                else:
                    red("Element not found! Please enter number between 1 and 118")
            elif menu == 9:
                os.system("clear")
                purple("GOOD BYE!")
                break
            input("Enter to continue ")
            os.system("clear")