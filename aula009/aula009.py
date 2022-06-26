frase = 'Curso em Video Python'
#Análise com len(), count(), find(), transformações com replace()
# , upper(), lower(), capitalize(), title(), strip(), junção com join().
###########FATIAMENTO################
print(frase[9])#começa apenas no 9 #V
print(frase[9:13])#cadeia do 9 ao 13 #Vide
print(frase[9:21])#cadeia do 9 ao 21 #frase toda
print(frase[9:21:2])#saltando de 2 em dois do 9 ao 21
print(frase[:5])#começa do caractere 0 até o 5
print(frase[15:])#começa do 15 até o final
print(frase[9::3])#começa do 9 até o final pulando 3
############ANALISE###################
#####METODOS###############
print(len(frase))#numero de caracteres na str
print(frase.count("o"))#conta quantas vezes tem a str especifica
print(frase.count("o",0,13))#entre o caractere 0 ao 13
print(frase.find("deo"))#em que momento começou
print(frase.find("Android"))#retorna valor -1,entao nao existe
print("Curso"in frase )#valor booleano retorna True
#######TRANSFORMAÇÃO#################
####METODOS################
print(frase.replace("Python","Android"))#substitui uma str
print(frase.upper())#toda frase vai fica maiuscula
print(frase.lower())#toda frase vai fica mminuscula
print(frase.capitalize())#todos os caracteres minusculos e so a primeira letra maiuscula
print(frase.title())#transforma toda quebra de palavra em maiusculo
#####################################
frase1 = "   Aprenda Python  "
print(frase1.strip())#remove os primeiros e ultimos espaços
print(frase1.rstrip())#remove os espaços da direita e mantem os da esquerda
print(frase1.lstrip())#remove os espaços da esquerda e mantem os da direita
#########DIVISÃO##############
print(frase.split())#divide a str em uma lista
#########JUNÇÃO################
print('-'.join(frase))#ge