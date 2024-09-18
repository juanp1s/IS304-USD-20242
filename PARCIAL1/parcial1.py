class NumerosPrimos:
    def __init__(self, limite):
        self.limite = limite

    def es_primo(self, num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    def obtener_primos(self):
        primos = []
        for num in range(2, self.limite + 1):
            if self.es_primo(num):
                primos.append(num)
        return primos


def main():
    limite = int(input("Introduce un número entero: "))
    numeros_primos = NumerosPrimos(limite)
    primos = numeros_primos.obtener_primos()
    print("Números primos menores o iguales a", limite, ":", primos)


if __name__ == "__main__":
    main()
