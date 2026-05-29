# برای اعمال رنگ توی output استفاده میشه.
# برای استفاده راحت ازش اینجوری اول برنامه ایمپورتش کن:
    # from color import *
def red(text):
    print("\033[91m {}\033[00m".format(text))
def green(text):
    print("\033[92m {}\033[00m".format(text))
def yellow(text):
    print("\033[93m {}\033[00m".format(text))
def blue(text):
    print("\033[94m {}\033[00m".format(text))
def purple(text):
    print("\033[95m {}\033[00m".format(text))
def cyan(text):
    print("\033[96m {}\033[00m".format(text))                   