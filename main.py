#needed libraries
import sys, os

#verifying if args in bash are ok
if len(sys.argv) < 2:
    print("Faltando argumentos!")
    exit()
elif len(sys.argv) > 2:
    print("Argumentos demais!")
    exit()
elif len(sys.argv) == 2:
    if os.path.isfile(sys.argv[1]):
        print("👍")
    else:
        print("O argumento não é um arquivo!")
        exit()

#since whatsapp exports a plain text chat delimiter is used to, guess what, delimite when a message starts and when It finishes.
delimiter = ''

#opens the file
fileobj = open(sys.argv[1], 'r')
words = fileobj.read().split(delimiter)
fileobj.close()

#converts everything to lowcase
words = [x.lower() for x in words]

#initializing variables
remove = 'a really big string so it won\'t have in your texts'
removelist = []


#hardcoded words to remove that you're sure you don't want to see
hardcodedwordstoremove = ['marketing', 'mídias sociais', 'midias sociais', 'parrilha', 'parrilheiro', 'cozinheiro', 'pedagogo', 'pedagogia', 'professora', 'experiência em clínicas', 'superior completo em administração', 'professor', 'salgadeiro', 'salgadeira', 'superior em ciências contábeis', 'atendente', 'vendedor', 'vendedora', 'sexo feminino', 'vendas', 'eletricista', 'licitações', 'segurança do trabalho', 'segurança de trabalho', 'babá', 'recepcionista', 'experiência na área imobiliária', 'designer', 'design gráfico', 'experiência', 'dexion', 'refrigeração', 'mestre de obras', 'licitação', 'autocad', 'auto cad', 'engenheiro', 'engenheira', 'mecanico', 'enfermagem', 'carpinteiro', 'serralheiro', 'menor aprendiz', 'camareira', 'terapeuta']

for x in hardcodedwordstoremove:
    words = [v for v in words if x not in v]

#notremovestrings
notremovestrings = ['técnico de ti', 'técnico em ti', 'aux admin', 'auxiliar administrativo', ' técnico de informática', 'tecnico de informatica', 'tecnico em ti', 'tecnico de ti', '']

#outputing all messages
print("Mensagens: ")
for x in words:
    print("---\n" + x + "\n---")
print("Total de mensagens: " + str(len(words)) + ".\n")

#while loop to close the program if "pronto" is typed.
while remove != "pronto":
    if remove == '-1':
        #if -1 is typed It removes the last message.
        words = words[:-1]
        #cleans terminal
        os.system('cls' if os.name == 'nt' else 'clear')
        #prints all the messages
        for x in words:
            print("---\n" + x + "\n---")
        print("Total de mensagens: " + str(len(words)) + ".\n")
        #asks user for a word to find and remove
        remove = input("Removedor: ")
    else:
        #removes messages containing certain word
        for i in words:
            for x in notremovestrings:
                if x not in i:
                    words = [x for x in words if remove not in x]
        
        #cleans terminal
        os.system('cls' if os.name == 'nt' else 'clear')
        #prints all the messages
        for x in words:
            print("---\n" + x + "\n---")
        print("Total de mensagens: " + str(len(words)) + ".\n")
        #asks user for a word to find and remove
        remove = input("Removedor: ")
        #appends the choosed word in a list. 
        removelist.append(remove)

#cleans terminal
os.system('cls' if os.name == 'nt' else 'clear')

#prints the list containing all words user asked to remove
print(removelist)