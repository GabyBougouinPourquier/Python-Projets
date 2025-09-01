import random

nombre_aleatoir = random.randint(1, 10)
print()
print()
print()
print()
print("devine un chiffre entre 1 et 10")
print()

essai1 = 0

infini = True
boucle = True
while infini:

    while boucle:

        question = int(input("-> "))
        essai1 += 1
        if question > 10:
            print("tu dois entrés un chiffres entre 1 et 10  ! :(")

        elif question == nombre_aleatoir:
            if essai1 == 1:
                print("Bravo !")
                print()
                print("TU ES UN DIEU !!!")
                print()
                print("TU AS REUSSIS EN 1 ESSAI !!!")
                print()
                print(" ° °")
                print(" ___")
                print("|___|")
                essai1 = 0
                boucle = False
            elif essai1 == 2:
                print("Bravo !")
                print()
                print("TU ES TROP FORT !!!")
                print()
                print("TU AS REUSSIS EN 2 ESSAIS !!!")
                essai1 = 0
                boucle = False
            else:
                print("Bravo")
                print("Tu as réussis en " + str(essai1) + " essais !")
                essai1 = 0
                boucle = False

        elif question > nombre_aleatoir:
            print("Plus petit")
        elif question < nombre_aleatoir:
            print("Plus grand")


    nombre_aleatoir2 = random.randint(1, 10)
    print()
    print()
    print()
    print()
    print("devine un chiffre entre 1 et 10")

    essai2 = 0
    boucle2 = True
    while boucle2:
        question2 = int(input("-> "))
        essai2 += 1
        if question2 > 10:
            print("tu dois entrés un chiffres entre 1 et 10 ! :(")
        elif question2 == nombre_aleatoir2:
            if essai2 == 1:
                print("Bravo !")
                print()
                print("TU ES UN DIEU !!!")
                print()
                print("TU AS REUSSIS EN 1 ESSAI !!!")
                print()
                print(":)")
                print(";)")
                essai2 = 0
                boucle2 = False
            elif essai2 == 2:
                print("Bravo !")
                print()
                print("TU ES TROP FORT !!!")
                print()
                print("TU AS REUSSIS EN 2 ESSAIS !!!")
                essai2 = 0
                boucle2 = False
            else:
                print("Bravo")
                print("Tu as réussis en " + str(essai2) + " essais !")
                boucle2 = False

        elif question2 > nombre_aleatoir2:
            print("Plus petit")
        elif question2 < nombre_aleatoir2:
            print("Plus grand")
for infini in range(0, 10000000000):
    print(infini)

