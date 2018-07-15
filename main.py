# Created by Gianfranco Romaelle, April 2018
import os
from time import sleep

from sympy import *
from sympy.parsing.sympy_parser import parse_expr, standard_transformations, implicit_multiplication_application, convert_xor

while True:
    try:

        x = Symbol('x')

        transformations = (standard_transformations + (implicit_multiplication_application, convert_xor))
        print("Press Ctrl + C to quit.")
        print("If you want to use constants 'e' or 'pi', write E * (function) or pi * (function)")

        f = parse_expr(input("Give me an equation: "), transformations=transformations)

        if f.is_constant() is True:
            raise AssertionError

        fprime = f.diff()
        f = lambdify(x, f)
        fprime = lambdify(x, fprime)
        newtons_expr = lambdify(x, x - (f(x) / fprime(x)))



        def newtons_method(guess, maxiter=15):
            approx = newtons_expr(guess)
            if float(Abs(approx - guess)) < 0.001:
                return approx
            elif maxiter is 0:
                raise AssertionError
            else:
                return newtons_method(approx, maxiter-1)

        try:
            print("A close estimate to one of the solutions to your equation: " + str(round(float(newtons_method(1)), 3)))
            input()
            os.system('cls' if os.name == 'nt' else 'clear')

        except (ZeroDivisionError, AssertionError):
            print('This equation either does not converge using Newton\'s method, or has no solutions.')
            sleep(2)
            os.system('cls' if os.name == 'nt' else 'clear')




    except ValueError or TypeError:
        print("Nah, I can't take that. My circuits say there is more than one variable letter here.")
        input()
        os.system('cls' if os.name == 'nt' else 'clear')

    except SyntaxError:
        print("You fat-fingered something.")
        input()
        os.system('cls' if os.name == 'nt' else 'clear')

    except AssertionError:
        print("This equation either does not converge using Newton\'s method, or has no solutions.")
        input()
        os.system('cls' if os.name == 'nt' else 'clear')

    except KeyboardInterrupt:
        quit()
