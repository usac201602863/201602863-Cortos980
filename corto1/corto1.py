
print("Hola")
Collatz = 'collatz.txt'
N = 863
n = 2
#ln = []
archivo = open(Collatz, 'w')
def numeropar(num):
    #global p
    
    c = num%2
    if c == 0:
        #print("Es par")
        n = num//2
        #num += 1
        ln.append(n)
        #numeropar(num)
        buscaruno(n)

    else:
        #print("No es par")
        n = num*3+1
        #num += 1
        ln.append(n)
        buscaruno(n)
        #numeropar(num)
        
def buscaruno(n):
    if n!= 1:
        numeropar(n)


while(N>=n):
    print(n)
    ln=[n]
    numeropar(n)
    n += 1
    archivo.write(str(ln))
    archivo.write("\n")
    print(ln)
    del ln
archivo.close()

