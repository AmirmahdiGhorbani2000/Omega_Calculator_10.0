# =============================================================================
# Omega Calculator 10.0 - Module 3: Numerical Calculus
# Author: Amirmahdi Ghorbani
# =============================================================================
# This module provides numerical methods for differentiation and integration
# of user-defined mathematical functions. These operations form the calculus
# core of the Omega Calculator application.
#
# Methods:
#   - der(expr, x, h): Numerical derivative using central difference formula
#   - integral(expr, a, b, n): Numerical integration using Simpson's rule
#
# Numerical Methods Background:
#   - Central difference provides O(h²) accuracy by canceling first-order
#     error terms through symmetric sampling
#   - Simpson's rule provides O(h⁴) accuracy by fitting quadratic polynomials
#     through consecutive groups of three points
#
# Dependencies:
#   - math (standard library)
#   - math_base (local module): MathBase.make_function() for dynamic
#     function compilation from string expressions
#
# Last Modified: 2026-05-29
# Version: 10.0 (Modular Edition)
# =============================================================================

import math
from math_base import MathBase


class Calculus:
    """
    Numerical calculus operations: differentiation and integration.

    This class provides static methods for computing derivatives and
    definite integrals of functions defined by string expressions.
    Functions are dynamically compiled using MathBase.make_function()
    which safely evaluates user-provided mathematical expressions.
    """

    @staticmethod
    def der(expr, x, h=1e-6):
        """
        Computes the numerical derivative of a function at a point.

        Uses the central difference formula:
            f'(x) ≈ [f(x + h) - f(x - h)] / (2h)

        This method provides second-order accuracy (truncation error
        proportional to h²), which is significantly better than forward
        or backward differences (error proportional to h). The default
        step size of 1e-6 balances truncation error against floating-point
        roundoff error.

        Error Analysis:
            The central difference formula has:
            - Truncation error: O(h²) from the Taylor series expansion
              f(x+h) = f(x) + h·f'(x) + h²/2·f''(x) + h³/6·f'''(x) + ...
              When we compute [f(x+h) - f(x-h)]/(2h), the f''(x) terms
              cancel, leaving error proportional to h²·f'''(x)
            - Roundoff error: O(ε/h) where ε ≈ 2.2e-16 for double precision
              (machine epsilon)
            - Optimal h balances these: h_opt ≈ ε^(1/3) ≈ 6e-6

            For smooth functions and h = 1e-6, relative error is typically
            on the order of 1e-10 to 1e-8.

        Args:
            expr (str): Mathematical expression representing the function
                       f(x). Supports standard operators (+, -, *, /, **)
                       and math functions (sin, cos, tan, sqrt, log, exp).
                       Examples: "x**2", "sin(x)", "x**3 + 2*x - 1"
            x (float): The point at which to evaluate the derivative.
            h (float): Step size for the difference quotient.
                       Default: 1e-6. Values that are too small may
                       suffer from catastrophic cancellation; values
                       that are too large reduce accuracy.

        Returns:
            float: The approximate value of f'(x).

        Example:
            >>> Calculus.der("x**2", 3)
            6.000000000000227  # Exact: 6, error: ~2e-13
            >>> Calculus.der("sin(x)", math.pi/4)
            0.7071067811864529  # cos(π/4) = √2/2 ≈ 0.70710678
        """
        # Dynamically compile the mathematical expression into a callable
        # Python function. MathBase.make_function() handles the secure
        # evaluation of the expression string.
        f = MathBase.make_function(expr)

        # Apply the central difference formula:
        # f'(x) ≈ [f(x+h) - f(x-h)] / (2h)
        #
        # The symmetric sampling at x+h and x-h causes first-order error
        # terms (proportional to h) to cancel out, leaving the second-order
        # term as the dominant error source.
        return (f(x + h) - f(x - h)) / (2 * h)

    @staticmethod
    def integral(expr, a, b, n=1000):
        """
        Computes the definite integral of a function using Simpson's rule.

        Simpson's rule approximates ∫ₐᵇ f(x)dx by fitting quadratic
        polynomials through consecutive groups of three equally-spaced
        points. This yields fourth-order accuracy (error proportional
        to h⁴), making it significantly more precise than the trapezoidal
        rule (error proportional to h²) for the same number of function
        evaluations.

        Formula:
            ∫ₐᵇ f(x)dx ≈ (h/3)[f(x₀) + 4f(x₁) + 2f(x₂) + 4f(x₃) + ...
                                   + 2f(x_{n-2}) + 4f(x_{n-1}) + f(x_n)]

        where:
            - h = (b - a) / n is the width of each subinterval
            - n must be even (the method pairs up subintervals)
            - The coefficients follow the pattern: 1, 4, 2, 4, 2, ..., 4, 1

        The pattern of weights (1, 4, 2, 4, 2, ..., 4, 1) comes from
        integrating the Lagrange quadratic interpolant over each pair
        of subintervals.

        Args:
            expr (str): Mathematical expression representing the integrand
                       f(x). Supports standard operators and math functions.
                       Examples: "x**2", "sin(x)", "exp(-x**2)"
            a (float): Lower limit of integration.
            b (float): Upper limit of integration. Can be less than a
                      (the formula handles reversed limits correctly).
            n (int): Number of subintervals. Must be even for Simpson's
                    rule to work correctly (will be automatically adjusted
                    if odd). Default: 1000. Larger values increase accuracy
                    but require more function evaluations (n+1 evaluations).
                    For smooth functions, n=1000 typically yields accuracy
                    better than 1e-8.

        Returns:
            float: The approximate value of the definite integral ∫ₐᵇ f(x)dx.

        Accuracy:
            For sufficiently smooth functions (four continuous derivatives),
            the truncation error is bounded by:
                |Error| ≤ (b-a)⁵ / (180·n⁴) · max|f⁽⁴⁾(x)|
            where max|f⁽⁴⁾(x)| is the maximum absolute value of the fourth
            derivative on [a, b].

        Example:
            >>> Calculus.integral("x**2", 0, 1)
            0.3333333333333333  # Exact: 1/3
            >>> Calculus.integral("sin(x)", 0, math.pi)
            2.0  # Exact area under one arch of sine wave
            >>> Calculus.integral("exp(-x**2)", -1, 1)
            1.493648...  # Gaussian integral (no closed form)
        """
        # Dynamically compile the integrand expression into a callable
        # function using the secure expression evaluator
        f = MathBase.make_function(expr)

        # Simpson's rule requires an even number of subintervals to
        # properly form the pairs for quadratic interpolation.
        # If n is odd, increment by 1 to ensure correctness.
        if n % 2 != 0:
            n += 1

        # Calculate the width of each subinterval.
        # h = (b - a) / n
        h = (b - a) / n

        # Initialize the sum with the endpoint values.
        # Both f(x₀) and f(x_n) have coefficient 1 in Simpson's formula.
        total = f(a) + f(b)

        # Apply Simpson's rule weights to interior points:
        # - Odd-indexed points (1, 3, 5, ..., n-1): weight = 4
        # - Even-indexed interior points (2, 4, 6, ..., n-2): weight = 2
        #
        # The full pattern is: 1, 4, 2, 4, 2, ..., 4, 2, 4, 1
        #                      ↑                    ↑     ↑
        #                    f(x₀)              f(x_{n-1}) f(x_n)

        # Process odd-indexed points: x₁, x₃, x₅, ..., x_{n-1}
        # Each of these gets weight 4 in the formula
        for i in range(1, n, 2):
            total += 4 * f(a + i * h)

        # Process even-indexed interior points: x₂, x₄, x₆, ..., x_{n-2}
        # Each of these gets weight 2 in the formula
        # Note: x₀ and x_n are excluded (they were handled above)
        for i in range(2, n - 1, 2):
            total += 2 * f(a + i * h)

        # Final multiplication by h/3 per Simpson's formula.
        # The factor 1/3 comes from integrating the quadratic interpolant
        # over each pair of subintervals of width 2h.
        return (h / 3) * total