# Created by Gianfranco Romaelle, April 2018
import os
from time import sleep

from sympy import *
from sympy.parsing.sympy_parser import parse_expr, standard_transformations, implicit_multiplication_application, convert_xor

while True:
    try:

        x = Symbol('x')

        transformations = (standard_transformations + (implicit_multiplication_application, convert_xor))
        print("If you want to use constants 'e' or 'pi', write E * (function) or pi * (function)")
        f = parse_expr(input("Give me an equation: "), transformations=transformations)

        fprime = f.diff()


        try:
            fprimeprime = fprime.diff()
            conTest = lambdify(x, Abs((f * fprimeprime) / (fprime) ** 2))

            if (conTest(1) > 1) or (f.is_constant() is True):
                raise AssertionError

        except AssertionError or ZeroDivisionError:
            print('This equation either does not converge using Newton\'s method, or has no solutions.')
            sleep(2)
            os.system('cls' if os.name == 'nt' else 'clear')

        else:

            f = lambdify(x, f)
            fprime = lambdify(x, fprime)

            newtons_expr = x - (f(x)/fprime(x))
            newtons_expr = lambdify(x, newtons_expr)

            def newtons_method(guess):
                approx1 = guess
                approx2 = float(newtons_expr(approx1))
                approx = True

                while float(Abs((approx2 - approx1))) > 0.001:
                    if (approx is True):        #if the approx is True, the program knows to change the value of approx1.
                        approx1 = newtons_expr(approx2)
                        approx = False
                    else:                       #if approx is False, the program knows to change the value of approx2.
                        approx2 = newtons_expr(approx1)
                        approx = True
                else:
                    if (approx is True):
                        return approx2          #...because the last value changed would have been approx2 when approx is True
                    else:
                        return approx1

            try:
                print("A close estimate to one of the solutions to your equation: " + str(round(float(newtons_method(1)), 3)))
                input()
                os.system('cls' if os.name == 'nt' else 'clear')

            except ZeroDivisionError:
                print('This equation either does not converge using Newton\'s method, or has no solutions.')
                sleep(2)
                os.system('cls' if os.name == 'nt' else 'clear')


    except ValueError or TypeError:
        print("Nah, I can't take that. My circuits say there is more than one variable letter here.")

    except SyntaxError:
        print("You fat-fingered something.")

    except KeyboardInterrupt:
        quit()



