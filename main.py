def citiredate():
    lst = []
    givenstring = input(" Dati datele problemei, separate prin virgula")
    numersasstring = givenstring.split(",")
    for x in numersasstring:
        lst.append(int(x))
    return lst


'''
2. Afisarea tuturor nr negtive din lista.
'''
def negative(lst):
    for i in range (len(lst)):
        if lst[i]<0:
            print(lst[i], " ")
'''
3.Afisarea celui mai mic nr care are ultima cif egala cu o cifra citita de la tastatura.

'''
def celmaimic(lst):
    n=int(input("Dati nr:"))
    minnr= 0
    for i in range (len(lst)):
        if lst[i]%10==n:
            if lst[i]<minnr:
                minnr=lst[i]
    print(lst[i])

'''
4.Superprime
'''
def isPrime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n >= 2:
        for i in range(2, n):
            if n % i == 0:
                return False
        return True



def is_superprime(lst):
    for i in range (len(lst)):
        while lst[i]>0:
            if isPrime(lst[i]) == True:
                lst[i]=lst[i]//10
        print(lst[i], " ")







def main():
    lst = []
    while True:
        print("1. Citire date.")
        print("2. Afisarea tuturor numerelor negative")
        print("3.Afisarea celui mai mic nr care are ultima cif egala cu o cifra citita de la tastatura.")
        print("4. Superprim")
        print("Pentru a inchide, introduce x")

        optiune = input("Alege optiunea")

        while True:
            printMenu()
            optiune = input("Dati optiunea: ")
            if optiune == "1":
                l = citire_lista()
            elif optiune == "2":
                l1 = negative(lst)
                print(l1[:])
            elif optiune == "3":
                l2 =  celmaimic(lst)
                print(l2[:])
            elif optiune == "4":
                is_superprime(lst)
                print(l3[:])
            elif optiune == "x":
                break


main()
exit(0)