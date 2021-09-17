print("Média da turma\n")
qtdVezes = 0
somaMedias = 0
qtdAlunos = int(input("Digite a quantidade de alunos na turma: \n"))
while(qtdVezes < qtdAlunos):
    nomeAluno = str.lower(input('Nome do aluno: '))
    nota1 = float(input('Digite a primeira nota: '))
    nota2 = float(input('Digite a segunda nota: '))
    mediaAluno = (nota1 + nota2) / 2
    print('Média do aluno:{:.2f}\n'.format(mediaAluno))
    somaMedias = somaMedias + mediaAluno
    qtdVezes = qtdVezes + 1
    mediaTurma = somaMedias / qtdAlunos
print('A média da turma é:{:.2f}'.format(mediaTurma))
