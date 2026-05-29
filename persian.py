# =============================================================================
# Omega Calculator 10.0 - Module 9: Persian User Interface
# Author: Amirmahdi Ghorbani
# =============================================================================
# This module implements the complete Persian-language user interface for
# the Omega Calculator. It mirrors the English interface (CalculatorAppEN)
# with all user-facing strings translated to Persian (Farsi).
#
# Architecture:
#   Identical to the English version: composition over inheritance.
#   The class creates instances of all core engine modules and delegates
#   computation to them while handling all user interaction in Persian.
#
# Menu Structure (9 main categories, Persian labels):
#   1. حساب پایه (Basic Operations)
#   2. جبر و معادلات (Algebra & Equations)
#   3. هندسه و اندازه‌گیری (Geometry & Measurement)
#   4. نظریه اعداد (Number Theory)
#   5. آمار (Statistics)
#   6. حسابان (Calculus)
#   7. فیزیک (Physics)
#   8. جدول تناوبی (Periodic Table)
#   9. خروج (Exit)
#
# Dependencies:
#   - All core engine modules (same as English version)
#   - color (local): Terminal text coloring
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

# Import all core engine modules (same as English version)
from math_base import MathBase
from equations import EquationSolver
from calculus import Calculus
from matrix_ops import MatrixOperations
from formulas import PhysicsFormulas
from constants import PhysicalConstants
from periodic_table import PeriodicTable


class CalculatorAppFA:
    """
    Persian-language user interface for Omega Calculator.

    This class provides the complete Persian (Farsi) language interface.
    It mirrors CalculatorAppEN functionality with all user-facing strings
    translated to Persian. The underlying mathematical engine is identical;
    only the presentation layer differs.
    """

    def __init__(self):
        """Initializes the Persian UI with references to all core engines."""
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

    def moadeleD4(self):
        """حل معادله درجه چهارم."""
        red("معادله درجه چهارم")
        blue("ax⁴+bx³+cx²+dx+e=0")
        a = self.math_base.infut("a: "); b = self.math_base.infut("b: ")
        c = self.math_base.infut("c: "); d = self.math_base.infut("d: ")
        e = self.math_base.infut("e: ")
        roots = self.eq_solver.solve_quartic(a, b, c, d, e)
        purple(f"ریشه ها: {roots}")

    def lcm(self, a, b):
        """محاسبه ک.م.م دو عدد."""
        return (abs(a * b)) // gcd(a, b)

    def cot(self, x):
        """محاسبه کتانژانت."""
        return cos(x) / sin(x)

    def is_prime(self, n):
        """بررسی اول بودن عدد."""
        if n < 2: return False
        if n == 2: return True
        if n % 2 == 0: return False
        for i in range(3, int(sqrt(n)) + 1, 2):
            if n % i == 0: return False
        return True

    # =========================================================================
    # MENU 1: BASIC OPERATIONS (حساب پایه)
    # =========================================================================

    def radix(self):
        """تبدیل مبنای اعداد."""
        red("مبنای اعداد")
        blue("A) دسیمال به ..."); blue("B) ... به دسیمال")
        dec = input("کدام گزینه را می خواهید؟ ")
        time.sleep(0.2); os.system("clear")
        if dec == "A":
            blue("1.دسیمال به باینری"); blue("2.دسیمال به اوکتال"); blue("3.دسیمال به هگزادسیمال")
            d = int(input("کدام گزینه را می خواهید؟ "))
            num = int(input("عدد دسیمال: "))
            if d == 1: purple(f"{num} = {bin(num)}")
            elif d == 2: purple(f"{num} = {oct(num)}")
            elif d == 3: purple(f"{num} = {hex(num)}")
        elif dec == "B":
            num = input("عدد: "); INT = int(num)
            purple(f"{num} = {INT}")

    def bf(self):
        """اعمال چهارگانه ریاضی."""
        red("اعمال چهارگانه")
        yellow("عملیات ریاضی موردنظر خود را بنویسید. مثل 2+3×6")
        express = input("").replace("×", "*").replace("÷", "/")
        express = str(eval(express))
        result = "حاصل: " + express
        purple(result)

    def pr(self):
        """توان و ریشه."""
        red("توان و ریشه")
        blue("1.توان\n 2.ریشه")
        powerORradical = input("گزینه مد نظر خود را بنویسید: ")
        if powerORradical == "1":
            power = input("چیزی شبیه 2^5 بنویسید: ")
            power = "حاصل: " + str(eval(power.replace("^", "**")))
            purple(power)
        elif powerORradical == "2":
            r1 = float(input("عدد را بنویسید: ")); r2 = float(input("ریشه را بنویسید: "))
            result = "حاصل: " + str(r1 ** (1 / r2))
            purple(result)
        else: red("یافت نشد.")

    def tri(self):
        """توابع مثلثاتی."""
        red("توابع مثلثاتی")
        yellow("عملیات را بنویسید: "); yellow("مثال: sin(8)")
        tri = "حاصل: " + str((eval(input(""))))
        purple(tri)

    def mosh(self):
        """محاسبه مشتق عددی."""
        red("مشتق")
        expr = (input("تابع: ")).replace("^", "**").replace("×", "*").replace("÷", "/")
        x = int(input("نقطه مشتق: "))
        i = self.calculus.der(expr, x)
        purple(f"حاصل: {i}")

    def gcdlcm(self):
        """ب.م.م و ک.م.م."""
        red("ب.م.م و ک.م.م")
        yellow("لطفاً بنویسید gcd(x,y) برای ب.م.م یا lcm(x,y) برای ک.م.م: ")
        query = "حاصل: " + str(eval(input("")))
        purple(query)

    def Abs(self):
        """قدر مطلق."""
        red("قدر مطلق")
        result = "حاصل: " + str(abs(float(input("عدد را بنویسید: "))))
        purple(result)

    def taghrib(self):
        """تقریب (گرد کردن)."""
        red("تقریب")
        up_down = input("برای گرد کردن رو به بالا U و برای گرد کردن رو به پایین D وارد کنید: ")
        number = float(input("عدد: "))
        if up_down in ["U", "D"]:
            if up_down == "U": result = "حاصل: " + str(ceil(number))
            elif up_down == "D": result = "حاصل: " + str(floor(number))
            purple(result)
        else: red("یافت نشد.")

    def fis(self):
        """رابطه فیثاغورس."""
        red("رابطه فیثاغورس")
        sides = input("اضلاع قائم را وارد کنید مثل 9-10: ").split("-")
        Xside = ((float(sides[0]) ** 2) + (float(sides[1]) ** 2)) ** (1 / 2)
        result = "حاصل: " + str(Xside)
        purple(result)

    def svm(self):
        """معادله تک مجهولی درجه اول."""
        red("معادله تک مجهولی درجه اول")
        blue("ax+b=cx+d")
        if 2 < 5:
            abcd = input("مقادیر a,b,c,d را مانند 2-7-3-9 وارد کنید: ").split("-")
            a = float(abcd[0]); b = float(abcd[1]); c = float(abcd[2]); d = float(abcd[3])
            a = a - c; d = d - b; x = d / a
            result = "X : " + str(x)
            purple(result)
        else: red("یافت نشد.")

    def matrixF(self):
        """عملیات ماتریسی."""
        red("ماتریس")
        blue("1.جمع"); blue("2.ضرب"); blue("3.دترمینان"); blue("4.معکوس ماتریس ۲×۲")
        cyan("نکته: ماتریس ها را به صورت زیر بنویسید:")
        cyan("1,2,3;4,5,6;7,8,9")
        mat = int(input("کدام گزینه را می خواهید؟ "))
        time.sleep(0.2); os.system("clear")
        if mat == 1:
            a = input("ماتریس اول: "); b = input("ماتریس دوم: ")
            A = self.matrix_ops.matrix(a); B = self.matrix_ops.matrix(b)
            add = self.matrix_ops.matrix_add(A, B)
            purple("حاصل:"); purple(f"{add}")
        elif mat == 2:
            a = input("ماتریس اول: "); b = input("ماتریس دوم: ")
            A = self.matrix_ops.matrix(a); B = self.matrix_ops.matrix(b)
            add = self.matrix_ops.matrix_multiply(A, B)
            purple("حاصل:"); purple(add)
        elif mat == 3:
            a = input("ماتریس: "); A = self.matrix_ops.matrix(a)
            add = self.matrix_ops.determinant(A)
            purple("حاصل:"); purple(f"{add}")
        elif mat == 4:
            a = input("ماتریس (دو در دو): "); A = self.matrix_ops.matrix(a)
            add = self.matrix_ops.inverse_2x2(A)
            purple("حاصل:"); purple(f"{add}")

    def fact(self):
        """فاکتوریل."""
        red("فاکتوریل")
        num = int(input("عدد را وارد کنید: "))
        F = factorial(num)
        purple(f"{num}! = {F}")

    def rn(self):
        """ساخت عدد تصادفی."""
        red("ساخت عدد تصادفی")
        yellow("شروع،پایان و گام را مانند 1-100-5 وارد کنید: ")
        sss = input("").split("-")
        s1 = int(sss[0]); s2 = int(sss[1]); s3 = int(sss[2])
        number = random.randrange(s1, s2, s3)
        result = "عدد تصادفی:" + str(number)
        purple(result)

    def unit(self):
        """تبدیل واحد."""
        red("تبدیل واحد")
        blue("A) طول (cm,m,km,inch,foot)"); blue("B) دما (C,F,K)"); blue("C) جرم (g,kg,pound)")
        unit_choice = input("مقدار A یا B یا C را وارد کنید: ")
        if unit_choice == "A":
            yellow("بنویسید: مقدار از به (با فاصله)."); yellow("مثال: 100 cm m")
            parts = input("").split()
            value = float(parts[0]); from_u = parts[1]; to_u = parts[2]
            meter_values = {"cm": 0.01, "m": 1, "km": 1000, "inch": 0.0254, "foot": 0.3048}
            in_meters = value * meter_values[from_u]
            result_value = in_meters / meter_values[to_u]
            purple(f"حاصل:  {result_value} {to_u}")
        elif unit_choice == "B":
            yellow("بنویسید مقدار از به (با فاصله)."); yellow("مثال: 100 C F")
            parts = input("").split()
            value = float(parts[0]); from_u = parts[1]; to_u = parts[2]
            if from_u == "C":
                if to_u == "F": result_value = (value * 9 / 5) + 32
                elif to_u == "K": result_value = value + 273.15
                else: result_value = value
            elif from_u == "F":
                if to_u == "C": result_value = (value - 32) * 5 / 9
                elif to_u == "K": result_value = (value - 32) * 5 / 9 + 273.15
                else: result_value = value
            elif from_u == "K":
                if to_u == "C": result_value = value - 273.15
                elif to_u == "F": result_value = (value - 273.15) * 9 / 5 + 32
                else: result_value = value
            else: result_value = value
            purple(f"حاصل: {result_value} {to_u}")
        elif unit_choice == "C":
            yellow("بنویسید مقدار از به (با فاصله)."); yellow("مثال: 5 kg pound")
            parts = input("").split()
            value = float(parts[0]); from_u = parts[1]; to_u = parts[2]
            gram_values = {"g": 1, "kg": 1000, "pound": 453.592}
            in_grams = value * gram_values[from_u]
            result_value = in_grams / gram_values[to_u]
            purple(f"حاصل: {result_value} {to_u}")
        else: red("یافت نشد")

    def inte(self):
        """انتگرال معین."""
        red("انتگرال")
        expr = input("تابع (مثل x^2): ")
        a = float(input("حد پایین: ")); b = float(input("حد بالا: "))
        expr = expr.replace("^", "**").replace("×", "*").replace("÷", "/")
        i = self.calculus.integral(expr, a, b)
        purple(f"∫ = {i}")

    def pa(self):
        """محیط و مساحت اشکال هندسی."""
        red("محیط و مساحت")
        blue("A) مربع"); blue("B) مستطیل"); blue("C) دایره"); blue("D) مثلث")
        shape_choice = input("مقدار A یا B یا C یا D را وارد کنید: ")
        if shape_choice == "A":
            side = float(input("طول ضلع: "))
            perimeter = 4 * side; area = side ** 2
            purple(f"محیط = {perimeter} , مساحت: = {area}")
        elif shape_choice == "B":
            l = float(input("طول: ")); w = float(input("عرض: "))
            perimeter = 2 * (l + w); area = l * w
            purple(f"محیط = {perimeter} , مساحت = {area}")
        elif shape_choice == "C":
            r = float(input("شعاع: "))
            perimeter = 2 * pi * r; area = pi * r ** 2
            purple(f"محیط = {perimeter} , مساحت = {area}")
        elif shape_choice == "D":
            yellow("A) متساوی الاضلاع   B) قائم الزاویه   C) مختلف الاضلاع")
            tri_type = input("گزینه مد نظر خود را وارد کنید: ")
            if tri_type == "A":
                s = float(input("اندازه ضلع: "))
                perimeter = 3 * s; area = (sqrt(3) / 4) * s ** 2
                purple(f"محیط = {perimeter} , مساحت = {area}")
            elif tri_type == "B":
                a = float(input("ضلع قائم اول: ")); b = float(input("ضلع قائم دوم: "))
                c = sqrt(a ** 2 + b ** 2)
                perimeter = a + b + c; area = 0.5 * a * b
                purple(f"محیط = {perimeter} , مساحت = {area}")
            elif tri_type == "C":
                s1 = float(input("ضلع اول: ")); s2 = float(input("ضلع دوم: ")); s3 = float(input("ضلع سوم: "))
                perimeter = s1 + s2 + s3; sp = perimeter / 2
                area = sqrt(sp * (sp - s1) * (sp - s2) * (sp - s3))
                purple(f"محیط = {perimeter} , مساحت = {area}")
            else: red("یافت نشد")
        else: red("یافت نشد")

    def numg(self):
        """بازی حدس عدد."""
        red("بازی حدس عدد")
        yellow("عدد بین یک و صد است. حدس بزنید!")
        secret = random.randint(1, 100)
        attempts = 0; guessed = False
        while attempts < 10 and not guessed:
            try:
                guess = int(input(f"حدس شماره {attempts + 1}/10 - حدس تو: "))
                attempts += 1
                if guess == secret: green("درسته!"); guessed = True
                elif guess < secret: yellow("برو بالا!")
                else: yellow("برو پایین!")
            except: red("یک عدد درست وارد کنید.")
        if not guessed: purple(f"باختی! عدد {secret} بود!")

    def td(self):
        """حجم اشکال سه بعدی."""
        red("حجم اشکال سه بعدی")
        blue("A) مکعب"); blue("B) کره"); blue("C) استوانه"); blue("D) مخروط")
        shape_3d = input("یک گزینه وارد کنید: ")
        if shape_3d == "A":
            side = float(input("طول یال: ")); volume = side ** 3
            purple(f"V= {volume}")
        elif shape_3d == "B":
            r = float(input("شعاع: ")); volume = (4 / 3) * pi * r ** 3
            purple(f"V = {volume}")
        elif shape_3d == "C":
            r = float(input("شعاع: ")); h = float(input("ارتفاع: "))
            volume = pi * r ** 2 * h; purple(f"V = {volume}")
        elif shape_3d == "D":
            r = float(input("شعاع: ")); h = float(input("ارتفاع: "))
            volume = (1 / 3) * pi * r ** 2 * h; purple(f"V = {volume}")
        else: red("یافت نشد")

    def Fo(self):
        """الگوهای معروف."""
        red("الگو های معروف")
        blue("A) فیبوناچی"); blue("B) مثلث پاسکال"); blue("C) جدول ضرب")
        pat_choice = input("یک گزینه وارد کنید: ")
        if pat_choice == "A":
            n = int(input("چند جمله؟ "))
            a, b = 0, 1; result = ""
            for i in range(n): result += str(a) + " "; a, b = b, a + b
            purple(result)
        elif pat_choice == "B":
            rows = int(input("چند سطر؟ "))
            for i in range(rows):
                row_val = 1; line = ""
                for j in range(i + 1):
                    line += str(row_val) + " "
                    row_val = row_val * (i - j) // (j + 1)
                purple(line.center(50))
        elif pat_choice == "C":
            n = int(input("یک عدد وارد کنید: "))
            for i in range(1, n + 1):
                line = ""
                for j in range(1, n + 1): line += str(i * j) + "\t"
                purple(line)
        else: red("یافت نشد")

    def jadval(self):
        """جدول ضرب."""
        red("جدول ضرب")
        blue("A) یک عدد"); blue("B) چند عدد")
        mul_choice = input("یک گزینه وارد کنید: ")
        if mul_choice == "A":
            num = int(input("یک عدد وارد کنید:  ")); limit = int(input("تا: "))
            for i in range(1, limit + 1): purple(f"{num} × {i} = {num * i}")
        elif mul_choice == "B":
            start = int(input("شروع: ")); end = int(input("پایان: "))
            for i in range(start, end + 1):
                line = ""
                for j in range(1, 11): line += f"{i}×{j}={i * j}  "
                purple(line)
        else: red("یافت نشد")

    def tvm(self):
        """معادله دو مجهولی."""
        red("معادله دو مجهولی درجه اول")
        cyan("فرم:"); yellow("ax+by=c\n dx+ey=f")
        yellow("مقدار a,b,c,d,e,f را بنویسید: "); yellow("مثال: 2-3-8-1-2-5")
        parts = input("").split("-")
        a1 = float(parts[0]); b1 = float(parts[1]); c1 = float(parts[2])
        a2 = float(parts[3]); b2 = float(parts[4]); c2 = float(parts[5])
        det = a1 * b2 - a2 * b1
        if det == 0: red("حل این معادله ناممکن است!")
        else:
            x = (c1 * b2 - c2 * b1) / det; y = (a1 * c2 - a2 * c1) / det
            purple(f"x = {x} , y = {y}")

    def d2m(self):
        """معادله درجه دوم."""
        red("معادله درجه دوم")
        yellow("فرم: ax² + bx + c = 0")
        yellow("مقدار a,b,c را بنویسید."); yellow("مثال: 1-5-6")
        parts = input("").split("-")
        a = float(parts[0]); b = float(parts[1]); c = float(parts[2])
        if a == 0: red("این معادله درجه ۲ نیست زیرا a نمی تواند ۰ باشد.")
        else:
            delta = b ** 2 - 4 * a * c
            if delta > 0:
                x1 = (-b + sqrt(delta)) / (2 * a); x2 = (-b - sqrt(delta)) / (2 * a)
                purple(f"ریشه های حقیقی: x1 = {x1} , x2 = {x2}")
            elif delta == 0:
                x = -b / (2 * a); purple(f"ریشه: x = {x}")
            else:
                real = -b / (2 * a); imag = sqrt(abs(delta)) / (2 * a)
                purple(f"ریشه های مختلط: x1 = {real}+{imag}i , x2 = {real}-{imag}i")

    def m(self):
        """آمار مقدماتی."""
        red("آمار مقدماتی")
        blue("A) میانگین"); blue("B) میانه"); blue("C) مد")
        stat_choice = input("گزینه مد نظر خود را وارد کنید: ")
        yellow("عدد ها را با فاصله وارد کنید: ")
        nums = list(map(float, input("").split())); nums.sort()
        if stat_choice == "A": purple(f"میانگین = {sum(nums) / len(nums)}")
        elif stat_choice == "B":
            n = len(nums)
            if n % 2 == 0: median_val = (nums[n // 2 - 1] + nums[n // 2]) / 2
            else: median_val = nums[n // 2]
            purple(f"میانه = {median_val}")
        elif stat_choice == "C":
            freq = {}
            for num in nums: freq[num] = freq.get(num, 0) + 1
            max_freq = max(freq.values())
            modes = [k for k, v in freq.items() if v == max_freq]
            if len(modes) == len(nums): purple("بدون مد.")
            else: purple(f"مد(ها) = {modes}")
        else: red("یافت نشد.")

    def Variate(self):
        """توزیعات آماری."""
        red("توزیعات آماری")
        blue("A) یونیفرم"); blue("B) نرمال"); blue("C) مثلثی"); blue("D) اِکسپو"); blue("E) بتا")
        blue("F) گاما"); blue("G) لگ‌نرمال"); blue("H) پارتو"); blue("I) ویبول"); blue("J) فون مایزس")
        dist_choice = input("گزینه مد نظر خود را وارد کنید: ")
        try:
            if dist_choice == "A":
                a = float(input("مینیمم: ")); b = float(input("ماکزیمم: "))
                purple(f"عدد تصادفی: {random.uniform(a, b)}")
            elif dist_choice == "B":
                mu = float(input("میانه: ")); sigma = float(input("انحراف معیار: "))
                purple(f"عدد تصادفی: {random.gauss(mu, sigma)}")
            elif dist_choice == "C":
                low = float(input("مینیمم: ")); high = float(input("ماکزیمم: ")); mode = float(input("مُد: "))
                purple(f"عدد تصادفی: {random.triangular(low, high, mode)}")
            elif dist_choice == "D":
                lam = float(input("لامبدا: ")); purple(f"عدد تصادفی: {random.expovariate(lam)}")
            elif dist_choice == "E":
                alpha = float(input("آلفا: ")); beta = float(input("بتا: "))
                purple(f"عدد تصادفی: {random.betavariate(alpha, beta)}")
            elif dist_choice == "F":
                alpha = float(input("آلفا: ")); beta = float(input("بتا: "))
                purple(f"عدد تصادفی: {random.gammavariate(alpha, beta)}")
            elif dist_choice == "G":
                mu = float(input("مو (mu): ")); sigma = float(input("سیگما: "))
                purple(f"عدد تصادفی: {random.lognormvariate(mu, sigma)}")
            elif dist_choice == "H":
                alpha = float(input("آلفا: ")); purple(f"عدد تصادفی: {random.paretovariate(alpha)}")
            elif dist_choice == "I":
                alpha = float(input("آلفا: ")); beta = float(input("بتا: "))
                purple(f"عدد تصادفی: {random.weibullvariate(alpha, beta)}")
            elif dist_choice == "J":
                mu = float(input("مو (mu): ")); kappa = float(input("کاپا: "))
                purple(f"عدد تصادفی: {random.vonmisesvariate(mu, kappa)}")
            else: red("یافت نشد.")
        except: red("خطا یافت شد.")

    def prime(self):
        """اعداد اول."""
        red("اعداد اول")
        blue("A) تشخیص عدد اول"); blue("B) پیدا کردن همه اعداد اول تا n")
        prime_choice = input("گزینه مورد نظر خود را وارد کنید: ")
        if prime_choice == "A":
            n = int(input("عدد: "))
            if self.is_prime(n): green(f"{n} اول است ✅")
            else: red(f"{n} اول نیست ❌")
        elif prime_choice == "B":
            limit = int(input("تا چه عددی؟: ")); primes = []
            for i in range(2, limit + 1):
                if self.is_prime(i): primes.append(i)
            purple(f"اعداد اول تا {limit}:"); purple(str(primes))
            green(f"{len(primes)} عدد اول پیدا شد")
        else: red("یافت نشد")

    def jabr(self):
        """جبر پایه."""
        red("جبر پایه")
        blue("A) بسط (a+b)^2 و (a-b)^2"); blue("B) فاکتور گیری a^2-b^2")
        alg_choice = input("یک گزینه انتخاب کنید: ")
        if alg_choice == "A":
            a = float(input("a: ")); b = float(input("b: "))
            sum_sq = a ** 2 + 2 * a * b + b ** 2; diff_sq = a ** 2 - 2 * a * b + b ** 2
            purple(f"(a+b)^2 = {sum_sq}"); purple(f"(a-b)^2 = {diff_sq}")
        elif alg_choice == "B":
            a = float(input("a: ")); b = float(input("b: "))
            result = a ** 2 - b ** 2
            purple(f"a^2 - b^2 = {result}")
            purple(f"شکل فاکتور گرفته: ({a}+{b})({a}-{b}) = {result}")

    # =========================================================================
    # POLYNOMIAL EQUATIONS
    # =========================================================================

    def quintic_equation(self):
        """معادله درجه پنجم."""
        red("معادله درجه پنجم"); blue("ax⁵+bx⁴+cx³+dx²+ex+f=0")
        parts = input("ضرایب a,b,c,d,e,f را با ; جدا کنید: ").split(";")
        coeffs = [float(p) for p in parts]
        roots = self.eq_solver.solve_polynomial_general(coeffs)
        purple(f"ریشه ها = {roots}")

    def sextic_equation(self):
        """معادله درجه ششم."""
        red("معادله درجه ششم"); blue("ax⁶+bx⁵+cx⁴+dx³+ex²+fx+g=0")
        parts = input("ضرایب a,b,c,d,e,f,g را با ; جدا کنید: ").split(";")
        coeffs = [float(p) for p in parts]
        roots = self.eq_solver.solve_polynomial_general(coeffs)
        purple(f"ریشه ها = {roots}")

    def septic_equation(self):
        """معادله درجه هفتم."""
        red("معادله درجه هفتم"); blue("ax⁷+bx⁶+cx⁵+dx⁴+ex³+fx²+gx+h=0")
        parts = input("ضرایب a,b,c,d,e,f,g,h را با ; جدا کنید: ").split(";")
        coeffs = [float(p) for p in parts]
        roots = self.eq_solver.solve_polynomial_general(coeffs)
        purple(f"ریشه ها = {roots}")

    def octic_equation(self):
        """معادله درجه هشتم."""
        red("معادله درجه هشتم"); blue("ax⁸+bx⁷+cx⁶+dx⁵+ex⁴+fx³+gx²+hx+i=0")
        parts = input("ضرایب a,b,c,d,e,f,g,h,i را با ; جدا کنید: ").split(";")
        coeffs = [float(p) for p in parts]
        roots = self.eq_solver.solve_polynomial_general(coeffs)
        purple(f"ریشه ها = {roots}")

    def nonic_equation(self):
        """معادله درجه نهم."""
        red("معادله درجه نهم"); blue("ax⁹+bx⁸+cx⁷+dx⁶+ex⁵+fx⁴+gx³+hx²+ix+j=0")
        parts = input("ضرایب (۱۰ عدد) را با ; جدا کنید: ").split(";")
        coeffs = [float(p) for p in parts]
        roots = self.eq_solver.solve_polynomial_general(coeffs)
        purple(f"ریشه ها = {roots}")

    def decic_equation(self):
        """معادله درجه دهم."""
        red("معادله درجه دهم"); blue("ax¹⁰+bx⁹+cx⁸+dx⁷+ex⁶+fx⁵+gx⁴+hx³+ix²+jx+k=0")
        parts = input("ضرایب (۱۱ عدد) را با ; جدا کنید: ").split(";")
        coeffs = [float(p) for p in parts]
        roots = self.eq_solver.solve_polynomial_general(coeffs)
        purple(f"ریشه ها = {roots}")

    # =========================================================================
    # PHYSICS SUB-MENUS (Persian)
    # =========================================================================

    def _physics_kinematics_fa(self):
        """سینماتیک."""
        purple("سینماتیک")
        cyan("1.سرعت نهایی [v=v0+at]"); cyan("2.مکان [x=x0+v0t+0.5at²]")
        cyan("3.سرعت نهایی [v²=v0²+2aΔx]"); cyan("4.سرعت متوسط [v_avg=Δx/Δt]")
        cyan("5.شتاب متوسط [a_avg=Δv/Δt]"); cyan("6.سرعت سقوط آزاد [v=gt]")
        cyan("7.ارتفاع سقوط آزاد [h=0.5gt²]"); cyan("8.برد پرتابه [R=v0²sin(2θ)/g]")
        cyan("9.حداکثر ارتفاع پرتابه [H=v0²sin²θ/(2g)]"); cyan("10.زمان پرواز پرتابه [T=2v0sinθ/g]")
        cin = int(input("کدام گزینه را می خواهید؟ "))
        time.sleep(0.2); os.system("clear")
        infut = self.math_base.infut
        if cin == 1:
            red("v = v0 + at"); v0 = infut("v0: "); a = infut("a: "); t = infut("t: ")
            purple(f"v = {self.physics.velocity_final_1(v0, a, t)}")
        elif cin == 2:
            red("x = x0 + v0t + 0.5at²"); x0 = infut("x0: "); v0 = infut("v0: "); a = infut("a: "); t = infut("t: ")
            purple(f"x = {self.physics.position_2(x0, v0, a, t)}")
        elif cin == 3:
            red("v² = v0² + 2aΔx"); v0 = infut("v0: "); a = infut("a: "); dx = infut("dx: ")
            purple(f"v = {self.physics.velocity_final_3(v0, a, dx)}")
        elif cin == 4:
            red("v_avg = Δx/Δt"); dx = infut("dx: "); dt = infut("dt: ")
            purple(f"v_avg = {self.physics.velocity_average(dx, dt)}")
        elif cin == 5:
            red("a_avg = Δv/Δt"); dv = infut("dv: "); dt = infut("dt: ")
            purple(f"a_avg = {self.physics.acceleration_average(dv, dt)}")
        elif cin == 6:
            red("v = gt"); g = infut("g: "); t = infut("t: ")
            purple(f"v = {self.physics.free_fall_velocity(t, g)}")
        elif cin == 7:
            red("h = 0.5gt²"); g = infut("g: "); t = infut("t: ")
            purple(f"h = {self.physics.free_fall_height(t, g)}")
        elif cin == 8:
            red("R = v0²sin(2θ)/g"); v0 = infut("v0: "); theta = infut("θ (درجه): "); g = infut("g: ")
            purple(f"برد = {self.physics.projectile_range(v0, theta, g)}")
        elif cin == 9:
            red("H = v0²sin²θ/(2g)"); v0 = infut("v0: "); theta = infut("θ (درجه): "); g = infut("g: ")
            purple(f"حداکثر ارتفاع = {self.physics.projectile_max_height(v0, theta, g)}")
        elif cin == 10:
            red("T = 2v0sinθ/g"); v0 = infut("v0: "); theta = infut("θ (درجه): "); g = infut("g: ")
            purple(f"زمان پرواز = {self.physics.projectile_time_of_flight(v0, theta, g)}")

    def _physics_dynamics_fa(self):
        """دینامیک."""
        purple("دینامیک")
        cyan("1.نیرو [F=ma]"); cyan("2.وزن [w=mg]"); cyan("3.نیروی عمودی سطح شیبدار [N=mgcosθ]")
        cyan("4.اصطکاک جنبشی [f_k=μ_k N]"); cyan("5.اصطکاک ایستایی بیشینه [f_s=μ_s N]")
        cyan("6.نیروی خالص یک بعدی [F_net=ΣF]"); cyan("7.تکانه [p=mv]")
        cyan("8.ضربه [J=FΔt]"); cyan("9.قانون هوک [F=-kx]")
        cin = int(input("کدام گزینه را می خواهید؟ "))
        time.sleep(0.2); os.system("clear")
        infut = self.math_base.infut
        if cin == 1:
            red("F = ma"); m = infut("m: "); a = infut("a: ")
            purple(f"F = {self.physics.force_newton(m, a)}")
        elif cin == 2:
            red("w = mg"); m = infut("m: "); g = infut("g: ")
            purple(f"w = {self.physics.weight(m, g)}")
        elif cin == 3:
            red("N = mgcosθ"); m = infut("m: "); theta = infut("θ (درجه): "); g = infut("g: ")
            purple(f"N = {self.physics.normal_incline(m, theta, g)}")
        elif cin == 4:
            red("f_k = μ_k N"); mu_k = infut("μ_k: "); N = infut("N: ")
            purple(f"f_k = {self.physics.friction_kinetic(mu_k, N)}")
        elif cin == 5:
            red("f_s_max = μ_s N"); mu_s = infut("μ_s: "); N = infut("N: ")
            purple(f"f_s_max = {self.physics.friction_static_max(mu_s, N)}")
        elif cin == 6:
            red("F_net = ΣF"); forces = list(map(float, input("نیروها را با فاصله وارد کنید: ").split()))
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

    def _physics_work_energy_fa(self):
        """کار، انرژی و توان."""
        purple("کار، انرژی و توان")
        cyan("1.کار [W=Fdcosθ]"); cyan("2.انرژی جنبشی [KE=0.5mv²]")
        cyan("3.انرژی پتانسیل گرانشی [PE=mgh]"); cyan("4.انرژی پتانسیل کشسانی [PE=0.5kx²]")
        cyan("5.قضیه کار-انرژی [W_net=ΔKE]"); cyan("6.انرژی مکانیکی [E=KE+PE]")
        cyan("7.توان متوسط [P_avg=W/t]"); cyan("8.توان لحظه‌ای [P=Fvcosθ]")
        cyan("9.بازده [η=(W_out/W_in)×100]")
        cin = int(input("کدام گزینه را می خواهید؟ "))
        time.sleep(0.2); os.system("clear")
        infut = self.math_base.infut
        if cin == 1:
            red("W = Fd cosθ"); F = infut("F: "); d = infut("d: "); theta = infut("θ (درجه): ")
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
            red("P = Fv cosθ"); F = infut("F: "); v = infut("v: "); theta = infut("θ (درجه): ")
            purple(f"P = {self.physics.power_instantaneous(F, v, theta)}")
        elif cin == 9:
            red("η = (W_out / W_in) × 100"); W_out = infut("W_out: "); W_in = infut("W_in: ")
            purple(f"بازده = {self.physics.efficiency(W_out, W_in)}%")

    def _physics_fluids_fa(self):
        """مکانیک سیالات."""
        purple("مکانیک سیالات")
        cyan("1.چگالی [ρ=m/V]"); cyan("2.فشار [P=F/A]"); cyan("3.فشار در عمق [P=P0+ρgh]")
        cyan("4.نیروی شناوری [F_b=ρ_fluid V_sub g]")
        cyan("5.معادله برنولی [P2=P1+0.5ρ(v1²-v2²)+ρg(h1-h2)]")
        cyan("6.معادله پیوستگی [v2=A1v1/A2]")
        cin = int(input("کدام گزینه را می خواهید؟ "))
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

    def _physics_electricity_fa(self):
        """الکتریسیته و مغناطیس."""
        purple("الکتریسیته و مغناطیس")
        cyan("1.قانون اهم - ولتاژ [V=IR]"); cyan("2.قانون اهم - جریان [I=V/R]")
        cyan("3.قانون اهم - مقاومت [R=V/I]"); cyan("4.توان الکتریکی [P=VI]")
        cyan("5.توان الکتریکی [P=I²R]"); cyan("6.توان الکتریکی [P=V²/R]")
        cyan("7.مقاومت سری [R_total=R1+R2+...]"); cyan("8.مقاومت موازی [1/R_total=1/R1+1/R2+...]")
        cyan("9.ولتاژ از انرژی [V=W/q]"); cyan("10.جریان الکتریکی [I=Δq/Δt]")
        cyan("11.قانون کولن [F=kq1q2/r²]"); cyan("12.میدان الکتریکی [E=F/q]")
        cyan("13.میدان الکتریکی خازن تخت [E=V/d]")
        cin = int(input("کدام گزینه را می خواهید؟ "))
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
            resistors = list(map(float, input("مقاومت ها را با فاصله وارد کنید: ").split()))
            purple(f"R_total = {self.physics.resistors_series(resistors)}")
        elif cin == 8:
            red("1/R_total = 1/R1 + 1/R2 + ...")
            resistors = list(map(float, input("مقاومت ها را با فاصله وارد کنید: ").split()))
            purple(f"R_total = {self.physics.resistors_parallel(resistors)}")
        elif cin == 9:
            red("V = W/q"); W = infut("W: "); q = infut("q: ")
            purple(f"V = {self.physics.voltage_energy(W, q)}")
        elif cin == 10:
            red("I = Δq/Δt"); q = infut("Δq: "); t = infut("Δt: ")
            purple(f"I = {self.physics.current_rate(q, t)}")
        elif cin == 11:
            red("F = k q1 q2 / r²"); q1 = infut("q1: "); q2 = infut("q2: "); r = infut("r: ")
            k = infut("k (پیش‌فرض 8.99e9): ")
            if k == 0: F = self.physics.coulomb_law(q1, q2, r)
            else: F = self.physics.coulomb_law(q1, q2, r, k)
            purple(f"F = {F}")
        elif cin == 12:
            red("E = F/q"); F = infut("F: "); q = infut("q: ")
            purple(f"E = {self.physics.electric_field(F, q)}")
        elif cin == 13:
            red("E = V/d"); V = infut("V: "); d = infut("d: ")
            purple(f"E = {self.physics.electric_field_parallel_plate(V, d)}")

    def _physics_heat_fa(self):
        """حرارت و ترمودینامیک."""
        purple("حرارت و ترمودینامیک")
        cyan("1.گرمای محسوس [Q=mcΔT]"); cyan("2.گرمای نهان ذوب [Q=mL_f]")
        cyan("3.گرمای نهان تبخیر [Q=mL_v]"); cyan("4.انبساط طولی [ΔL=αL0ΔT]")
        cyan("5.انبساط سطحی [ΔA=βA0ΔT]"); cyan("6.انبساط حجمی [ΔV=γV0ΔT]")
        cyan("7.فشار گاز ایده‌آل [P=nRT/V]"); cyan("8.حجم گاز ایده‌آل [V=nRT/P]")
        cyan("9.قانون اول ترمودینامیک [ΔU=Q-W]"); cyan("10.بازده موتور حرارتی [η=1-Q_c/Q_h]")
        cin = int(input("کدام گزینه را می خواهید؟ "))
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
            purple(f"بازده = {self.physics.heat_engine_efficiency(Q_h, Q_c)}")

    def _physics_optics_fa(self):
        """نور و اپتیک."""
        purple("نور و اپتیک")
        cyan("1.سرعت موج [c=fλ]"); cyan("2.ضریب شکست [n=c/v]")
        cyan("3.قانون اسنل [θ2=arcsin(n1 sinθ1/n2)]"); cyan("4.معادله عدسی‌ها [1/f=1/p+1/q]")
        cyan("5.بزرگنمایی [M=-q/p]"); cyan("6.قدرت عدسی [P=1/f]"); cyan("7.زاویه بحرانی [θ_c=arcsin(n2/n1)]")
        cin = int(input("کدام گزینه را می خواهید؟ "))
        time.sleep(0.2); os.system("clear")
        infut = self.math_base.infut
        if cin == 1:
            red("c = fλ"); f = infut("f: "); lam = infut("λ: ")
            purple(f"c = {self.physics.wave_speed(f, lam)}")
        elif cin == 2:
            red("n = c/v"); c = infut("c: "); v = infut("v: ")
            purple(f"n = {self.physics.refractive_index(c, v)}")
        elif cin == 3:
            red("θ2 = arcsin(n1 sinθ1 / n2)"); n1 = infut("n1: "); theta1 = infut("θ1 (درجه): "); n2 = infut("n2: ")
            purple(f"θ2 = {self.physics.snells_law_angle2(n1, theta1, n2)} درجه")
        elif cin == 4:
            red("1/f = 1/p + 1/q"); p = infut("p: "); q = infut("q: ")
            purple(f"f = {self.physics.lens_maker_equation(0, p, q)}")
        elif cin == 5:
            red("M = -q/p"); p = infut("p: "); q = infut("q: ")
            purple(f"M = {self.physics.magnification(p, q)}")
        elif cin == 6:
            red("P = 1/f"); f = infut("f (متر): ")
            purple(f"P = {self.physics.lens_power(f)} D")
        elif cin == 7:
            red("θ_c = arcsin(n2/n1)"); n1 = infut("n1: "); n2 = infut("n2: ")
            purple(f"θ_c = {self.physics.critical_angle(n1, n2)} درجه")

    def _physics_modern_fa(self):
        """فیزیک مدرن."""
        purple("فیزیک مدرن")
        cyan("1.همارزی جرم-انرژی [E=mc²]"); cyan("2.انرژی فوتون [E=hf]")
        cyan("3.انرژی فوتون از طول موج [E=hc/λ]"); cyan("4.طول موج دوبروی [λ=h/mv]")
        cyan("5.ضریب لورنتس [γ=1/√(1-v²/c²)]"); cyan("6.اتساع زمان [Δt=γΔt₀]")
        cyan("7.انقباض طول [L=L₀/γ]")
        cin = int(input("کدام گزینه را می خواهید؟ "))
        time.sleep(0.2); os.system("clear")
        infut = self.math_base.infut
        if cin == 1:
            red("E = mc²"); m = infut("m: "); c = infut("c (پیش‌فرض 3e8): ")
            if c == 0: E = self.physics.mass_energy_equivalence(m)
            else: E = self.physics.mass_energy_equivalence(m, c)
            purple(f"E = {E}")
        elif cin == 2:
            red("E = hf"); f = infut("f: "); h = infut("h (پیش‌فرض 6.626e-34): ")
            if h == 0: E = self.physics.photon_energy(f)
            else: E = self.physics.photon_energy(f, h)
            purple(f"E = {E}")
        elif cin == 3:
            red("E = hc/λ"); lam = infut("λ: "); h = infut("h (پیش‌فرض 6.626e-34): "); c = infut("c (پیش‌فرض 3e8): ")
            if h == 0 and c == 0: E = self.physics.photon_energy_wavelength(lam)
            elif h == 0: E = self.physics.photon_energy_wavelength(lam, c=c)
            elif c == 0: E = self.physics.photon_energy_wavelength(lam, h=h)
            else: E = self.physics.photon_energy_wavelength(lam, h, c)
            purple(f"E = {E}")
        elif cin == 4:
            red("λ = h/mv"); m = infut("m: "); v = infut("v: "); h = infut("h (پیش‌فرض 6.626e-34): ")
            if h == 0: lam = self.physics.de_broglie_wavelength(m, v)
            else: lam = self.physics.de_broglie_wavelength(m, v, h)
            purple(f"λ = {lam}")
        elif cin == 5:
            red("γ = 1/√(1-v²/c²)"); v = infut("v: "); c = infut("c (پیش‌فرض 3e8): ")
            if c == 0: gamma = self.physics.lorentz_factor(v)
            else: gamma = self.physics.lorentz_factor(v, c)
            purple(f"γ = {gamma}")
        elif cin == 6:
            red("Δt = γ Δt₀"); dt0 = infut("Δt₀: "); v = infut("v: "); c = infut("c (پیش‌فرض 3e8): ")
            if c == 0: dt = self.physics.time_dilation(dt0, v)
            else: dt = self.physics.time_dilation(dt0, v, c)
            purple(f"Δt = {dt}")
        elif cin == 7:
            red("L = L₀/γ"); L0 = infut("L₀: "); v = infut("v: "); c = infut("c (پیش‌فرض 3e8): ")
            if c == 0: L = self.physics.length_contraction(L0, v)
            else: L = self.physics.length_contraction(L0, v, c)
            purple(f"L = {L}")

    def _physics_constants_fa(self):
        """ثابت های فیزیک."""
        purple("ثابت های فیزیک")
        cyan("1.g = 9.8 m/s²"); cyan("2.G = 6.674×10⁻¹¹ N·m²/kg²")
        cyan("3.c = 3×10⁸ m/s"); cyan("4.h = 6.626×10⁻³⁴ J·s")
        cyan("5.ħ = 1.054×10⁻³⁴ J·s"); cyan("6.k_B = 1.38×10⁻²³ J/K")
        cyan("7.e = 1.6×10⁻¹⁹ C"); cyan("8.ε₀ = 8.85×10⁻¹² C²/N·m²")
        cyan("9.μ₀ = 4π×10⁻⁷ N/A²"); cyan("10.m_e = 9.11×10⁻³¹ kg")
        cyan("11.m_p = 1.67×10⁻²⁷ kg"); cyan("12.N_A = 6.022×10²³ mol⁻¹")
        cyan("13.R = 8.314 J/(mol·K)"); cyan("14.σ = 5.67×10⁻⁸ W/m²·K⁴")
        cyan("15.R_∞ = 1.097×10⁷ m⁻¹"); cyan("16.μ_B = 9.274×10⁻²⁴ J/T")
        cyan("17.a0 = 5.29×10⁻¹¹ m")
        cin = int(input("کدام ثابت را می خواهید؟ "))
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
    # MAIN APPLICATION LOOP (Persian)
    # =========================================================================

    def run(self):
        """حلقه اصلی برنامه به زبان فارسی."""
        while True:
            cyan("ماشین حساب امگا ۱۰.۰\n")
            purple("منو")
            yellow("1.حساب پایه"); yellow("2.جبر و معادلات"); yellow("3.هندسه و اندازه‌گیری")
            yellow("4.نظریه اعداد"); yellow("5.آمار"); yellow("6.حسابان")
            yellow("7.فیزیک"); yellow("8.جدول تناوبی"); yellow("9.خروج")
            menu = int(input("کدام گزینه را می خواهید؟"))
            os.system("clear"); time.sleep(0.25)
            red("قابلیت ها:")
            if menu == 1:
                green("1.چهار عمل اصلی\n ‌2.توان و ریشه")
                green("3.قدر مطلق\n 4.تقریب\n 5.فاکتوریل\n 6.جدول ضرب")
                A1 = int(input("کدام قابلیت را می خواهید؟ "))
                time.sleep(0.2); os.system("clear")
                if A1 == 1: self.bf()
                elif A1 == 2: self.pr()
                elif A1 == 3: self.Abs()
                elif A1 == 4: self.taghrib()
                elif A1 == 5: self.fact()
                elif A1 == 6: self.jadval()
            elif menu == 2:
                green("1.جبر پایه\n 2.معادله تک مجهولی\n 3.معادله دو مجهولی\n 4.معادله درجه دوم")
                green("5.معادله درجه سوم\n 6.معادله درجه چهارم\n 7.معادله درجه پنجم\n 8.معادله درجه ششم\n 9.معادله درجه هفتم\n 10.معادله درجه هشتم\n 11.معادله درجه نهم\n 12.معادله درجه دهم\n 13.ماتریس")
                A2 = int(input("کدام قابلیت را می خواهید؟ "))
                time.sleep(0.2); os.system("clear")
                if A2 == 1: self.jabr()
                elif A2 == 2: self.svm()
                elif A2 == 3: self.tvm()
                elif A2 == 4: self.d2m()
                elif A2 == 5:
                    red("معادله درجه سوم"); blue("ax³+bx²+cx+d=0")
                    n = input("مقدار های a,b,c,d را به ترتیب با فاصله بنویسید: ").split()
                    a = float(n[0]); b = float(n[1]); c = float(n[2]); d = float(n[3])
                    r = self.eq_solver.cubic_equation(a, b, c, d)
                    purple(f"ریشه های معادله:\n {r[0]}\n {r[1]}\n {r[2]}")
                elif A2 == 6: self.moadeleD4()
                elif A2 == 7: self.quintic_equation()
                elif A2 == 8: self.sextic_equation()
                elif A2 == 9: self.septic_equation()
                elif A2 == 10: self.octic_equation()
                elif A2 == 11: self.nonic_equation()
                elif A2 == 12: self.decic_equation()
                elif A2 == 13: self.matrixF()
            elif menu == 3:
                green("1.محیط و مساحت\n 2.حجم اشکال سه بعدی\n 3.رابطه فیثاغورس\n 4.توابع مثلثاتی\n 5.تبدیل واحد")
                c = int(input("کدام قابلیت را می خواهید؟ "))
                time.sleep(0.2); os.system('clear')
                if c == 1: self.pa()
                elif c == 2: self.td()
                elif c == 3: self.fis()
                elif c == 4: self.tri()
                elif c == 5: self.unit()
            elif menu == 4:
                green("1.ب.م.م و ک.م.م\n 2.کار با اعداد اول\n 3.الگو های مشهور\n 4.مبنای اعداد")
                d = int(input("کدام قابلیت را می خواهید؟ "))
                time.sleep(0.2); os.system('clear')
                if d == 1: self.gcdlcm()
                elif d == 2: self.prime()
                elif d == 3: self.Fo()
                elif d == 4: self.radix()
            elif menu == 5:
                green("1.آمار پایه\n 2.توزیع های آماری\n 3.ساخت عدد تصادفی\n 4.بازی حدس عدد")
                e = int(input("کدام قابلیت را می خواهید؟ "))
                time.sleep(0.2); os.system("clear")
                if e == 1: self.m()
                elif e == 2: self.Variate()
                elif e == 3: self.rn()
                elif e == 4: self.numg()
            elif menu == 6:
                green("1.انتگرال\n 2.مشتق")
                f = int(input("کدام قابلیت را می خواهید؟ "))
                time.sleep(0.2); os.system("clear")
                if f == 1: self.inte()
                elif f == 2: self.mosh()
            elif menu == 7:
                green("1.سینماتیک\n 2.دینامیک\n 3.کار، انرژی و توان\n 4.مکانیک سیالات\n 5.الکتریسیته و مغناطیس\n 6.حرارت و ترمودینامیک\n 7.نور و اپتیک\n 8.فیزیک مدرن\n 9.ثابت های فیزیک")
                ph = int(input("کدام قابلیت را می خواهید؟ "))
                time.sleep(0.2); os.system("clear")
                if ph == 1: self._physics_kinematics_fa()
                elif ph == 2: self._physics_dynamics_fa()
                elif ph == 3: self._physics_work_energy_fa()
                elif ph == 4: self._physics_fluids_fa()
                elif ph == 5: self._physics_electricity_fa()
                elif ph == 6: self._physics_heat_fa()
                elif ph == 7: self._physics_optics_fa()
                elif ph == 8: self._physics_modern_fa()
                elif ph == 9: self._physics_constants_fa()
            elif menu == 8:
                purple("جدول تناوبی")
                num = int(input("شماره عنصر را وارد کنید (۱-۱۱۸): "))
                e = self.periodic.element_info(num)
                if e:
                    cyan("اطلاعات عنصر:")
                    yellow(f"نام فارسی: {e['fa']}"); yellow(f"نام انگلیسی: {e['en']}")
                    yellow(f"نماد: {e['symbol']}"); yellow(f"عدد اتمی: {e['atomic']}")
                    yellow(f"عدد جرمی: {e['mass']} g/mol"); yellow(f"گروه: {e['group']}")
                    yellow(f"تناوب: {e['period']}"); yellow(f"دسته: {e['category']}")
                    yellow(f"نقطه ذوب: {e['mp']} °C"); yellow(f"نقطه جوش: {e['bp']} °C")
                    yellow(f"ساختار الکترونی: {e['config']}")
                    if e['year'] == 0: yellow("سال کشف: نامشخص (از دوران باستان شناخته شده)")
                    else: yellow(f"سال کشف: {e['year']} میلادی")
                else: red("عنصر یافت نشد! لطفاً عددی بین ۱ تا ۱۱۸ وارد کنید")
            elif menu == 9:
                os.system("clear"); purple("خداحافظ!"); break
            input("برای ادامه Enter بزنید...")
            os.system("clear")