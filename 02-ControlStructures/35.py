# coding=utf-8
# pierwiastki równania ax^2+bx+c=0
from math import sqrt



a = input("Podaj a: ")
try:
    float(a)
except (ValueError, NameError):
    print("Podana wartość nie jest prawidłową liczbą")
else:
    b = input("Podaj b: ")
    try:
        float(b)
    except (ValueError, NameError):
        print("Podana wartość nie jest prawidłową liczbą")
    else:
        c = input("Podaj c: ")
        try:
            float(c)
        except (ValueError, NameError):
            print("Podana wartość nie jest prawidłową liczbą")
        else:
            print("Równanie {0}x^2+{1}x+{2}=0 ".format(a,b,c))
