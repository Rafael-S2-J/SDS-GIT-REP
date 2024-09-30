paciente = input("NOME DO PACIENTE: ")
DtDeNasc = int(input("ANO DE NASCIMENTO: "))
qntSin = int(input("POSSUI QUANTOS SINTOMAS? "))
if qntSin >0:
    grau = input("QUAIS FORAM SINTOMAS: ") 

idade = 2024 - DtDeNasc

if qntSin>3:
    gr=("<<GRAU ALTO>>")
    
elif qntSin>2:
    gr=("<<GRAU MÉDIO>>")
    
elif qntSin>1:
    gr=("<<GRAU BAIXO>>")
    
elif qntSin==0:
    print("VOLTE PARA CASA VOCÊ ESTA BEM, SEU LOUCO")


while True:
    if idade<10:
        responsavel=input("NOME DO RESPONSAVEL: ")
        rgResponsavel=int(input("RG:"))
        print("<<PEDIATRIA>>")
        print("PACIENTE: " ,paciente)
        print("IDADE: ", idade)
        print("RESPONSAVEL: ",responsavel)
        print("RG: ", rgResponsavel)
        print(gr)
        break    
    
    elif idade<17:
        responsavel=input("NOME DO RESPONSAVEL: ")
        rgResponsavel=int(input("RG:"))
        print("<<CLINICA GERAL>>")
        print("PACIENTE: " ,paciente)
        print("IDADE: ", idade)
        print("RESPONSAVEL: ",responsavel)
        print("RG: ", rgResponsavel)
        print(gr)
        break
    
    elif idade>18:
        rg=int(input("RG: "))
        print("<<CLINICA GERAL>>")
        print("PACIENTE: " ,paciente)
        print("IDADE: ", idade)
        print("RG: ", rg)
        print(gr)
        break
    
    