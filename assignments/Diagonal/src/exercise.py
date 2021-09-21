import math 
def main():
    #escribe tu código abajo de esta línea
    largo=float(input('(largo)>>>'))
    ancho=float(input('(ancho)>>>'))

    diagonal= math.sqrt(largo**2 + ancho**2)

    print(diagonal)

if __name__=='__main__':
    main()
