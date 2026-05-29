# =============================================================================
# Omega Calculator 10.0 - Module 10: Application Entry Point
# Author: Amirmahdi Ghorbani
# =============================================================================
# This is the main entry point for the Omega Calculator application.
# It handles language selection (English or Persian) and launches the
# appropriate user interface. This is the ONLY file that should be
# executed to run the application.
#
# Usage:
#   Run this file in Python:
#       python main.py
#
#   Or in Pydroid 3 / any Python environment:
#       Open main.py and press Run
#
# File Structure (all files must be in the same directory):
#   main.py              - This file (entry point)
#   color.py             - Terminal coloring module
#   math_base.py         - Mathematical utilities
#   equations.py         - Numerical equation solvers
#   calculus.py          - Derivatives and integrals
#   matrix_ops.py        - Matrix algebra operations
#   constants.py         - Physical constants
#   formulas.py          - Physics formulas library
#   periodic_table.py    - Periodic table database (118 elements)
#   english.py           - English user interface
#   persian.py           - Persian user interface
#
# Dependencies:
#   - color (local): Terminal text coloring
#   - os (standard library): Screen clearing
#   - english (local): CalculatorAppEN class
#   - persian (local): CalculatorAppFA class
#
# Last Modified: 2026-05-29
# Version: 10.0 (Modular Edition - Final)
# =============================================================================

from color import *
import os

# Import the two user interface classes
from english import CalculatorAppEN
from persian import CalculatorAppFA


# =============================================================================
# MAIN PROGRAM
# =============================================================================

if __name__ == "__main__":
    """
    Application startup: language selection and launch.

    The user is prompted to choose between English (A) and Persian (B).
    Based on the selection, the appropriate CalculatorApp class is
    instantiated and its run() method is called, which starts the
    main interactive menu loop.

    The screen is cleared after language selection to provide a clean
    starting interface for the main menu.
    """

    # Display language selection prompt
    cyan("Which language do you want?")
    yellow("  A) English\n   B) فارسی")
    zaban = input("")
    os.system("clear")

    # Route to the appropriate language interface
    if zaban == "A":
        app = CalculatorAppEN()
        app.run()
    elif zaban == "B":
        app = CalculatorAppFA()
        app.run()


# =============================================================================
# END OF OMEGA CALCULATOR 10.0
# =============================================================================
# Congratulations! You have reached the end of the Omega Calculator source.
#
# Project Summary:
#   - Developer: Amirmahdi Ghorbani (age 13)
#   - Experience: 9 months of self-taught Python programming
#   - Development Tool: Mid-range Android tablet with Pydroid 3
#   - Internet Access: None (fully offline development)
#   - Architecture: Modular Object-Oriented Design
#   - Total Modules: 10 Python files
#   - Total Lines: ~7,000 (including documentation)
#
# Features:
#   - 69 physics formulas across 8 subfields
#   - Polynomial equation solver (degrees 1-10)
#   - Numerical calculus (differentiation & integration)
#   - Matrix operations (add, multiply, determinant, inverse)
#   - Complete periodic table (118 elements, 11 properties each)
#   - 17 physical constants
#   - 10 statistical distributions
#   - Bilingual interface (English & Persian)
#   - Professional-grade documentation
#
# Version History:
#   v1.0  - Basic arithmetic (4 operations + powers/roots)
#   v8.0  - Object-oriented refactor
#   v9.0  - Professional documentation added
#   v10.0 - Modular architecture (current version)
# =============================================================================