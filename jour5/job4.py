liste=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']



for j in range (len(liste)):
    liste.append(liste[j])
    
message=input('entrez le message a dechiffrer:')
clef=int(input('entrer la clef:'))
    
def chiffrement(lettre,liste,clef):
    for i in range(len(liste)):
        if lettre == ' ':
            return' '
        elif liste[i]==lettre:
            return str(liste[i+clef])


message_chiffrer= str()

for lettre in message:
    message_chiffrer += chiffrement(lettre,liste,clef)
print(message_chiffrer)
    