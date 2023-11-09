def corrigir_palavra(str):
  modified = False
  for i in range(0, len(str) - 1):
    if str[i].upper() == str[i+1].upper():
      if (str[i].isupper() and str[i+1].islower()) or (str[i].islower() and str[i+1].isupper()):
        str = str[:i] + str[i+2:]
        modified = True
        return corrigir_palavra(str)
  if not modified:
    return str


def eh_anagrama(str1, str2):
  return sorted(str1.upper()) == sorted(str2.upper())


def check_arg(string):
  if not isinstance(string, str):
    return False
  if len(string) < 1:
    return False
  for i in range(0, len(string)):
      if not string[i].isalpha() and string[i] != " ":
        return False
  for i in range(0, len(string) - 1):
    if string[i] == " " and string[i+1] == " ":
      return False
  return True


def corrigir_doc(str = None):
  if check_arg(str):
    texto = []
    palavra = ""
    for i in range(0, len(str)):
      if str[i] == " ":
        texto.append(corrigir_palavra(palavra))
        palavra = ""
      else:
        palavra += str[i]
    
    anagramas = []  
    x = 0
    while x < len(texto):
      z = x + 1
      while z < len(texto):
        # só anagramas em que a sequencia de letras é diferente
        if eh_anagrama(texto[x], texto[z]) and texto[x] != texto[z]:
          if texto[z].upper() not in anagramas:
            anagramas.append(texto[z].upper())
            texto.remove(texto[z])
          x = 0
        else:
          z += 1
      x += 1
    novo = ""
    for i in range(len(texto)):
      if i == len(texto) - 1:
        novo += texto[i]
      else:
        novo += texto[i] + " "
    return novo
  raise ValueError('corrigir_doc: argumento invalido')


def obter_posicao(move, pos):
  stay = {
    1:["E","C"],
    2:"C",
    3:["D","C"],
    4:"E",
    6:"D",
    7:["E","B"],
    8:"B",
    9:["D","B"]
  }

  if pos != 5 and move in stay[pos]:
    return pos
  else:
     if move == "E":
       return pos - 1
     elif move == "D":
       return pos + 1
     elif move == "C":
       if pos == 5:
         return pos - 3
       return pos - 3
     elif move == "B":
       if pos == 5:
         return pos + 3
       return pos + 3


def obter_digito(move, pos):
  for c in move:
    pos = obter_posicao(c, pos)
  return pos


def check_pin(moves):
  if not isinstance(moves, tuple):
    return False
  if len(moves) < 4 or len(moves) > 10:
    return False
  for move in moves:
    if len(move) < 1:
      return False
    for c in move:
      if not isinstance(c, str) or c not in ["C", "B", "D", "E"]:
        return False
  return True

def obter_pin(moves):
  if check_pin(moves):
    pos = 5
    pin = ()
    for move in moves:
      pos = obter_digito(move, pos)
      pin += (pos,)
    return pin
  else:
    raise ValueError('obter_pin: argumento invalido')

def eh_entrada(entry): # string, array em string, tuplo de inteiros
  print(entry[0])
  if len(entry) != 3 and not isinstance(entry, str):
    return False
  for i in range(0, len(entry[0])):
    if not entry[0][i].isalpha() and entry[0][i] != '-':
      return False
  return True

print(eh_entrada((('aaaa-bbb'), 1, 2)))