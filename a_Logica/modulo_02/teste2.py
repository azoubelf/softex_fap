

aprovados_turma_1 = 0
aprovados_turma_2 = 0
aprovados_turma_3 = 0
aprovados_turma_4 = 0

melhor_aluno_turma_1 = 0
melhor_aluno_turma_2 = 0
melhor_aluno_turma_3 = 0
melhor_aluno_turma_4 = 0


maior_nota_turma_1 = 0
maior_nota_turma_2 = 0
maior_nota_turma_3 = 0
maior_nota_turma_4 = 0

maior_nota_todas = 0
melhor_aluno = ""


#quantos, de quais turmas, maior nota turma, maior nota todas

print("\nPrimeira turma")
for i in range(3):
    nome = input("Nome do aluno: ")
    nota = float(input("Nota do aluno: "))
    if nota >= 7:
        aprovados_turma_1 += 1

    if nota > maior_nota_turma_1:
        maior_nota_turma_1 = nota
        melhor_aluno_turma_1 = nome

    if nota > maior_nota_todas:
        maior_nota_todas = nota
        melhor_aluno = nome

print("\nSegunda turma")
for i in range(3):
    nome = input("Nome do aluno: ")
    nota = float(input("Nota do aluno: "))
    if nota >= 7:
        aprovados_turma_2 += 1

    if nota > maior_nota_turma_2:
        maior_nota_turma_2 = nota
        melhor_aluno_turma_2 = nome
    
    if nota > maior_nota_todas:
        maior_nota_todas = nota
        melhor_aluno = nome

print("\nTerceira turma")
for i in range(3):
    nome = input("Nome do aluno: ")
    nota = float(input("Nota do aluno: "))
    if nota >= 7:
        aprovados_turma_3 += 1

    if nota > maior_nota_turma_3:
        maior_nota_turma_3 = nota
        melhor_aluno_turma_3 = nome

    if nota > maior_nota_todas:
        maior_nota_todas = nota
        melhor_aluno = nome

print("\nQuarta turma")
for i in range(3):
    nome = input("Nome do aluno: ")
    nota = float(input("Nota do aluno: "))
    
    if nota >= 7:
        aprovados_turma_4 += 1

    if nota > maior_nota_turma_4:
        maior_nota_turma_4 = nota
        melhor_aluno_turma_4 = nome

    if nota > maior_nota_todas:
        maior_nota_todas = nota
        melhor_aluno = nome



print(f"\nTurma 01 - Aprovados: {aprovados_turma_1}")
print(f"Turma 02 - Aprovados: {aprovados_turma_2}")
print(f"Turma 03 - Aprovados: {aprovados_turma_3}")
print(f"Turma 04 - Aprovados: {aprovados_turma_4}")

print(f"\nMelhor aluno da turma 01: {melhor_aluno_turma_1}")
print(f"Melhor nota da turma 01: {maior_nota_turma_1}")
print(f"Melhor aluno da turma 02: {melhor_aluno_turma_2}")
print(f"Melhor nota da turma 02: {maior_nota_turma_2}")
print(f"Melhor aluno da turma 03: {melhor_aluno_turma_3}")
print(f"Melhor nota da turma 03: {maior_nota_turma_3}")
print(f"Melhor aluno da turma 04: {melhor_aluno_turma_4}")
print(f"Melhor nota da turma 04: {maior_nota_turma_4}")

print(f"\nMelhor aluno: {melhor_aluno}")
print(f"Maior nota: {maior_nota_todas}")


