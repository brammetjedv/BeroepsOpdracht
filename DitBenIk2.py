
keuze = 0

print("wat wil je van me weten?")
print("A. mijn verjaardig")
print("B. mijn werkervaaring")
antwoord1 = input("A of B?")
if antwoord1 == "A" or antwoord1 == "a":
    print("Oke")
    keuze = 1
elif antwoord1 == "B" or antwoord1 == "b":
    print("Oke")
    keuze = 2


if keuze == 1:
    print("hoe oud denk je dat ik ben?")
    print("A. 16")
    print("B. 17")
    print("C. 18")
    antwoord2 = input("A, B of C?")
    if antwoord2 == "A" or antwoord2 == "a":
        print("ja dat klopt!")
    elif antwoord2 == "B" or antwoord2 == "b":
        print("nee helaas")
    elif antwoord2 == "C" or antwoord2 == "c":
        print("nope jammer!")
elif keuze == 2:
    print("waar denk je dat ik werk")
    print("A. Starbucks")
    print("B. Je werkt niet")
    print("C. Deliveroo")
    antwoord2 = input("A, B of C?")
    if antwoord2 == "C" or antwoord2 == "c":
        print("ja dat klopt!")
    elif antwoord2 == "B" or antwoord2 == "b":
        print("nee helaas")
    elif antwoord2 == "A" or antwoord2 == "a":
        print("nope jammer!")
 
 
