entrada = list(map(lambda x: float(x), input().split()))

pesos = [2, 3, 4, 1]

soma_valores = 0
soma_pesos = sum(pesos)

for i in range(len(entrada)):
    soma_valores += entrada[i] * pesos[i]

media = soma_valores / soma_pesos

print(f"Media: {media:.1f}")

if media >= 7.0:
    print("Aluno aprovado.")
if media < 5.0:
    print("Aluno reprovado.")
if media >= 5.0 and media <= 6.9:
    print("Aluno em exame.")

    nota_exame = float(input())

    print(f"Nota do exame: {nota_exame:.1f}")

    nova_media = (media + nota_exame) / 2

    if nova_media >= 5.0:
        print("Aluno aprovado.")
        print(f"Media final: {nova_media:.1f}")
    if nova_media <= 4.9:
        print("Aluno reprovado.")
        print(f"Media final: {nova_media:.1f}")