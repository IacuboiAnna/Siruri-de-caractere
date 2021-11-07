s=input('Dati sirul:')
print('Numarul de aparitii a caracterului ''A'' in sirul s este:', s.count('A')) #a 
print('Sirul obtinut prin inlocuirea caracterului "A" cu caracterul "*" este:', s.replace('A','*')) #b
print('Sirul obtinut prin radierea tuturor aparitiilor a caracterului "B" este:', s.replace('B','')) #c
print('Numarul de aparitii a silabei "MA" in sirul s este:', s.count('MA')) #d
print('Sirul obtinut prin substituirea tuturor aparitiilor silabei "MA" cu silaba "TA" este:', s.replace('MA','TA')) #e
print('Sirul obtinut prin radierea tuturor apritiilor a silabei "TO" este:', s.replace('TO','')) #f
print('Sirul s scris invers:', s[::-1]) #g