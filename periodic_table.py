# =============================================================================
# Omega Calculator 10.0 - Module 7: Periodic Table Database
# Author: Amirmahdi Ghorbani
# =============================================================================
# This module contains the complete periodic table database with all 118
# confirmed chemical elements. Each element entry includes 11 properties
# in both Persian and English for bilingual display support.
#
# Properties per element:
#   - fa: Persian name (e.g., "هیدروژن", "طلا")
#   - en: English name (e.g., "Hydrogen", "Gold")
#   - symbol: Chemical symbol, 1-3 characters (e.g., "H", "Au", "Uup")
#   - atomic: Atomic number = number of protons (1-118)
#   - mass: Standard atomic weight in g/mol (IUPAC values)
#   - group: Periodic table group number (1-18)
#   - period: Periodic table period number (1-7)
#   - category: Classification in Persian (فلز قلیایی, گاز نجیب, etc.)
#   - mp: Melting point in degrees Celsius (0 if unknown)
#   - bp: Boiling point in degrees Celsius (0 if unknown)
#   - config: Electron configuration using noble gas notation
#   - year: Year of discovery (0 if known since antiquity)
#
# Data Organization:
#   Elements are stored in a class-level dictionary with atomic number
#   as the key, enabling O(1) lookup. The data is organized by periods
#   (rows of the periodic table) for readability.
#
# Sources:
#   - Atomic masses: IUPAC standard atomic weights
#   - Electron configurations: Aufbau principle (Madelung rule)
#   - Discovery years: IUPAC and historical records
#
# Dependencies:
#   None (pure data class, no imports required)
#
# Last Modified: 2026-05-29
# Version: 10.0 (Modular Edition)
# =============================================================================


class PeriodicTable:
    """
    Complete periodic table database containing all 118 confirmed elements.

    Provides a single static method element_info(num) for O(1) lookup
    of element data by atomic number. All element data is stored as a
    class-level dictionary with 11 properties per element, enabling
    bilingual (Persian/English) display.
    """

    # =========================================================================
    # Complete element database: 118 elements organized by period
    # Key: atomic number (int, 1-118)
    # Value: dict with 11 properties
    # =========================================================================
    _elements = {
        # =====================================================================
        # Period 1 (Elements 1-2): Hydrogen and Helium
        # The simplest elements, filling the 1s orbital
        # =====================================================================
        1: {"fa": "هیدروژن", "en": "Hydrogen", "symbol": "H", "atomic": 1, "mass": 1.008, "group": 1, "period": 1, "category": "غیرفلز", "mp": -259.1, "bp": -252.9, "config": "1s¹", "year": 1766},
        2: {"fa": "هلیوم", "en": "Helium", "symbol": "He", "atomic": 2, "mass": 4.0026, "group": 18, "period": 1, "category": "گاز نجیب", "mp": -272.2, "bp": -268.9, "config": "1s²", "year": 1868},

        # =====================================================================
        # Period 2 (Elements 3-10): Filling 2s and 2p orbitals
        # =====================================================================
        3: {"fa": "لیتیوم", "en": "Lithium", "symbol": "Li", "atomic": 3, "mass": 6.94, "group": 1, "period": 2, "category": "فلز قلیایی", "mp": 180.5, "bp": 1342, "config": "[He] 2s¹", "year": 1817},
        4: {"fa": "بریلیوم", "en": "Beryllium", "symbol": "Be", "atomic": 4, "mass": 9.012, "group": 2, "period": 2, "category": "فلز قلیایی خاکی", "mp": 1287, "bp": 2471, "config": "[He] 2s²", "year": 1798},
        5: {"fa": "بور", "en": "Boron", "symbol": "B", "atomic": 5, "mass": 10.81, "group": 13, "period": 2, "category": "شبه‌فلز", "mp": 2076, "bp": 3927, "config": "[He] 2s² 2p¹", "year": 1808},
        6: {"fa": "کربن", "en": "Carbon", "symbol": "C", "atomic": 6, "mass": 12.011, "group": 14, "period": 2, "category": "نافلز", "mp": 3550, "bp": 4827, "config": "[He] 2s² 2p²", "year": 0},
        7: {"fa": "نیتروژن", "en": "Nitrogen", "symbol": "N", "atomic": 7, "mass": 14.007, "group": 15, "period": 2, "category": "نافلز", "mp": -210, "bp": -195.8, "config": "[He] 2s² 2p³", "year": 1772},
        8: {"fa": "اکسیژن", "en": "Oxygen", "symbol": "O", "atomic": 8, "mass": 15.999, "group": 16, "period": 2, "category": "نافلز", "mp": -218.8, "bp": -183, "config": "[He] 2s² 2p⁴", "year": 1774},
        9: {"fa": "فلوئور", "en": "Fluorine", "symbol": "F", "atomic": 9, "mass": 18.998, "group": 17, "period": 2, "category": "هالوژن", "mp": -219.6, "bp": -188.1, "config": "[He] 2s² 2p⁵", "year": 1886},
        10: {"fa": "نئون", "en": "Neon", "symbol": "Ne", "atomic": 10, "mass": 20.18, "group": 18, "period": 2, "category": "گاز نجیب", "mp": -248.6, "bp": -246.1, "config": "[He] 2s² 2p⁶", "year": 1898},

        # =====================================================================
        # Period 3 (Elements 11-18): Filling 3s and 3p orbitals
        # =====================================================================
        11: {"fa": "سدیم", "en": "Sodium", "symbol": "Na", "atomic": 11, "mass": 22.99, "group": 1, "period": 3, "category": "فلز قلیایی", "mp": 97.8, "bp": 883, "config": "[Ne] 3s¹", "year": 1807},
        12: {"fa": "منیزیم", "en": "Magnesium", "symbol": "Mg", "atomic": 12, "mass": 24.305, "group": 2, "period": 3, "category": "فلز قلیایی خاکی", "mp": 650, "bp": 1091, "config": "[Ne] 3s²", "year": 1755},
        13: {"fa": "آلومینیوم", "en": "Aluminium", "symbol": "Al", "atomic": 13, "mass": 26.982, "group": 13, "period": 3, "category": "فلز پس‌گذار", "mp": 660.3, "bp": 2470, "config": "[Ne] 3s² 3p¹", "year": 1825},
        14: {"fa": "سیلیسیم", "en": "Silicon", "symbol": "Si", "atomic": 14, "mass": 28.086, "group": 14, "period": 3, "category": "شبه‌فلز", "mp": 1414, "bp": 3265, "config": "[Ne] 3s² 3p²", "year": 1824},
        15: {"fa": "فسفر", "en": "Phosphorus", "symbol": "P", "atomic": 15, "mass": 30.974, "group": 15, "period": 3, "category": "غیرفلز", "mp": 44.1, "bp": 280, "config": "[Ne] 3s² 3p³", "year": 1669},
        16: {"fa": "گوگرد", "en": "Sulfur", "symbol": "S", "atomic": 16, "mass": 32.06, "group": 16, "period": 3, "category": "غیرفلز", "mp": 115.2, "bp": 444.6, "config": "[Ne] 3s² 3p⁴", "year": 0},
        17: {"fa": "کلر", "en": "Chlorine", "symbol": "Cl", "atomic": 17, "mass": 35.45, "group": 17, "period": 3, "category": "هالوژن", "mp": -101.5, "bp": -34, "config": "[Ne] 3s² 3p⁵", "year": 1774},
        18: {"fa": "آرگون", "en": "Argon", "symbol": "Ar", "atomic": 18, "mass": 39.95, "group": 18, "period": 3, "category": "گاز نجیب", "mp": -189.4, "bp": -185.8, "config": "[Ne] 3s² 3p⁶", "year": 1894},

        # =====================================================================
        # Period 4 (Elements 19-36): First transition metal series (3d)
        # =====================================================================
        19: {"fa": "پتاسیم", "en": "Potassium", "symbol": "K", "atomic": 19, "mass": 39.098, "group": 1, "period": 4, "category": "فلز قلیایی", "mp": 63.5, "bp": 759, "config": "[Ar] 4s¹", "year": 1807},
        20: {"fa": "کلسیم", "en": "Calcium", "symbol": "Ca", "atomic": 20, "mass": 40.078, "group": 2, "period": 4, "category": "فلز قلیایی خاکی", "mp": 842, "bp": 1484, "config": "[Ar] 4s²", "year": 0},
        21: {"fa": "اسکاندیم", "en": "Scandium", "symbol": "Sc", "atomic": 21, "mass": 44.956, "group": 3, "period": 4, "category": "فلز واسطه", "mp": 1541, "bp": 2836, "config": "[Ar] 3d¹ 4s²", "year": 1879},
        22: {"fa": "تیتانیم", "en": "Titanium", "symbol": "Ti", "atomic": 22, "mass": 47.867, "group": 4, "period": 4, "category": "فلز واسطه", "mp": 1668, "bp": 3287, "config": "[Ar] 3d² 4s²", "year": 1791},
        23: {"fa": "وانادیم", "en": "Vanadium", "symbol": "V", "atomic": 23, "mass": 50.942, "group": 5, "period": 4, "category": "فلز واسطه", "mp": 1910, "bp": 3407, "config": "[Ar] 3d³ 4s²", "year": 1801},
        24: {"fa": "کروم", "en": "Chromium", "symbol": "Cr", "atomic": 24, "mass": 51.996, "group": 6, "period": 4, "category": "فلز واسطه", "mp": 1907, "bp": 2671, "config": "[Ar] 3d⁵ 4s¹", "year": 1797},
        25: {"fa": "منگنز", "en": "Manganese", "symbol": "Mn", "atomic": 25, "mass": 54.938, "group": 7, "period": 4, "category": "فلز واسطه", "mp": 1246, "bp": 2061, "config": "[Ar] 3d⁵ 4s²", "year": 1774},
        26: {"fa": "آهن", "en": "Iron", "symbol": "Fe", "atomic": 26, "mass": 55.845, "group": 8, "period": 4, "category": "فلز واسطه", "mp": 1538, "bp": 2861, "config": "[Ar] 3d⁶ 4s²", "year": 0},
        27: {"fa": "کبالت", "en": "Cobalt", "symbol": "Co", "atomic": 27, "mass": 58.933, "group": 9, "period": 4, "category": "فلز واسطه", "mp": 1495, "bp": 2927, "config": "[Ar] 3d⁷ 4s²", "year": 1735},
        28: {"fa": "نیکل", "en": "Nickel", "symbol": "Ni", "atomic": 28, "mass": 58.693, "group": 10, "period": 4, "category": "فلز واسطه", "mp": 1455, "bp": 2913, "config": "[Ar] 3d⁸ 4s²", "year": 1751},
        29: {"fa": "مس", "en": "Copper", "symbol": "Cu", "atomic": 29, "mass": 63.546, "group": 11, "period": 4, "category": "فلز واسطه", "mp": 1085, "bp": 2562, "config": "[Ar] 3d¹⁰ 4s¹", "year": 0},
        30: {"fa": "روی", "en": "Zinc", "symbol": "Zn", "atomic": 30, "mass": 65.38, "group": 12, "period": 4, "category": "فلز پس‌گذار", "mp": 419.5, "bp": 907, "config": "[Ar] 3d¹⁰ 4s²", "year": 0},
        31: {"fa": "گالیم", "en": "Gallium", "symbol": "Ga", "atomic": 31, "mass": 69.723, "group": 13, "period": 4, "category": "فلز پس‌گذار", "mp": 29.8, "bp": 2400, "config": "[Ar] 3d¹⁰ 4s² 4p¹", "year": 1875},
        32: {"fa": "ژرمانیم", "en": "Germanium", "symbol": "Ge", "atomic": 32, "mass": 72.63, "group": 14, "period": 4, "category": "شبه‌فلز", "mp": 938.3, "bp": 2833, "config": "[Ar] 3d¹⁰ 4s² 4p²", "year": 1886},
        33: {"fa": "آرسنیک", "en": "Arsenic", "symbol": "As", "atomic": 33, "mass": 74.922, "group": 15, "period": 4, "category": "شبه‌فلز", "mp": 817, "bp": 614, "config": "[Ar] 3d¹⁰ 4s² 4p³", "year": 0},
        34: {"fa": "سلنیم", "en": "Selenium", "symbol": "Se", "atomic": 34, "mass": 78.96, "group": 16, "period": 4, "category": "غیرفلز", "mp": 221, "bp": 685, "config": "[Ar] 3d¹⁰ 4s² 4p⁴", "year": 1817},
        35: {"fa": "برم", "en": "Bromine", "symbol": "Br", "atomic": 35, "mass": 79.904, "group": 17, "period": 4, "category": "هالوژن", "mp": -7.2, "bp": 58.8, "config": "[Ar] 3d¹⁰ 4s² 4p⁵", "year": 1826},
        36: {"fa": "کریپتون", "en": "Krypton", "symbol": "Kr", "atomic": 36, "mass": 83.798, "group": 18, "period": 4, "category": "گاز نجیب", "mp": -157.4, "bp": -153.2, "config": "[Ar] 3d¹⁰ 4s² 4p⁶", "year": 1898},

        # =====================================================================
        # Period 5 (Elements 37-54): Second transition metal series (4d)
        # =====================================================================
        37: {"fa": "روبیدیم", "en": "Rubidium", "symbol": "Rb", "atomic": 37, "mass": 85.468, "group": 1, "period": 5, "category": "فلز قلیایی", "mp": 39.3, "bp": 688, "config": "[Kr] 5s¹", "year": 1861},
        38: {"fa": "استرانسیم", "en": "Strontium", "symbol": "Sr", "atomic": 38, "mass": 87.62, "group": 2, "period": 5, "category": "فلز قلیایی خاکی", "mp": 777, "bp": 1382, "config": "[Kr] 5s²", "year": 1790},
        39: {"fa": "ایتریم", "en": "Yttrium", "symbol": "Y", "atomic": 39, "mass": 88.906, "group": 3, "period": 5, "category": "فلز واسطه", "mp": 1526, "bp": 2930, "config": "[Kr] 4d¹ 5s²", "year": 1794},
        40: {"fa": "زیرکونیم", "en": "Zirconium", "symbol": "Zr", "atomic": 40, "mass": 91.224, "group": 4, "period": 5, "category": "فلز واسطه", "mp": 1855, "bp": 4409, "config": "[Kr] 4d² 5s²", "year": 1789},
        41: {"fa": "نیوبیم", "en": "Niobium", "symbol": "Nb", "atomic": 41, "mass": 92.906, "group": 5, "period": 5, "category": "فلز واسطه", "mp": 2477, "bp": 4744, "config": "[Kr] 4d⁴ 5s¹", "year": 1801},
        42: {"fa": "مولیبدن", "en": "Molybdenum", "symbol": "Mo", "atomic": 42, "mass": 95.95, "group": 6, "period": 5, "category": "فلز واسطه", "mp": 2623, "bp": 4639, "config": "[Kr] 4d⁵ 5s¹", "year": 1778},
        43: {"fa": "تکنسیوم", "en": "Technetium", "symbol": "Tc", "atomic": 43, "mass": 98, "group": 7, "period": 5, "category": "فلز واسطه", "mp": 2157, "bp": 4265, "config": "[Kr] 4d⁵ 5s²", "year": 1937},
        44: {"fa": "روتنیوم", "en": "Ruthenium", "symbol": "Ru", "atomic": 44, "mass": 101.07, "group": 8, "period": 5, "category": "فلز واسطه", "mp": 2334, "bp": 4150, "config": "[Kr] 4d⁷ 5s¹", "year": 1844},
        45: {"fa": "رودیوم", "en": "Rhodium", "symbol": "Rh", "atomic": 45, "mass": 102.91, "group": 9, "period": 5, "category": "فلز واسطه", "mp": 1964, "bp": 3695, "config": "[Kr] 4d⁸ 5s¹", "year": 1803},
        46: {"fa": "پالادیم", "en": "Palladium", "symbol": "Pd", "atomic": 46, "mass": 106.42, "group": 10, "period": 5, "category": "فلز واسطه", "mp": 1555, "bp": 2963, "config": "[Kr] 4d¹⁰", "year": 1803},
        47: {"fa": "نقره", "en": "Silver", "symbol": "Ag", "atomic": 47, "mass": 107.87, "group": 11, "period": 5, "category": "فلز واسطه", "mp": 961.8, "bp": 2162, "config": "[Kr] 4d¹⁰ 5s¹", "year": 0},
        48: {"fa": "کادمیم", "en": "Cadmium", "symbol": "Cd", "atomic": 48, "mass": 112.41, "group": 12, "period": 5, "category": "فلز واسطه", "mp": 321.1, "bp": 767, "config": "[Kr] 4d¹⁰ 5s²", "year": 1817},
        49: {"fa": "ایندیم", "en": "Indium", "symbol": "In", "atomic": 49, "mass": 114.82, "group": 13, "period": 5, "category": "فلز پس‌گذار", "mp": 156.6, "bp": 2072, "config": "[Kr] 4d¹⁰ 5s² 5p¹", "year": 1863},
        50: {"fa": "قلع", "en": "Tin", "symbol": "Sn", "atomic": 50, "mass": 118.71, "group": 14, "period": 5, "category": "فلز پس‌گذار", "mp": 231.9, "bp": 2602, "config": "[Kr] 4d¹⁰ 5s² 5p²", "year": 0},
        51: {"fa": "آنتیموان", "en": "Antimony", "symbol": "Sb", "atomic": 51, "mass": 121.76, "group": 15, "period": 5, "category": "شبه‌فلز", "mp": 630.6, "bp": 1587, "config": "[Kr] 4d¹⁰ 5s² 5p³", "year": 0},
        52: {"fa": "تلوریم", "en": "Tellurium", "symbol": "Te", "atomic": 52, "mass": 127.6, "group": 16, "period": 5, "category": "شبه‌فلز", "mp": 449.5, "bp": 988, "config": "[Kr] 4d¹⁰ 5s² 5p⁴", "year": 1782},
        53: {"fa": "ید", "en": "Iodine", "symbol": "I", "atomic": 53, "mass": 126.9, "group": 17, "period": 5, "category": "هالوژن", "mp": 113.7, "bp": 184.3, "config": "[Kr] 4d¹⁰ 5s² 5p⁵", "year": 1811},
        54: {"fa": "زنون", "en": "Xenon", "symbol": "Xe", "atomic": 54, "mass": 131.29, "group": 18, "period": 5, "category": "گاز نجیب", "mp": -111.8, "bp": -108.1, "config": "[Kr] 4d¹⁰ 5s² 5p⁶", "year": 1898},

        # =====================================================================
        # Period 6 (Elements 55-86): Includes Lanthanides (4f series)
        # =====================================================================
        55: {"fa": "سزیم", "en": "Caesium", "symbol": "Cs", "atomic": 55, "mass": 132.91, "group": 1, "period": 6, "category": "فلز قلیایی", "mp": 28.5, "bp": 671, "config": "[Xe] 6s¹", "year": 1860},
        56: {"fa": "باریم", "en": "Barium", "symbol": "Ba", "atomic": 56, "mass": 137.33, "group": 2, "period": 6, "category": "فلز قلیایی خاکی", "mp": 727, "bp": 1870, "config": "[Xe] 6s²", "year": 1808},

        # Lanthanide series (57-71): Filling the 4f orbital
        57: {"fa": "لانتان", "en": "Lanthanum", "symbol": "La", "atomic": 57, "mass": 138.91, "group": 3, "period": 6, "category": "لانتانید", "mp": 920, "bp": 3464, "config": "[Xe] 5d¹ 6s²", "year": 1839},
        58: {"fa": "سریم", "en": "Cerium", "symbol": "Ce", "atomic": 58, "mass": 140.12, "group": 3, "period": 6, "category": "لانتانید", "mp": 795, "bp": 3443, "config": "[Xe] 4f¹ 5d¹ 6s²", "year": 1803},
        59: {"fa": "پرازئودیمیم", "en": "Praseodymium", "symbol": "Pr", "atomic": 59, "mass": 140.91, "group": 3, "period": 6, "category": "لانتانید", "mp": 935, "bp": 3520, "config": "[Xe] 4f³ 6s²", "year": 1885},
        60: {"fa": "نئودیمیم", "en": "Neodymium", "symbol": "Nd", "atomic": 60, "mass": 144.24, "group": 3, "period": 6, "category": "لانتانید", "mp": 1024, "bp": 3074, "config": "[Xe] 4f⁴ 6s²", "year": 1885},
        61: {"fa": "پرومتیم", "en": "Promethium", "symbol": "Pm", "atomic": 61, "mass": 145, "group": 3, "period": 6, "category": "لانتانید", "mp": 1042, "bp": 3000, "config": "[Xe] 4f⁵ 6s²", "year": 1945},
        62: {"fa": "ساماریم", "en": "Samarium", "symbol": "Sm", "atomic": 62, "mass": 150.36, "group": 3, "period": 6, "category": "لانتانید", "mp": 1072, "bp": 1791, "config": "[Xe] 4f⁶ 6s²", "year": 1879},
        63: {"fa": "یوروپیم", "en": "Europium", "symbol": "Eu", "atomic": 63, "mass": 151.96, "group": 3, "period": 6, "category": "لانتانید", "mp": 822, "bp": 1529, "config": "[Xe] 4f⁷ 6s²", "year": 1901},
        64: {"fa": "گادولینیم", "en": "Gadolinium", "symbol": "Gd", "atomic": 64, "mass": 157.25, "group": 3, "period": 6, "category": "لانتانید", "mp": 1313, "bp": 3273, "config": "[Xe] 4f⁷ 5d¹ 6s²", "year": 1880},
        65: {"fa": "تربیم", "en": "Terbium", "symbol": "Tb", "atomic": 65, "mass": 158.93, "group": 3, "period": 6, "category": "لانتانید", "mp": 1356, "bp": 3123, "config": "[Xe] 4f⁹ 6s²", "year": 1843},
        66: {"fa": "دیسپروزیم", "en": "Dysprosium", "symbol": "Dy", "atomic": 66, "mass": 162.5, "group": 3, "period": 6, "category": "لانتانید", "mp": 1412, "bp": 2567, "config": "[Xe] 4f¹⁰ 6s²", "year": 1886},
        67: {"fa": "هولمیم", "en": "Holmium", "symbol": "Ho", "atomic": 67, "mass": 164.93, "group": 3, "period": 6, "category": "لانتانید", "mp": 1474, "bp": 2700, "config": "[Xe] 4f¹¹ 6s²", "year": 1878},
        68: {"fa": "اربیم", "en": "Erbium", "symbol": "Er", "atomic": 68, "mass": 167.26, "group": 3, "period": 6, "category": "لانتانید", "mp": 1529, "bp": 2868, "config": "[Xe] 4f¹² 6s²", "year": 1843},
        69: {"fa": "تولیوم", "en": "Thulium", "symbol": "Tm", "atomic": 69, "mass": 168.93, "group": 3, "period": 6, "category": "لانتانید", "mp": 1545, "bp": 1950, "config": "[Xe] 4f¹³ 6s²", "year": 1879},
        70: {"fa": "ایتربیوم", "en": "Ytterbium", "symbol": "Yb", "atomic": 70, "mass": 173.04, "group": 3, "period": 6, "category": "لانتانید", "mp": 824, "bp": 1196, "config": "[Xe] 4f¹⁴ 6s²", "year": 1878},
        71: {"fa": "لوتسیم", "en": "Lutetium", "symbol": "Lu", "atomic": 71, "mass": 174.97, "group": 3, "period": 6, "category": "لانتانید", "mp": 1652, "bp": 3402, "config": "[Xe] 4f¹⁴ 5d¹ 6s²", "year": 1907},

        # Period 6 continued: Transition metals (5d series)
        72: {"fa": "هافنیم", "en": "Hafnium", "symbol": "Hf", "atomic": 72, "mass": 178.49, "group": 4, "period": 6, "category": "فلز واسطه", "mp": 2233, "bp": 4603, "config": "[Xe] 4f¹⁴ 5d² 6s²", "year": 1923},
        73: {"fa": "تانتال", "en": "Tantalum", "symbol": "Ta", "atomic": 73, "mass": 180.95, "group": 5, "period": 6, "category": "فلز واسطه", "mp": 3017, "bp": 5458, "config": "[Xe] 4f¹⁴ 5d³ 6s²", "year": 1802},
        74: {"fa": "تنگستن", "en": "Tungsten", "symbol": "W", "atomic": 74, "mass": 183.84, "group": 6, "period": 6, "category": "فلز واسطه", "mp": 3422, "bp": 5555, "config": "[Xe] 4f¹⁴ 5d⁴ 6s²", "year": 1781},
        75: {"fa": "رنیوم", "en": "Rhenium", "symbol": "Re", "atomic": 75, "mass": 186.21, "group": 7, "period": 6, "category": "فلز واسطه", "mp": 3186, "bp": 5596, "config": "[Xe] 4f¹⁴ 5d⁵ 6s²", "year": 1925},
        76: {"fa": "اسمیم", "en": "Osmium", "symbol": "Os", "atomic": 76, "mass": 190.23, "group": 8, "period": 6, "category": "فلز واسطه", "mp": 3033, "bp": 5012, "config": "[Xe] 4f¹⁴ 5d⁶ 6s²", "year": 1803},
        77: {"fa": "ایریدیم", "en": "Iridium", "symbol": "Ir", "atomic": 77, "mass": 192.22, "group": 9, "period": 6, "category": "فلز واسطه", "mp": 2446, "bp": 4428, "config": "[Xe] 4f¹⁴ 5d⁷ 6s²", "year": 1803},
        78: {"fa": "پلاتین", "en": "Platinum", "symbol": "Pt", "atomic": 78, "mass": 195.08, "group": 10, "period": 6, "category": "فلز واسطه", "mp": 1768, "bp": 3825, "config": "[Xe] 4f¹⁴ 5d⁹ 6s¹", "year": 1735},
        79: {"fa": "طلا", "en": "Gold", "symbol": "Au", "atomic": 79, "mass": 196.97, "group": 11, "period": 6, "category": "فلز واسطه", "mp": 1064, "bp": 2856, "config": "[Xe] 4f¹⁴ 5d¹⁰ 6s¹", "year": 0},
        80: {"fa": "جیوه", "en": "Mercury", "symbol": "Hg", "atomic": 80, "mass": 200.59, "group": 12, "period": 6, "category": "فلز پس‌گذار", "mp": -38.8, "bp": 356.6, "config": "[Xe] 4f¹⁴ 5d¹⁰ 6s²", "year": 0},
        81: {"fa": "تالیم", "en": "Thallium", "symbol": "Tl", "atomic": 81, "mass": 204.38, "group": 13, "period": 6, "category": "فلز پس‌گذار", "mp": 304, "bp": 1473, "config": "[Xe] 4f¹⁴ 5d¹⁰ 6s² 6p¹", "year": 1861},
        82: {"fa": "سرب", "en": "Lead", "symbol": "Pb", "atomic": 82, "mass": 207.2, "group": 14, "period": 6, "category": "فلز پس‌گذار", "mp": 327.5, "bp": 1749, "config": "[Xe] 4f¹⁴ 5d¹⁰ 6s² 6p²", "year": 0},
        83: {"fa": "بیسموت", "en": "Bismuth", "symbol": "Bi", "atomic": 83, "mass": 208.98, "group": 15, "period": 6, "category": "فلز پس‌گذار", "mp": 271.4, "bp": 1564, "config": "[Xe] 4f¹⁴ 5d¹⁰ 6s² 6p³", "year": 0},
        84: {"fa": "پولونیم", "en": "Polonium", "symbol": "Po", "atomic": 84, "mass": 209, "group": 16, "period": 6, "category": "شبه‌فلز", "mp": 254, "bp": 962, "config": "[Xe] 4f¹⁴ 5d¹⁰ 6s² 6p⁴", "year": 1898},
        85: {"fa": "استاتین", "en": "Astatine", "symbol": "At", "atomic": 85, "mass": 210, "group": 17, "period": 6, "category": "هالوژن", "mp": 302, "bp": 337, "config": "[Xe] 4f¹⁴ 5d¹⁰ 6s² 6p⁵", "year": 1940},
        86: {"fa": "رادون", "en": "Radon", "symbol": "Rn", "atomic": 86, "mass": 222, "group": 18, "period": 6, "category": "گاز نجیب", "mp": -71, "bp": -61.7, "config": "[Xe] 4f¹⁴ 5d¹⁰ 6s² 6p⁶", "year": 1900},

        # =====================================================================
        # Period 7 (Elements 87-118): Includes Actinides (5f series)
        # =====================================================================
        87: {"fa": "فرانسیم", "en": "Francium", "symbol": "Fr", "atomic": 87, "mass": 223, "group": 1, "period": 7, "category": "فلز قلیایی", "mp": 27, "bp": 677, "config": "[Rn] 7s¹", "year": 1939},
        88: {"fa": "رادیم", "en": "Radium", "symbol": "Ra", "atomic": 88, "mass": 226, "group": 2, "period": 7, "category": "فلز قلیایی خاکی", "mp": 700, "bp": 1737, "config": "[Rn] 7s²", "year": 1898},

        # Actinide series (89-103): Filling the 5f orbital
        89: {"fa": "آکتینیم", "en": "Actinium", "symbol": "Ac", "atomic": 89, "mass": 227, "group": 3, "period": 7, "category": "آکتینید", "mp": 1050, "bp": 3198, "config": "[Rn] 6d¹ 7s²", "year": 1899},
        90: {"fa": "توریم", "en": "Thorium", "symbol": "Th", "atomic": 90, "mass": 232.04, "group": 3, "period": 7, "category": "آکتینید", "mp": 1750, "bp": 4788, "config": "[Rn] 6d² 7s²", "year": 1829},
        91: {"fa": "پروتاکتینیم", "en": "Protactinium", "symbol": "Pa", "atomic": 91, "mass": 231.04, "group": 3, "period": 7, "category": "آکتینید", "mp": 1572, "bp": 4000, "config": "[Rn] 5f² 6d¹ 7s²", "year": 1913},
        92: {"fa": "اورانیوم", "en": "Uranium", "symbol": "U", "atomic": 92, "mass": 238.03, "group": 3, "period": 7, "category": "آکتینید", "mp": 1135, "bp": 4131, "config": "[Rn] 5f³ 6d¹ 7s²", "year": 1789},
        93: {"fa": "نپتونیوم", "en": "Neptunium", "symbol": "Np", "atomic": 93, "mass": 237, "group": 3, "period": 7, "category": "آکتینید", "mp": 644, "bp": 3902, "config": "[Rn] 5f⁴ 6d¹ 7s²", "year": 1940},
        94: {"fa": "پلوتونیم", "en": "Plutonium", "symbol": "Pu", "atomic": 94, "mass": 244, "group": 3, "period": 7, "category": "آکتینید", "mp": 639, "bp": 3228, "config": "[Rn] 5f⁶ 7s²", "year": 1940},
        95: {"fa": "امریسیم", "en": "Americium", "symbol": "Am", "atomic": 95, "mass": 243, "group": 3, "period": 7, "category": "آکتینید", "mp": 1176, "bp": 2011, "config": "[Rn] 5f⁷ 7s²", "year": 1944},
        96: {"fa": "کوریوم", "en": "Curium", "symbol": "Cm", "atomic": 96, "mass": 247, "group": 3, "period": 7, "category": "آکتینید", "mp": 1340, "bp": 3110, "config": "[Rn] 5f⁷ 6d¹ 7s²", "year": 1944},
        97: {"fa": "برکلیوم", "en": "Berkelium", "symbol": "Bk", "atomic": 97, "mass": 247, "group": 3, "period": 7, "category": "آکتینید", "mp": 986, "bp": 2627, "config": "[Rn] 5f⁹ 7s²", "year": 1949},
        98: {"fa": "کالیفرنیم", "en": "Californium", "symbol": "Cf", "atomic": 98, "mass": 251, "group": 3, "period": 7, "category": "آکتینید", "mp": 900, "bp": 1470, "config": "[Rn] 5f¹⁰ 7s²", "year": 1950},
        99: {"fa": "اینشتینیم", "en": "Einsteinium", "symbol": "Es", "atomic": 99, "mass": 252, "group": 3, "period": 7, "category": "آکتینید", "mp": 860, "bp": 996, "config": "[Rn] 5f¹¹ 7s²", "year": 1952},
        100: {"fa": "فرمیم", "en": "Fermium", "symbol": "Fm", "atomic": 100, "mass": 257, "group": 3, "period": 7, "category": "آکتینید", "mp": 1527, "bp": 0, "config": "[Rn] 5f¹² 7s²", "year": 1952},
        101: {"fa": "مندلیویوم", "en": "Mendelevium", "symbol": "Md", "atomic": 101, "mass": 258, "group": 3, "period": 7, "category": "آکتینید", "mp": 827, "bp": 0, "config": "[Rn] 5f¹³ 7s²", "year": 1955},
        102: {"fa": "نوبلیوم", "en": "Nobelium", "symbol": "No", "atomic": 102, "mass": 259, "group": 3, "period": 7, "category": "آکتینید", "mp": 827, "bp": 0, "config": "[Rn] 5f¹⁴ 7s²", "year": 1958},
        103: {"fa": "لورنسیم", "en": "Lawrencium", "symbol": "Lr", "atomic": 103, "mass": 262, "group": 3, "period": 7, "category": "آکتینید", "mp": 1627, "bp": 0, "config": "[Rn] 5f¹⁴ 7s² 7p¹", "year": 1961},

        # Period 7 continued: Superheavy elements (104-118)
        104: {"fa": "رادرفوردیم", "en": "Rutherfordium", "symbol": "Rf", "atomic": 104, "mass": 267, "group": 4, "period": 7, "category": "فلز واسطه", "mp": 2100, "bp": 5500, "config": "[Rn] 5f¹⁴ 6d² 7s²", "year": 1964},
        105: {"fa": "دوبنیم", "en": "Dubnium", "symbol": "Db", "atomic": 105, "mass": 268, "group": 5, "period": 7, "category": "فلز واسطه", "mp": 0, "bp": 0, "config": "[Rn] 5f¹⁴ 6d³ 7s²", "year": 1967},
        106: {"fa": "سیبورگیم", "en": "Seaborgium", "symbol": "Sg", "atomic": 106, "mass": 269, "group": 6, "period": 7, "category": "فلز واسطه", "mp": 0, "bp": 0, "config": "[Rn] 5f¹⁴ 6d⁴ 7s²", "year": 1974},
        107: {"fa": "بوریوم", "en": "Bohrium", "symbol": "Bh", "atomic": 107, "mass": 270, "group": 7, "period": 7, "category": "فلز واسطه", "mp": 0, "bp": 0, "config": "[Rn] 5f¹⁴ 6d⁵ 7s²", "year": 1981},
        108: {"fa": "هاسیم", "en": "Hassium", "symbol": "Hs", "atomic": 108, "mass": 277, "group": 8, "period": 7, "category": "فلز واسطه", "mp": 0, "bp": 0, "config": "[Rn] 5f¹⁴ 6d⁶ 7s²", "year": 1984},
        109: {"fa": "مایتنریم", "en": "Meitnerium", "symbol": "Mt", "atomic": 109, "mass": 278, "group": 9, "period": 7, "category": "فلز واسطه", "mp": 0, "bp": 0, "config": "[Rn] 5f¹⁴ 6d⁷ 7s²", "year": 1982},
        110: {"fa": "دارمشتادتیوم", "en": "Darmstadtium", "symbol": "Ds", "atomic": 110, "mass": 281, "group": 10, "period": 7, "category": "فلز واسطه", "mp": 0, "bp": 0, "config": "[Rn] 5f¹⁴ 6d⁸ 7s²", "year": 1994},
        111: {"fa": "رونتگنیوم", "en": "Roentgenium", "symbol": "Rg", "atomic": 111, "mass": 282, "group": 11, "period": 7, "category": "فلز واسطه", "mp": 0, "bp": 0, "config": "[Rn] 5f¹⁴ 6d⁹ 7s²", "year": 1994},
        112: {"fa": "کوپرنیسیم", "en": "Copernicium", "symbol": "Cn", "atomic": 112, "mass": 285, "group": 12, "period": 7, "category": "فلز واسطه", "mp": 0, "bp": 0, "config": "[Rn] 5f¹⁴ 6d¹⁰ 7s²", "year": 1996},
        113: {"fa": "نیهونیوم", "en": "Nihonium", "symbol": "Nh", "atomic": 113, "mass": 286, "group": 13, "period": 7, "category": "فلز پس‌گذار", "mp": 0, "bp": 0, "config": "[Rn] 5f¹⁴ 6d¹⁰ 7s² 7p¹", "year": 2003},
        114: {"fa": "فلروویوم", "en": "Flerovium", "symbol": "Fl", "atomic": 114, "mass": 289, "group": 14, "period": 7, "category": "فلز پس‌گذار", "mp": 0, "bp": 0, "config": "[Rn] 5f¹⁴ 6d¹⁰ 7s² 7p²", "year": 1999},
        115: {"fa": "مسکوویوم", "en": "Moscovium", "symbol": "Mc", "atomic": 115, "mass": 290, "group": 15, "period": 7, "category": "فلز پس‌گذار", "mp": 0, "bp": 0, "config": "[Rn] 5f¹⁴ 6d¹⁰ 7s² 7p³", "year": 2003},
        116: {"fa": "لیورموریوم", "en": "Livermorium", "symbol": "Lv", "atomic": 116, "mass": 293, "group": 16, "period": 7, "category": "فلز پس‌گذار", "mp": 0, "bp": 0, "config": "[Rn] 5f¹⁴ 6d¹⁰ 7s² 7p⁴", "year": 2000},
        117: {"fa": "تنسی", "en": "Tennessine", "symbol": "Ts", "atomic": 117, "mass": 294, "group": 17, "period": 7, "category": "هالوژن", "mp": 0, "bp": 0, "config": "[Rn] 5f¹⁴ 6d¹⁰ 7s² 7p⁵", "year": 2010},
        118: {"fa": "اوگانسون", "en": "Oganesson", "symbol": "Og", "atomic": 118, "mass": 294, "group": 18, "period": 7, "category": "گاز نجیب", "mp": 0, "bp": 0, "config": "[Rn] 5f¹⁴ 6d¹⁰ 7s² 7p⁶", "year": 2002},
    }

    @staticmethod
    def element_info(num):
        """
        Retrieves complete information for a chemical element by atomic number.

        Performs O(1) dictionary lookup in the class-level _elements database.
        Returns a dictionary with 11 bilingual properties for the requested
        element, or None if the atomic number is outside the valid range (1-118).

        Args:
            num (int): Atomic number of the element, ranging from 1 (Hydrogen)
                      to 118 (Oganesson).

        Returns:
            dict or None: A dictionary with 11 keys if the element exists:
                fa (str)     : Persian name (e.g., "طلا" for gold)
                en (str)     : English name (e.g., "Gold")
                symbol (str) : Chemical symbol, 1-3 characters (e.g., "Au")
                atomic (int) : Atomic number = number of protons
                mass (float) : Standard atomic weight in g/mol
                group (int)  : Group number in periodic table (1-18)
                period (int) : Period number in periodic table (1-7)
                category (str): Classification in Persian
                               (فلز قلیایی, گاز نجیب, لانتانید, etc.)
                mp (float)   : Melting point in °C (0 if unknown/unstable)
                bp (float)   : Boiling point in °C (0 if unknown/unstable)
                config (str) : Electron configuration in noble gas notation
                               (e.g., "[Xe] 4f¹⁴ 5d¹⁰ 6s¹" for gold)
                year (int)   : Year of discovery (0 if known since antiquity)
            Returns None if num < 1 or num > 118.

        Example:
            >>> gold = PeriodicTable.element_info(79)
            >>> gold['fa']
            'طلا'
            >>> gold['symbol']
            'Au'
            >>> gold['config']
            '[Xe] 4f¹⁴ 5d¹⁰ 6s¹'
            >>> gold['year']
            0  # Known since ancient times
        """
        return PeriodicTable._elements.get(num)