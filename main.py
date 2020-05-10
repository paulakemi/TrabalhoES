import func

func.menu()

msg = str(input("Digite uma letra: "))

primo1 = 2
primo2 = 7

indexMsg = func.indexMsg( msg[:1] )

N = func.N( primo1, primo2 )
print("Seu N é {} ele é resultado do produto de dois numeros primos".format(N))

tetaN = func.tetaN( primo1, primo2 )
print("Seu teta(N) é {}".format(tetaN))

encriptKey = func.encriptKey( N, tetaN )
print("Essa é sua chave para encriptar {}".format(encriptKey))

encriptIndex = func.encript( indexMsg, encriptKey, N )

novaMsg = func.letraIndex( encriptIndex )
print("Essa é sua letra incriptada {}".format(novaMsg))

decriptKey = func.decriptKey( encriptKey, tetaN )
print("Essa é sua chave decriptar {}".format(decriptKey))

decript = func.decript( encriptIndex, decriptKey, N )

MsgDecriptada = func.letraIndex( decript )
print("Essa é sua letra depois de ser decriptada {}".format(MsgDecriptada))
