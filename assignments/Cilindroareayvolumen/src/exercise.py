import math

def area_cilindro(radio, altura):
    area_circulo= math.pi * radio**2
    area_pared= (2 * math.pi * radio) * altura

    return 2 * area_circulo + area_pared 

def volumen_cilindro(r, a):
    area_cilindro= math.pi * r**2
    return area_cilindro * a

def main():
    #escribe tu código abajo de esta línea
    radio= float(input('(radio)>>>'))
    altura= float(input('(altura)>>>'))

    area = area_cilindro(radio, altura)
    volumen = volumen_cilindro(radio, altura)

    print(f'area={area:.2f}')
    print(f'volumen={volumen:.2f}')


if __name__=='__main__':
    main()
