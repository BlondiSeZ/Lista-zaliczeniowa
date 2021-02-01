print ("!!!!pisz nazwy z polskimi znakami!!!!")
x = float(input("Ile bitów ma bajt? (podaj liczbę): "))
a = 0
if x == 8:
    a +=+1
    print ("git")
else:
    a += 0
    print("zle")

x = float(input("Jaki numerek ma najnowszy Iphone? (podaj liczbę): "))
if x == 12:
    a += 1
    print ("git")
else:
    a += 0
    print("zle")

x = input("Jaka jest najpopularniejsza wyszukiwarka? (podaj nazwę): ")
if x == ("google"):
    a += 1
    print ("git")
else:
    a += 0
    print("zle")

x = input("Darmowe oprogramowanie to? (freeware/shareware/trail): ")
if x == ("freeware"):
    a += 1
    print ("git")
else:
    a += 0
    print("zle")

x = input("Jakie rozszerzenie maja pliki graficzne? (pptx/jpg/doc): ")
if x == ("jpg"):
    a += 1
    print ("git")
else:
    a += 0
    print("zle")

x = input("Podstawowy edytor graficzny wbudowany w Windowsa to?: ")
if x == ("paint"):
    a += 1
    print ("git")
else:
    a += 0
    print("zle")

x = input("MP3 to format plikow(muzycznych/graficznych/tekstowych): ")
if x == ("muzycznych"):
    a += 1
    print ("git")
else:
    a += 0
    print("zle")

x = input("Co to Google Chrome? (skaner/przeglądarka/antywirus): ")
if x == ("przeglądarka"):
    a += 1
    print ("git")
else:
    a += 0
    print("zle")

x = input("Jak nazywamy ten znak '@' ? : ")
if x == ("małpa"):
    a += 1
    print ("git")
else:
    a += 0
    print("zle")

x = input("Producent windowsa? ")
if x == ("microsoft"):
    a += 1
    print ("git")
else:
    a += 0
    print("zle")

print("Twój wynik to", a,"/ 10")
if a >= 9:
    print("Twoja ocena to 5")
if a >= 7 and a < 9:
    print("Twoja ocena to 4")
if a >= 5 and a < 7:
    print("Twoja ocena to 3")
if a >= 3 and a < 5:
    print("Twoja ocena to 2")
if a < 3:
    print("Twoja ocena to 1")