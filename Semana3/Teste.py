# calcular a raiz quadrade da expressão ax² + bx + c = 0

# báskara : x = -b +/- RAIZ²(b² - 4*a*c)
#               ________________________
#                        2 * a
# Se delta menor que zero deve imprimir não tem raizes reais
# se delta igual a zero deve imprimir que tem uma raiz real
# se delta maior que zero deve imprimir que tem 2 raizes reais e imprimir os valores

import math

def bask():    

    a = float(input("a = "))
    b = float(input("b = "))
    c = float(input("c = "))

    delta = b**2 - 4 * a * c   

    if (delta < 0):        
        return print("delta é", delta, "sendo < 0 então:\n Não tem raízes reais")

    else:
        x1 = (-b + math.sqrt(delta)) / (2 * a)
        x2 = (-b - math.sqrt(delta)) / (2* a)
        
        if (delta > 0):            
            print ("delta > 0 = ",delta)
            return print("As raízes de Báskara são: ",x1, "e", x2)
        
        else:            
            print ("\ndelta = ",delta ,"\nDelta sendo igual a zero tem raízes iguais.\n")
            return print("A raiz real é ", x1)
                        

    

