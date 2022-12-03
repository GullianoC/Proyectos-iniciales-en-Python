

from cmath import sqrt
# Exercise 10 - Fibonacci

"""

Create a function that returns a specific member of the Fibonacci sequence:

> A series of numbers in which each number ( Fibonacci number ) is the sum of the two preceding numbers. The simplest is the series 1, 1, 2, 3, 5, 8, etc.

fibonacci(4) // returns the 4th member of the series: 3  (1, 1, 2, 3)

"""
#Se define la función fibonnaci

def fibonnaci(n):
    n = int(n)
    if n < 0:
        return(print("OOPS"))
    fiboden = (2**n *sqrt(5)).real
    fibonum = (((1+sqrt(5))**n) - ((1-sqrt(5))**n)).real
    fibonnaciResultado = fibonum/fiboden
    return(print(round((fibonnaciResultado))))
    
#Se inicia la función fibonnaci

print("Se prueba la función de fibonnaci")

#i) 4th fibonacci number is 3
fibonnaci(4)
#ii) 6th fibonacci number is 8
fibonnaci(6)
#iii) 10th fibonacci number is 55
fibonnaci(10)
#iv) 15th fibonacci number is 610
fibonnaci(15)
#v) 25th fibonacci number is 75025
fibonnaci(25)
#vi) doesn\'t accept negatives
fibonnaci(-25)
#vii) DOES accept strings (1 para obtener 1)
fibonnaci("1")
#viii) DOES accept strings (2 para obtener 1)
fibonnaci("2")
#ix)'DOES accept strings (8 para obtener 21)
fibonnaci("8")


    


