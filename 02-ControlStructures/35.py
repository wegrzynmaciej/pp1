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
            result = "Równanie {0}x^2+{1}x+{2}=0 ".format(a,b,c)
            a = float(a)
            b = float(b)
            c = float(c)
            delta = b**2-4*a*c
            if delta == 0:
                x0 = (-b)/2*a
                result += "ma jedno rozwiązanie {0}".format(x0)   
                print(result)
            elif delta < 0:
                result += "nie ma rozwiązań"
            else:
                x1 = ((-b)-sqrt(delta))/2*a
                x2 = ((-b)+sqrt(delta))/2*a
                result += "ma 2 rozwiązania: {0} oraz {1}".format(x1,x2)
            print(delta)
            print(result)