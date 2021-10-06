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
    assert is_palindrome(123) is False
    assert is_palindrome(26) is False
    assert is_palindrome(88) is True
    assert is_palindrome(121) is True

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
    assert is_superprime(233) is True
    assert is_superprime(237) is False

    n = int(input("Introduceti numarul: "))

    if is_superprime(n):
        print(f"Numarul {n} este superprim.")
    else:
        print(f"Numarul {n} nu este superprim.")



def get_largest_prime_below(n):
    """
    
    :param n: int
    :return: primul numar prim mai mic decat n
    
    Functia porneste de la n-1 si verifica daca numarul este prim cu ajutorul functiei is_prime(n)
    Numerele sunt verificate in ordine descrescatoare
    Daca nu exista programul returneaza 0
    
    """

    nr = n-1
    while nr > 0:
        if is_prime(nr) == True:
            return nr
        nr = nr - 1
    return 0


def test_get_largest_prime_below():
    """   
    citim un numar de la tastatura
    
    """
    assert get_largest_prime_below(20) == 19
    assert get_largest_prime_below(25) != 19

    n = int(input("Introduceti numarul: "))

    rezultat = get_largest_prime_below(n)
    if rezultat != 0:
        print(f"Numarul {rezultat} este ultimul numar prim mai mic decat {n}.")
    else:
        print(f"Nu exista numar prim mai mic decat {n}.")




def main():
    """

    Functia main contine meniul de accesare a problemelor
    :return: NONE

    """


    while True:
        print("1. Verifica daca un numar este palindrom.")
        print("2. Verifica daca un numar este superprim.")
        print("3. Găsește ultimul număr prim mai mic decât numarul dat.")
        print("x. Iesire din program - exit")

        optiune = input("Introduceti optiunea dorita:")

        if optiune == '1':
            test_is_palindrome()
        elif optiune == '2':
            test_is_superprime()
        elif optiune == '3':
            test_get_largest_prime_below()
        elif optiune == 'x':
            break
        else:
            print("Optiune invalida! Reincercati!")
main()