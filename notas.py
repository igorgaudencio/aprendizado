def media_notas():
    soma = 0
    media = 0

    nota1 = float ( input ( "Digite a primeira nota:") )
    nota2 = float ( input ( "Digite a segunda nota:") )
    nota3 = float ( input ( "Digite a terceira nota:") )

    soma = nota1 + nota2 + nota3
    media = soma/3

    print ( "nota = ", media )
    if media >= 7:
        print ("Aluno aprovado")
    
    else:
        print ("Aluno reprovado")
    return 0

media_notas()