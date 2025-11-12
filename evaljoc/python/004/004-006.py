# Definición de la clase Matematicas
class Matematicas:
    """
    Esta clase implementa tres métodos:
    1. redondeo(numero): redondea al entero más cercano
    2. techo(numero): redondea siempre hacia arriba
    3. suelo(numero): redondea siempre hacia abajo
    
    Nota: En el enunciado original había un error:
    decía "Si la parte decimal es menor que 0.5, redondear hacia abajo (al techo)"
    y "si no, redondear hacia arriba (al suelo)". Esto es incorrecto porque:
    - Techo siempre significa hacia arriba
    - Suelo siempre significa hacia abajo
    Por eso corregimos la definición: si decimal < 0.5 -> suelo; si >= 0.5 -> techo.
    """
    # Método que redondea al entero más cercano
    def redondeo(self, numero):
        parte_entera = int(numero)  # Parte entera del número
        parte_decimal = numero - parte_entera  # Parte decimal

        if numero >= 0:
            if parte_decimal < 0.5:
                return parte_entera
            else:
                return parte_entera + 1
        else:
            # En números negativos, el redondeo cambia de sentido
            if parte_decimal > -0.5:
                return parte_entera
            else:
                return parte_entera - 1

    # Método que redondea hacia arriba (techo)
    def techo(self, numero):
        parte_entera = int(numero)
        if numero > parte_entera:
            return parte_entera + 1
        else:
            return parte_entera

    # Método que redondea hacia abajo (suelo)
    def suelo(self, numero):
        parte_entera = int(numero)
        if numero < 0 and numero != parte_entera:
            return parte_entera - 1
        else:
            return parte_entera


# Creación de un objeto de la clase Matematicas
calc = Matematicas()

# Ejemplos prácticos
print("Redondear 4.7 al techo:", calc.techo(4.7))
print("Redondear 4.2 al suelo:", calc.suelo(4.2))
print("Redondear 4.7 con método redondeo:", calc.redondeo(4.7))
print("Redondear 4.2 con método redondeo:", calc.redondeo(4.2))
print("Redondear -3.6 con método redondeo:", calc.redondeo(-3.6))
