#Contar letras en un texto, variable tipo string
xx = text.replace('\n', ' ')
comp = set (xx)

for letra in list(comp):
    if not (',' in letra or '.' in letra or '”' in letra): 
     num = xx.count(letra)

     print("frec de "+letra + "=" + str(num))
