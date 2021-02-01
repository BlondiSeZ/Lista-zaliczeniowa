print("'koniec' konczy operacje")
print("Wielkosci dyskow to: (megabajt(MB), gigabajt(GB), terabajt(TB)")
def bajty():
    a=b*0.9313
    a = round(a, 2)
    print ("Prawdziwa pojemnośc dysku to:",a , x)
while True:
    x = input("Wartość początkowa (MB, GB, TB): ")
    if x == 'koniec':
        break
    if x in ('MB' ,'GB', 'TB'):
        if x == 'MB':
            b = float(input("wielkośc dysku: "))
            bajty()
        if x == 'GB':
            b = float(input("wielkośc dysku: "))
            bajty()
        if x == 'TB':
            b = float(input("wielkośc dysku: "))

            bajty()
    else:
        print("Nieprawidłowy znak operacji!")