def is_palindrome(n):
    """
    :param n: numar intreg
    :return: True daca numarul este palindrom, respectiv False daca numarul nu este palindrom
    Funtia calculeaza inversul numarului introdus
    Verifica daca este sau nu egal cu cel introdus de la tastatura

    """
    nr = n
    invers = 0

    while nr > 0:

        digit = nr % 10
        invers = invers * 10 + digit
        nr = nr // 10

    if n == invers:
        return True
    return False



def test_is_palindrome():
    """
    citim un numar de la tastatura

    """
    n = int(input("Introduceti numarul: "))
    if (is_palindrome(n)):
        print(f"Numarul {n} este palindrom.")
    else:
        print(f"Numarul {n} nu este palindrom.")

def is_prime(n):

    """

    :param n: int
    :return:  true daca n este prim si false daca nu.
    """

    if n < 2:
        return False
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            return False
    return True


def is_superprime(n):

    """
    
    :param n: Este de tipul int
    :return: Returneaza True daca numarul este superprim, False in caz contrar
    
    Functia inverseaza numarul, si dupa construieste unul nou din invers, cifra cu cifra
    In timpul constructiei acesta verifica daca numarul curent este prim
    Primalitatea este verificata cu ajutorul functiei is_prime(n)
    
    """
    nr = n
    invers = 0

    #prima inversiune
    while nr > 0:
        digit = nr % 10
        invers = invers * 10 + digit
        nr = nr // 10

    #reinitializarea variabilelor
    nr = invers
    invers = 0
    gresit = 1

    #a doua inversiune + verificare primalitate la fiecare pas
    while nr > 0 and gresit == 1:
        digit = nr % 10
        invers = invers * 10 + digit
        if is_prime(invers) == False:
            gresit = 0
        nr = nr // 10

    if gresit == 1:
        return True
    else:
        return False


def test_is_superprime():
    """
        citim un numar de la tastatura

    """

    n = int(input("Introduceti numarul: "))

    if is_superprime(n):
        print(f"Numarul {n} este superprim.")
    else:
        print(f"Numarul {n} nu este superprim.")


def main():
    while True:
        print("1. Verifica daca un numar este palindrom.")
        print("2. Verifica daca un numar este superprim.")
        print("x. Iesire din program - exit")

        optiune = input("Introduceti optiunea dorita:")

        if optiune == '1':
            test_is_palindrome()
        elif optiune == '2':
            test_is_superprime()
        elif optiune == 'x':
            break
        else:
            print("Optiune invalida! Reincercati!")
main()