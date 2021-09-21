def main():
    #escribe tu código abajo de esta línea
    s = 0
    c = 0

    while s < 1000:
        n = int(input())

        s = s + n
        c = c + 1 

    print(f'suma = {s}')
    print(f'cantidad de numeros = {c}')
    

if __name__=='__main__':
    main()
