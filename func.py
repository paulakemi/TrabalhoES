def menu():
  print("===========================")
  print("| Encript and decript RSA |")
  print("===========================")

def indexMsg( msg ):

  alfa = [
  'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'q', 'r', 's', 't', 'u',
  'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'v', 'w', 'x', 'y', 'z', 
  ]

  for letra in alfa:
    if letra == msg:
      return ( alfa.index(letra) + 1 )

def letraIndex( index ):

  alfa = [
  'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'q', 'r', 's', 't', 'u',
  'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'v', 'w', 'x', 'y', 'z', 
  ]

  return alfa[index-1]

def N( num1, num2 ):
  return (num1 * num2)

def tetaN( num1, num2 ):
  n = (num1-1)*(num2-1)
  return n

def remove_repetidos( lista ):
    l = []
    for i in lista:
        if i not in l:
            l.append(i)
    l.sort()
    return l

def encriptKey( num, tetaN ):

  lista = []
  for i in range(2, num):
    status = 0
    for c in range(2 , i+1):
      if ( i % c ) == 0:
        if ( num % c ) == 0:
          status = 1
    if status == 0:
      lista.append(i)

  lista = remove_repetidos(lista)

  for i in range(2, tetaN):
    status = 0
    for c in range(2 , i+1):
      if ( i % c ) == 0:
        if ( tetaN % c ) == 0:
          status = 1
    if status == 0:
      return i

def encript( indexMsg, encriptKey, N ):
  import math

  r = pow(indexMsg, encriptKey) % N

  return r

def decriptKey( encriptKey, tetaN ):

  c =0
  while True:
    c += 1
    if c != encriptKey:
      if ( ( encriptKey * c ) % tetaN ) == 1:
        break

  return c

def decript( encriptIndex, decriptKey, N ):
  import math

  r = pow(encriptIndex, decriptKey) % N

  return r
