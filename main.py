from Logic.Cuenta import Cuenta


if __name__ == '__main__':
    saldoInicial = float(input("ingrese el saldo de Cuenta"))
    cuenta = Cuenta(saldoInicial)
    cuenta.interes()
    cuenta.printSaldo()