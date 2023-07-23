x, y = list(map(lambda x: float(x), input().split()))

def find_quadrant(x, y):

    if x == 0 and y == 0:
        print("Origem")

    if x > 0 and y > 0:
        print("Q1")
        return
    if x < 0 and y > 0:
        print("Q2")
        return
    if x < 0 and y < 0:
        print("Q3")
        return
    if x > 0 and y < 0:
        print("Q4")
        return 

    if x > 0 or x < 0 and y == 0:
        print("Eixo X")
        return
    if x == 0 and y > 0 or y < 0:
        print("Eixo Y")
        return

find_quadrant(x, y)
