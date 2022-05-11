type_error_message = "Error: Tipo de dato no válido."
zero_division_message = "Error: No es posible dividir por cero."


def suma(num1, num2):
    try:
        num3 = num1 + num2
        return num3
    except TypeError:
        return type_error_message


def resta(num1, num2):
    try:
        num3 = num1 - num2
        return num3
    except TypeError:
        return type_error_message


def producto(num1, num2):
    try:
        num3 = num1 * num2
        return num3
    except TypeError:
        return type_error_message


def division(num1, num2):
    try:
        num3 = num1 / num2
        return num3
    except TypeError:
        return type_error_message
    except ZeroDivisionError:
        return zero_division_message
