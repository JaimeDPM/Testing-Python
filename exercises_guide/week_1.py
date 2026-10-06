1                      # crear un objeto entero sin nombre
i = 1                  # ahora sí, con nombre
type(i)                # comprobar su tipo
i + 5                  # operar con enteros

import math            # importar un módulo
dir(math)              # ver qué contiene el módulo
help(math.ceil)        # ver la ayuda/documentación de una función
print(math.ceil(4.3))         # probarla

'spam'                 # crear un string sin nombre
'spam'.upper()         # llamar a un método con notación de punto

nota = 1               # asignar nombre a un objeto
a = 3
type(a)                # <class 'int'>
a = 'spam'             # reasignar la MISMA variable a otro tipo
type(a)                # <class 'str'>  → esto es el "tipado dinámico"

del a                  # borrar la variable

i = 999999999999999999999999
i * i                  # Python no pierde precisión con enteros grandes
i ** 5

f = 4.3
type(f)

c = 4 + 5j             # número complejo
1 + 4.3                # int + float → se convierte a float
1 + 4.3 + (4+5j)       # + complejo → se convierte a complex

int(4.9)               # trunca a 4
float(4)
complex(4.0)

3 / 6                  # división normal → 0.5
7 // 2                 # división entera
7 % 2                  # resto
2 ** 10                # potencia
abs(-5)                # valor absoluto

1 < 2                  # True
1 > 5                  # False
