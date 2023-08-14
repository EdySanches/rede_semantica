# biblioteca
from pyswip import Prolog, registerForeign

# variaveis globais
assert_string = []
query_string = []
splited_assert = []
verb_dif = []
subj_dif=[]

# objeto prolog
prolog = Prolog()

print("-------- BASE DE CONHECIMENTO --------")


# ---------------------------------------- ESCRITA DO PROLOG ---------------------------------------- #
print("----- CADASTRO -----") 

# contagem de linhas
f = open("rede.txt", "r")
cont_lines = len(f.readlines())
f.seek(0,0)

print("Cadastrando um total de " + str(cont_lines) + " sentencas...\n")

# leitura do arquivo da rede
for i in range(cont_lines):
    splited_assert = f.readline().strip("\n").split(",")
    subj1_ass = splited_assert[0]
    verb_ass = splited_assert[1]
    subj2_ass = splited_assert[2]
    assert_string.append(str(verb_ass + "(" + subj1_ass + ", " + subj2_ass + ")"))
    #print("entrada: " + assert_string[i])

    if verb_ass not in verb_dif:
        verb_dif.append(verb_ass)
    if subj1_ass not in subj_dif:
        subj_dif.append(subj1_ass)
    if subj2_ass not in subj_dif:
        subj_dif.append(subj2_ass)

    # cadastrando na sujeitos e relacoes na base de conhecimento 
    prolog.assertz(verb_ass + "(" + subj1_ass + ", " + subj2_ass + ")")


# ---------------------------------------- CONSULTA DO PROLOG ---------------------------------------- #
print("----- CONSULTA -----") 

verif = input("Deseja realizar uma consulta? (y/n) \n")

while verif == "y":
    # obtencao da query 
    query_s = input("Insira uma palavra para consulta: \n")    
    
    # se a query for um sujeito
    if query_s in subj_dif:
        print("Consulta por sujeito:")
        # a cada verbo
        for i in range(len(verb_dif)):
            # consulta como sujeito 1
            search = list(prolog.query(verb_dif[i] + "(" + query_s + ",X)"))
            if search != []:
                #print("encontrou 1" + str(search))
                for j in range(len(subj_dif)):
                    #print("sujeito 1: " + subjs[j])
                    if subj_dif[j] in str(search):
                        print(query_s + " " + verb_dif[i] + " " + subj_dif[j])

            # consulta como sujeito 2
            search = list(prolog.query(verb_dif[i] + "(X," + query_s + ")"))
            if search != []:
                #print("encontrou 2"+ str(search))
                for j in range(len(subj_dif)):
                    #print("sujeito 2: " + subjs[j])
                    if subj_dif[j] in str(search):
                        print(subj_dif[j] + " " + verb_dif[i] + " " + query_s)

    # se a query for um verbo
    elif query_s in verb_dif:
        print("Consulta por relacao:")
        verb_search = query_s + "(X,Y)"
        for soln in prolog.query(verb_search): 
            print(soln["X"], str(query_s), soln["Y"])

    # se a query nao for reconhecida
    else:
        print("Esta palavra nao foi cadastrada nem como sujeito e nem como relacao!")

    verif = input("\nDeseja realizar uma nova consulta? (y/n)\n")

if verif == "n":
    print("Programa finalizado...")