maximum=100
note=int(input("entrez une note:"))
for i in range(0, 100):
    if note<40:
        print("il a echoué")
        break
    else:
        print("il a reussit")
        break