

def leer_numero(ini,fin,mensaje):
    value_to_return = None
    valid = True
    while valid:  # loop until the user enters a valid int
        try:
            x = int(input("{} : \n".format(mensaje)))
            if (x >= ini and x <= fin):
                value_to_return = x
            valid = True  # if this point is reached, x is a valid int
        except ValueError:
            print('Solo ingrese dígitos')


leer_numero(10,100,"mil")