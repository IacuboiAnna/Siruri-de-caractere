#PROGRAMEAZĂ! Se consideră şiruri de caractere formate din literele mari ale alfabetului latin şi spaţiu. 
#Elaboraţi un program care afişează şirurile în studiu după următoarele reguli:
#– fiecare literă de la ’A’ până la ’Y’ se înlocuieşte prin următoarea literă din alfabet;
#– fiecare literă ’Z’ se înlocuieşte prin litera ’A’;
#– fiecare spaţiu se înlocuieşte prin ’-’.
sir_initial=input('Dati un sir ce sa contina doar litere mari ale alfabetului latin si spatiu:')
sir_final=''
for i in sir_initial:
    if ord(i) in range(65,90):
        caracter1=chr(ord(i)+1)
        sir_final+=caracter1
    if ord(i)==90:
        caracter2=chr(65)
        sir_final+=caracter2
    if ord(i)==32:
        caracter3=chr(45)
        sir_final+=caracter3
print(sir_final)