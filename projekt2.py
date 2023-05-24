"""

projekt2.py: Druhý projekt do Engeto Online Python Akademie

author: Lukáš Andrysík  

email: lukas@andrysik.cz

discord: lukasandrysik#4601

"""
import random

def generuj():
    tajnecislo = str()
    while len(tajnecislo)<4:
        x = str (random.randint(0,9))
        if len (tajnecislo) == 0 and x == 0:
            continue
        elif x in tajnecislo:
            continue
        else:
            tajnecislo += x
    return tajnecislo


def uvitani():

    
    print ("Hi there! \n ----------------------------------------------- \nI've generated a random 4 digit number for you. \nLet's play a bulls and cows game.\n-----------------------------------------------")



def zadani():
    zadane_cislo = input ("Enter a number:\n-----------------------------------------------\n")
    if not len (zadane_cislo) == 4:
        print ("Zadane cislo nema spravnou delku")
    elif zadane_cislo [0] == "0":
        print ('nesmí začínat "0"')
    elif not zadane_cislo.isnumeric():
        print ("Není to korektní čislo")
    elif not len (set(zadane_cislo)) == 4:
        print ("Nesmi obsahovat duplicity")
    return zadane_cislo




def pocitej(zadane_cislo, tajnecislo):
    bulls = 0
    cows = 0
# Dubug only!
#    print (f"Tajnecislo:{tajnecislo}, Zadanecislo: {zadane_cislo}")

    for counter, cislice in enumerate (zadane_cislo):

        if cislice == tajnecislo [counter]:
            bulls += 1

        elif cislice in tajnecislo :
            cows +=1
    return bulls, cows




uvitani ()
tajne_cislo = generuj ()
bulls = 0
pokusy = 0
while bulls != 4:

    zadane_cislo =  zadani()
    bulls, cows  = pocitej (zadane_cislo, tajne_cislo)
    pokusy += 1
    print(f"{bulls} bull{'s'[:bulls^1]}, {cows} cow{'s'[:cows^1]}")

print (f"Correct, you've guessed the right number in {pokusy} guesses!")

