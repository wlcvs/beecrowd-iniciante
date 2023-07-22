entrada = float(input())
intervalos = [0, 25, 50, 75, 100]

def find_interval(entrada):
    if entrada < 0 or entrada > 100:
        print("Fora de intervalo")
        return

    for i in range(len(intervalos) - 1):
        if entrada == intervalos[i] or entrada == intervalos[i + 1]:
            print(f'Intervalo [{intervalos[i]},{intervalos[i + 1]}]')
            return
        if entrada > intervalos[i] and entrada <= intervalos[i + 1]:
            print(f'Intervalo ({intervalos[i]},{intervalos[i + 1]}]')
            return
        
        # print(intervalos[i], intervalos[i + 1])

find_interval(entrada)
