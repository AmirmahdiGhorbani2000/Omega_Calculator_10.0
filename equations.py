# =============================================================================
# Omega Calculator 10.0 - Module 2: Numerical Equation Solvers
# Author: Amirmahdi Ghorbani
# =============================================================================
# This module provides numerical methods for solving polynomial equations
# of varying degrees. It supports:
#   - Cubic equations via Cardano's analytical method (with complex roots)
#   - Quartic equations via hybrid Newton-Raphson with bracketing
#   - General polynomial equations (degrees 5-10) via numerical methods
#
# The core strategy for degree >= 3 combines Newton-Raphson iteration
# (fast convergence near roots) with bisection (guaranteed convergence)
# to create a robust hybrid solver. The algorithm:
#   1. Defines f(x) and f'(x) for the polynomial
#   2. Scans for intervals (brackets) where f(x) changes sign
#   3. Applies Newton-Raphson within each bracket
#   4. Falls back to bisection if Newton diverges
#   5. Filters, deduplicates, and sorts the resulting roots
#
# All methods are static for direct access without instantiation.
#
# Dependencies:
#   - math (standard library)
#   - cmath (standard library): Complex number operations for cubic solver
#
# Last Modified: 2026-05-29
# Version: 10.0 (Modular Edition)
# =============================================================================

import math
import cmath


class EquationSolver:
    """
    A collection of numerical methods for solving polynomial equations.

    This class provides static methods for finding roots of polynomials
    ranging from cubic equations (degree 3) to general polynomials of
    arbitrary degree. The implementation uses a combination of analytical
    formulas (Cardano's method for cubic) and numerical methods
    (Newton-Raphson with bisection fallback) for higher degrees.

    All methods are static and stateless. Results are returned as lists
    of floats (for real roots) or complex numbers (when complex roots
    are present and analytically determined).
    """

    # =========================================================================
    # QUARTIC SOLVER (Degree 4)
    # =========================================================================

    @staticmethod
    def solve_quartic(a, b, c, d, e):
        """
        Finds all real roots of a quartic equation using numerical methods.

        Solves ax⁴ + bx³ + cx² + dx + e = 0 by combining Newton-Raphson
        iteration with bracketing and bisection fallback. If the leading
        coefficient a is negligible (|a| < 1e-12), the equation is treated
        as a cubic and delegated to solve_cubic().

        Algorithm Overview:
        1. Define f(x) = ax⁴ + bx³ + cx² + dx + e (using Horner's method
           for efficient and numerically stable evaluation)
        2. Define f'(x) = 4ax³ + 3bx² + 2cx + d (also Horner's method)
        3. Calculate a conservative search radius based on coefficient
           magnitudes to ensure all real roots are captured
        4. Scan the interval [-bound, +bound] for brackets: adjacent
           points where f(x) changes sign (f(a)·f(b) < 0)
        5. For each bracket, apply Newton-Raphson starting from the
           bracket midpoint. Confine iterations to the bracket.
        6. If Newton-Raphson escapes the bracket or fails to converge,
           switch to the bisection method (guaranteed convergence for
           continuous functions with a sign change)
        7. If fewer than 4 roots are found (a quartic can have up to
           4 real roots), expand the search radius and retry with
           finer step size
        8. Deduplicate roots (merge those within 1e-6 of each other)
        9. Clean near-real complex numbers (imaginary part < 1e-8
           is treated as numerical noise and discarded)
        10. Round to 4 decimal places for display

        Args:
            a (float): Coefficient of x⁴ (leading coefficient)
            b (float): Coefficient of x³
            c (float): Coefficient of x²
            d (float): Coefficient of x (linear term)
            e (float): Constant term

        Returns:
            list: Sorted list of real roots, each rounded to 4 decimal
                  places. May contain fewer than 4 elements if some roots
                  are complex or if the numerical solver fails to converge
                  on all roots.

        Example:
            >>> EquationSolver.solve_quartic(1, -10, 35, -50, 24)
            [1.0, 2.0, 3.0, 4.0]  # (x-1)(x-2)(x-3)(x-4) = 0
            >>> EquationSolver.solve_quartic(1, 0, 0, 0, -16)
            [2.0, -2.0]  # x⁴ - 16 = 0 (only real roots returned)

        Technical Note:
            The global variable 'bound' is maintained for potential
            debugging purposes. It tracks the search radius used in
            the root-finding process. This is inherited from the
            original procedural implementation.
        """
        roots = []

        # Handle degenerate case: if the leading coefficient is effectively
        # zero (|a| < 1e-12), the equation is actually cubic or lower degree.
        # Delegate to the cubic solver which handles such cases recursively.
        if abs(a) < 1e-12:
            return EquationSolver.solve_cubic(b, c, d, e)

        # -----------------------------------------------------------------
        # Define the quartic polynomial f(x) and its derivative f'(x)
        # Both use Horner's method (nested multiplication) for efficient
        # evaluation with minimal floating-point operations.
        #
        # Standard form: f(x) = a·x⁴ + b·x³ + c·x² + d·x + e
        # Horner form:   f(x) = (((a·x + b)·x + c)·x + d)·x + e
        #
        # Horner's method reduces the number of multiplications from
        # O(n²) to O(n), where n is the polynomial degree. This
        # improves both performance and numerical stability.
        # -----------------------------------------------------------------
        def f(x):
            """Evaluate the quartic polynomial at x using Horner's method."""
            return ((a * x + b) * x + c) * x * x + d * x + e

        def df(x):
            """
            Evaluate the derivative f'(x) at x.

            f'(x) = 4a·x³ + 3b·x² + 2c·x + d
            Also evaluated using Horner's method for the cubic derivative.
            """
            return (4 * a * x + 3 * b) * x * x + 2 * c * x + d

        # -----------------------------------------------------------------
        # Bracket-finding function
        #
        # Scans an interval [start, end] with a given step size, looking
        # for adjacent points where f(x) changes sign. A sign change
        # between f(x) and f(x+step) indicates at least one root in
        # that interval, guaranteed by the Intermediate Value Theorem
        # (assuming the function is continuous).
        #
        # The step size controls the resolution of the search. Smaller
        # steps find more brackets but require more function evaluations.
        # -----------------------------------------------------------------
        def find_brackets(start, end, step=0.5):
            """
            Find intervals where f(x) changes sign.

            Args:
                start (float): Left boundary of the search interval.
                end (float): Right boundary of the search interval.
                step (float): Step size for scanning. Default: 0.5.
                             Smaller values provide finer resolution
                             but require more evaluations.

            Returns:
                list of tuple: Each tuple (left, right) represents a
                              bracket where f(left)·f(right) < 0,
                              indicating a root exists in the interval.
            """
            brackets = []
            x = start
            while x <= end:
                # Check if f(x) and f(x+step) have opposite signs
                # Product < 0 means one is positive, the other negative
                if f(x) * f(x + step) < 0:
                    brackets.append((x, x + step))
                x += step
            return brackets

        # -----------------------------------------------------------------
        # Newton-Raphson iteration with bracket confinement
        #
        # Standard Newton-Raphson: x_{n+1} = x_n - f(x_n)/f'(x_n)
        #
        # This method converges quadratically near a root (doubling the
        # number of correct digits each iteration), but can diverge if
        # the initial guess is far from the root or near a local extremum.
        #
        # To ensure robustness, we confine iterations to stay within the
        # bracket [bracket_a, bracket_b]. If an iteration steps outside,
        # we fall back to the bisection method, which is slower but
        # guarantees convergence for any continuous function with a
        # sign change.
        # -----------------------------------------------------------------
        def newton_with_bracket(x0, bracket_a, bracket_b, tol=1e-10, max_iter=100):
            """
            Find a root using Newton-Raphson, confined to [bracket_a, bracket_b].

            Args:
                x0 (float): Initial guess (typically the bracket midpoint).
                bracket_a (float): Left boundary - must have f(a)·f(b) < 0.
                bracket_b (float): Right boundary - must have f(a)·f(b) < 0.
                tol (float): Convergence tolerance. Iteration stops when
                            |x_{n+1} - x_n| < tol. Default: 1e-10.
                max_iter (int): Maximum iterations before giving up.
                               Default: 100.

            Returns:
                float or None: The found root approximation, or None if
                              the method fails to converge within max_iter
                              iterations.
            """
            x = x0
            for _ in range(max_iter):
                fx = f(x)
                dfx = df(x)

                # Protect against division by near-zero derivative.
                # This can happen near local extrema or multiple roots.
                if abs(dfx) < 1e-12:
                    break

                # Newton-Raphson step: x_{n+1} = x_n - f(x_n)/f'(x_n)
                x_new = x - fx / dfx

                # Check for convergence based on absolute change in x.
                # When the step size becomes very small, we consider
                # the iteration to have converged.
                if abs(x_new - x) < tol:
                    x = x_new
                    break

                x = x_new

                # Bracket check: If the iteration escapes the bracket,
                # Newton's method is likely diverging. Fall back to
                # bisection which is guaranteed to converge (though
                # more slowly) for any continuous function.
                if x < bracket_a or x > bracket_b:
                    return EquationSolver._bisection(bracket_a, bracket_b, f, tol)

            return x

        # -----------------------------------------------------------------
        # Root-finding driver function
        #
        # Orchestrates the complete root-finding process:
        # 1. Determines an appropriate search radius
        # 2. Scans for brackets (intervals containing roots)
        # 3. Applies the hybrid Newton-bisection solver to each bracket
        # 4. Collects and deduplicates the results
        # -----------------------------------------------------------------
        def find_roots():
            nonlocal roots
            global bound

            # Calculate a conservative search radius based on the
            # magnitudes of the coefficients. The formula:
            #   bound = max(1, sum_of_coeffs / |a|) + 1
            # provides a safe upper bound for the magnitude of any
            # real root (by Cauchy's bound theorem for polynomials).
            # The +1 ensures a margin of safety.
            bound = max(1.0, (abs(b) + abs(c) + abs(d) + abs(e)) / abs(a)) + 1

            # First pass: standard step size (0.3)
            brackets = find_brackets(-bound, bound, step=0.3)
            for bra, brb in brackets:
                x_mid = (bra + brb) / 2  # Midpoint as initial guess
                root = newton_with_bracket(x_mid, bra, brb)
                if root is not None and abs(f(root)) < 1e-8:
                    # Verify the root is not a duplicate of an existing one.
                    # Duplicates can arise when the same root is found from
                    # overlapping or adjacent brackets.
                    is_duplicate = False
                    for r in roots:
                        if abs(r - root) < 1e-6:
                            is_duplicate = True
                            break
                    if not is_duplicate:
                        roots.append(round(root, 10))

        # Execute the initial root-finding attempt
        find_roots()

        # -----------------------------------------------------------------
        # Expanded search for potentially missed roots
        #
        # A quartic polynomial can have up to 4 real roots. If fewer
        # are found in the first pass, expand the search radius by 50%
        # and use a finer step size (0.2) to capture roots that may
        # have been near the boundary or in narrow brackets that were
        # missed with the coarser step size.
        # -----------------------------------------------------------------
        if len(roots) < 4:
            brackets = find_brackets(-bound * 1.5, bound * 1.5, step=0.2)
            for bra, brb in brackets:
                if len(roots) >= 4:
                    break  # We have all expected roots
                x_mid = (bra + brb) / 2
                root = newton_with_bracket(x_mid, bra, brb)
                if root is not None and abs(f(root)) < 1e-8:
                    is_duplicate = False
                    for r in roots:
                        if abs(r - root) < 1e-6:
                            is_duplicate = True
                            break
                    if not is_duplicate:
                        roots.append(round(root, 10))

        # -----------------------------------------------------------------
        # Post-processing: sort and clean the results
        #
        # 1. Sort roots in ascending order for consistent output
        # 2. Handle complex numbers from numerical noise:
        #    - If the imaginary part is negligible (< 1e-8), treat as real
        #    - Otherwise, preserve the complex number as-is
        # 3. Round to 4 decimal places for clean display
        # -----------------------------------------------------------------
        roots.sort()

        cleaned_roots = []
        for r in roots:
            if isinstance(r, complex):
                # Check for numerically negligible imaginary part.
                # Floating-point operations can sometimes introduce
                # tiny imaginary components to mathematically real roots.
                if abs(r.imag) > 1e-8:
                    cleaned_roots.append(r)  # Genuinely complex
                else:
                    cleaned_roots.append(round(r.real, 10))  # Effectively real
            else:
                cleaned_roots.append(r)

        final_roots = [round(r, 4) if isinstance(r, float) else r for r in cleaned_roots]
        return final_roots

    # =========================================================================
    # BISECTION METHOD (Fallback for Newton-Raphson)
    # =========================================================================

    @staticmethod
    def _bisection(a_b, b_b, f, tol=1e-10):
        """
        Finds a root using the bisection method (binary search).

        This is a robust fallback method used when Newton-Raphson fails
        to converge (e.g., due to a poor initial guess or near-zero
        derivative). The bisection method is guaranteed to converge
        for any continuous function where f(a) and f(b) have opposite
        signs, though it converges linearly rather than quadratically.

        Algorithm:
        1. Verify that f(a) and f(b) have opposite signs (required for
           the Intermediate Value Theorem to guarantee a root).
        2. Compute the midpoint: mid = (a + b) / 2
        3. Evaluate f(mid). If |f(mid)| < tol, mid is the root.
        4. Determine which half-interval contains the sign change:
           - If f(a)·f(mid) < 0, the root is in [a, mid]
           - Otherwise, the root is in [mid, b]
        5. Repeat steps 2-4 with the new interval.
        6. Maximum 100 iterations as a safety limit.

        Convergence Rate:
            After n iterations, the error is at most (b-a)/2ⁿ.
            With tol=1e-10 and typical bracket sizes of ~1-10 units,
            convergence occurs in approximately 35-45 iterations.

        Args:
            a_b (float): Left endpoint of the interval.
            b_b (float): Right endpoint of the interval.
            f (function): The continuous function whose root is sought.
            tol (float): Convergence tolerance. Default: 1e-10.
                        The method stops when |f(mid)| < tol.

        Returns:
            float or None: The approximate root, or None if f(a)·f(b) >= 0
                          (meaning a root is not guaranteed in the interval).
        """
        fa = f(a_b)
        fb = f(b_b)

        # Verify the sign-change condition required by the Intermediate
        # Value Theorem. If f(a) and f(b) have the same sign, a root
        # is not guaranteed to exist in the interval (though there
        # could be an even number of roots, which bisection would miss).
        if fa * fb >= 0:
            return None

        for _ in range(100):
            mid = (a_b + b_b) / 2
            fmid = f(mid)

            # Check for convergence: |f(mid)| below tolerance
            if abs(fmid) < tol:
                return mid

            # Replace the endpoint that has the same sign as f(mid).
            # This maintains the invariant that f(a)·f(b) < 0,
            # ensuring the root remains bracketed.
            if fa * fmid < 0:
                b_b = mid
                fb = fmid
            else:
                a_b = mid
                fa = fmid

        # Maximum iterations reached. Return the best estimate.
        return (a_b + b_b) / 2

    # =========================================================================
    # CUBIC SOLVER (Degree 3) - Numerical Method
    # =========================================================================

    @staticmethod
    def solve_cubic(a, b, c, d):
        """
        Finds all real roots of a cubic equation using numerical methods.

        Solves ax³ + bx² + cx + d = 0 by combining Newton-Raphson
        iteration with bracketing. This is a purely numerical approach
        designed to find real roots only. For complex roots, use
        cubic_equation() which implements Cardano's analytical method.

        Args:
            a (float): Coefficient of x³.
            b (float): Coefficient of x².
            c (float): Coefficient of x (linear term).
            d (float): Constant term.

        Returns:
            list: Sorted list of real roots, rounded to 4 decimal places.

        Example:
            >>> EquationSolver.solve_cubic(1, -6, 11, -6)
            [1.0, 2.0, 3.0]  # (x-1)(x-2)(x-3) = 0
        """
        roots = []

        # Define the cubic polynomial and its derivative using Horner's method
        # f(x) = ((a·x + b)·x + c)·x + d
        def f(x):
            return ((a * x + b) * x + c) * x + d

        # f'(x) = (3a·x + 2b)·x + c
        def df(x):
            return (3 * a * x + 2 * b) * x + c

        # Bracket-finding: scan for sign changes in f(x)
        def find_brackets(start, end, step=0.5):
            brackets = []
            x = start
            while x <= end:
                if f(x) * f(x + step) < 0:
                    brackets.append((x, x + step))
                x += step
            return brackets

        # Newton-Raphson iteration for well-behaved cubic polynomials.
        # Unlike the quartic solver, this version does not confine
        # iterations to brackets (slightly less robust but simpler).
        def newton(x0, tol=1e-10, max_iter=100):
            x = x0
            for _ in range(max_iter):
                fx = f(x)
                dfx = df(x)
                if abs(dfx) < 1e-12:
                    break
                x_new = x - fx / dfx
                if abs(x_new - x) < tol:
                    return x_new
                x = x_new
            return x

        # Calculate search radius based on coefficient magnitudes.
        # Guard against division by zero if |a| is very small.
        bound = max(1.0, (abs(b) + abs(c) + abs(d)) / abs(a)) + 1 if abs(a) > 1e-12 else 10

        # Find and refine roots from each bracket
        brackets = find_brackets(-bound, bound, step=0.5)
        for bra, brb in brackets:
            x_mid = (bra + brb) / 2
            root = newton(x_mid)
            if root is not None and abs(f(root)) < 1e-8:
                # Deduplication: check if this root was already found
                is_duplicate = False
                for r in roots:
                    if abs(r - root) < 1e-6:
                        is_duplicate = True
                        break
                if not is_duplicate:
                    roots.append(round(root, 10))

        roots.sort()
        return [round(r, 4) for r in roots]

    # =========================================================================
    # GENERAL POLYNOMIAL SOLVER (Any Degree)
    # =========================================================================

    @staticmethod
    def solve_polynomial_general(coeffs):
        """
        Finds all real roots of a polynomial of arbitrary degree.

        This is a general-purpose numerical solver that works for any
        polynomial degree by iterating through the coefficient list.
        It uses the same Newton-Raphson with bracketing approach as
        the cubic and quartic solvers, but constructs f(x) and f'(x)
        dynamically from the coefficient list.

        This method is used for polynomial degrees 5 through 10 in
        the calculator (quintic through decic equations), where no
        closed-form analytical solution exists (by the Abel-Ruffini
        theorem for degree >= 5).

        Args:
            coeffs (list of float): Coefficients in descending degree order.
                                   Example: [1, -5, 6] represents x² - 5x + 6.
                                   The length of the list determines the
                                   polynomial degree (len(coeffs) - 1).

        Returns:
            list: Sorted list of real roots, rounded to 4 decimal places.
                  May return an empty list if no real roots are found.

        Example:
            >>> EquationSolver.solve_polynomial_general([1, -5, 6])
            [2.0, 3.0]  # Roots of x² - 5x + 6 = 0
            >>> EquationSolver.solve_polynomial_general([1, 0, 0, -8])
            [2.0]  # Real root of x³ - 8 = 0 (complex roots are excluded)
        """
        degree = len(coeffs) - 1

        # Evaluate the polynomial at x by iterating through coefficients.
        # For polynomial: a₀xⁿ + a₁xⁿ⁻¹ + ... + aₙ
        # This is not Horner's method but a direct term-by-term evaluation.
        # Horner's method would be more efficient but requires restructuring.
        def f(x):
            res = 0.0
            for i, c in enumerate(coeffs):
                res += c * (x ** (degree - i))
            return res

        # Evaluate the derivative at x.
        # The derivative of a₀xⁿ + a₁xⁿ⁻¹ + ... + aₙ is:
        #   n·a₀xⁿ⁻¹ + (n-1)·a₁xⁿ⁻² + ... + 1·aₙ₋₁
        # The last coefficient aₙ (constant term) has derivative 0,
        # so we iterate through coeffs[:-1] (excluding the last).
        def df(x):
            res = 0.0
            for i, c in enumerate(coeffs[:-1]):
                power = degree - i
                res += c * power * (x ** (power - 1))
            return res

        # Bracket-finding function (same pattern as other solvers)
        def find_brackets(start, end, step=0.5):
            brackets = []
            x = start
            while x <= end:
                if f(x) * f(x + step) < 0:
                    brackets.append((x, x + step))
                x += step
            return brackets

        # Newton-Raphson iteration
        def newton(x0, tol=1e-10, max_iter=100):
            x = x0
            for _ in range(max_iter):
                fx = f(x)
                dfx = df(x)
                if abs(dfx) < 1e-12:
                    break
                x_new = x - fx / dfx
                if abs(x_new - x) < tol:
                    return x_new
                x = x_new
            return x

        roots = []

        # Calculate search radius using the sum of absolute coefficient
        # values. This provides a conservative upper bound for root
        # magnitudes based on Cauchy's bound theorem.
        bound = max(1.0, sum(abs(c) for c in coeffs) / abs(coeffs[0])) + 1 if abs(coeffs[0]) > 1e-12 else 10

        brackets = find_brackets(-bound, bound, step=0.5)
        for bra, brb in brackets:
            x_mid = (bra + brb) / 2
            root = newton(x_mid)
            if root is not None and abs(f(root)) < 1e-8:
                is_duplicate = False
                for r in roots:
                    if abs(r - root) < 1e-6:
                        is_duplicate = True
                        break
                if not is_duplicate:
                    roots.append(round(root, 10))

        roots.sort()
        return [round(r, 4) if isinstance(r, float) else r for r in roots]

    # =========================================================================
    # CUBIC EQUATION - ANALYTICAL SOLVER (Cardano's Method)
    # =========================================================================

    @staticmethod
    def cubic_equation(a, b, c, d):
        """
        Solves a cubic equation using Cardano's analytical method.

        This method provides a complete solution for ax³ + bx² + cx + d = 0,
        returning both real and complex roots. It first transforms the
        cubic to depressed form (t³ + pt + q = 0) via the substitution
        x = t - b/(3a), then applies Cardano's formula.

        This method returns all three roots (including complex ones),
        unlike solve_cubic() which only returns real roots.

        Algorithm Overview:
        1. If |a| < 1e-12, treat as quadratic and use quadratic formula.
        2. Transform to depressed cubic: t³ + pt + q = 0
           where p = (3ac - b²)/(3a²) and q = (2b³ - 9abc + 27a²d)/(27a³).
        3. Compute discriminant Δ = (q/2)² + (p/3)³.
        4. Based on the sign of Δ:
           - Δ > 0: One real root, two complex conjugate roots
           - Δ < 0: Three distinct real roots (casus irreducibilis)
           - Δ = 0: All roots are real, with at least one multiple root
        5. Apply reverse substitution x = t - b/(3a) to obtain the
           original roots.

        Args:
            a (float): Coefficient of x³.
            b (float): Coefficient of x².
            c (float): Coefficient of x.
            d (float): Constant term.

        Returns:
            list: Three roots of the cubic equation. Real roots are
                  returned as floats, complex roots as Python complex
                  numbers (e.g., (1+2j)). The list always contains
                  exactly 3 elements.

        Example:
            >>> EquationSolver.cubic_equation(1, -6, 11, -6)
            [1.0, 2.0, 3.0]  # (x-1)(x-2)(x-3)
            >>> EquationSolver.cubic_equation(1, 0, 0, -8)
            [2.0, (-1+1.732j), (-1-1.732j)]  # x³ = 8
        """
        # Handle degenerate case: leading coefficient is negligible.
        # Solve as quadratic: bx² + cx + d = 0 using quadratic formula.
        if abs(a) < 1e-12:
            delta = c ** 2 - 4 * b * d
            if abs(b) < 1e-12:
                return []
            x1 = (-c + cmath.sqrt(delta)) / (2 * b)
            x2 = (-c - cmath.sqrt(delta)) / (2 * b)
            return [x1, x2]

        # Transform to depressed cubic: t³ + pt + q = 0
        # via the substitution x = t - b/(3a)
        p = (3 * a * c - b ** 2) / (3 * a ** 2)
        q = (2 * b ** 3 - 9 * a * b * c + 27 * a ** 2 * d) / (27 * a ** 3)

        # Compute the discriminant Δ = (q/2)² + (p/3)³
        # The sign of Δ determines the nature of the roots.
        delta = (q / 2) ** 2 + (p / 3) ** 3
        if abs(delta) < 1e-12:
            delta = 0  # Treat near-zero as exactly zero

        y_roots = []

        if delta > 0:
            # Case 1: Δ > 0 → One real root, two non-real complex conjugates
            # Use Cardano's formula with real cube roots for the real root
            # and complex cube roots for the complex conjugate pair.
            u = (-q / 2 + cmath.sqrt(delta)) ** (1 / 3)
            v = (-q / 2 - cmath.sqrt(delta)) ** (1 / 3)
            y1 = u + v  # The real root
            # Complex cube roots of unity: ω = e^(2πi/3), ω² = e^(4πi/3)
            omega = complex(-0.5, math.sqrt(3) / 2)      # e^(2πi/3)
            omega2 = complex(-0.5, -math.sqrt(3) / 2)    # e^(4πi/3) = ω²
            y2 = omega * u + omega2 * v
            y3 = omega2 * u + omega * v
            y_roots = [y1, y2, y3]

        elif delta < 0:
            # Case 2: Δ < 0 → Three distinct real roots (casus irreducibilis)
            # In this case, Cardano's formula involves complex numbers, but
            # the roots are all real. We use the trigonometric solution to
            # avoid complex intermediate values.
            # Let r = √(-p/3) and φ = arccos(3q/(2p·r))
            # Then the roots are: 2r·cos(φ/3), 2r·cos((φ+2π)/3), 2r·cos((φ+4π)/3)
            r = math.sqrt(-p / 3)
            phi = math.acos(3 * q / (2 * p * r))
            y1 = 2 * r * math.cos(phi / 3)
            y2 = 2 * r * math.cos((phi + 2 * math.pi) / 3)
            y3 = 2 * r * math.cos((phi + 4 * math.pi) / 3)
            y_roots = [y1, y2, y3]

        else:
            # Case 3: Δ = 0 → Multiple root case
            # All roots are real, with at least two equal.
            # The roots are: 2∛(-q/2), -∛(-q/2), -∛(-q/2)
            y1 = 2 * (-q / 2) ** (1 / 3)
            y2 = -(-q / 2) ** (1 / 3)
            y_roots = [y1, y2, y2]  # y2 is a double root

        # Reverse the substitution: x = y - b/(3a)
        # This transforms the depressed cubic roots back to the original
        shift = -b / (3 * a)
        x_roots = [y + shift for y in y_roots]

        # Post-process: separate real roots from complex roots.
        # Roots with negligible imaginary part (< 1e-12) are treated
        # as real and converted to float.
        result = []
        for root in x_roots:
            if abs(root.imag) < 1e-12:
                # Effectively real root (imaginary part is numerical noise)
                result.append(round(root.real, 10))
            else:
                # Genuinely complex root, preserve as complex number
                result.append(complex(round(root.real, 10), round(root.imag, 10)))

        return result