# 1.2.1
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


# 1.2.2
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


# 1.2.3
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


# 2.2.1
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


# 2.2.2
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


# 2.2.3
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


# 3.2.1
def eh_entrada(entry):
  lowercase = 'abcdefghijklmnopqrstuvwxyz'
  # Whole entry 
  if not isinstance(entry, tuple):
    return False
  if len(entry) != 3:
    return False
  
  # Cifra
  if not isinstance(entry[0], str) or len(entry[0]) < 1:
    return False
  for c in entry[0]:
    if c not in (lowercase + '-'):
      return False
  
  # Cheksum
  if not isinstance(entry[1], str) or len(entry[1]) != 7:
    return False
  if entry[1][0] != '[' and entry[1][-1] != ']':
    return False
  for i in range(1, len(entry[1]) - 1):
    if entry[1][i] not in lowercase:
      return False
  
  # Number tuple
  if not isinstance(entry[2], tuple) or len(entry[2]) < 2:
    return False
  for n in entry[2]:
    if not isinstance(n, int) or n < 0:
      return False
  return True


# 3.2.2
def validar_cifra(cifra, checksum):
  letters = {}
  for c in cifra:
    if c != '-':
      if c not in letters:
        letters[c] = 1
      else:
        letters[c] += 1
  letters = dict(sorted(letters.items(), key=lambda x: x[1]*(1+ord('z')) - ord(x[0]), reverse=True))
  return ''.join(key for key in list(letters.keys())[:5]) == checksum[1:6]


# 3.2.3
def filtrar_bdb(input):
  if isinstance(input, list) and len(input) >= 1 and all(eh_entrada(tuple) for tuple in input):
    output = []
    for tuple in input:
      if not (validar_cifra(tuple[0], tuple[1])):
        output.append(tuple)
    return output
  raise ValueError('filtrar_bdb: argumento invalido')


# 4.2.2
def obter_num_seguranca(tuple):
  n = 0
  size = len(tuple)
  for i in range(size):
    for j in range(size):
      if n == 0 and tuple[i] - tuple[j] > 0:
        n = tuple[i] - tuple[j]
      elif i != j and tuple[i] - tuple[j] < n and tuple[i] - tuple[j] >= 0:
        n = tuple[i] - tuple[j]
  return n


# 4.2.3
def decifrar_texto(cifra, number):
  i = 0
  output = ''
  size = len(cifra)
  while i < size:
    if cifra[i] == '-':
      output += ' '
      i += 1
    else:
      if i % 2 == 0:
        n = 1
      elif i % 2 != 0:
        n = -1
      ascii = ord(cifra[i]) + (number % 26) + n
      if ascii > 122:
        ascii = ascii - 26
      elif ascii < 97:
        ascii = ascii + 26
      output += chr(ascii)  
      i += 1
  return output


# 4.2.4
def decifrar_bdb(input):
  output = []
  if isinstance(input, list):
    for tuple in input:
      if not eh_entrada(tuple):
        raise ValueError('decifrar_bdb: argumento invalido')
      else:
        output.append(decifrar_texto(tuple[0], obter_num_seguranca(tuple[2])))
  return output


# 5.2.1
def eh_utilizador(input):
  if not isinstance(input, dict):
    return False
  if not isinstance(input['name'], str) or len(input['name']) < 1:
    return False
  if not isinstance(input['pass'], str) or len(input['pass']) < 1:
    return False
  if len(input) != 3:
    return False
  if not isinstance(input['rule'], dict):
    return False
  if len(input['rule']) != 2:
    return False
  if not isinstance(input['rule']['vals'], tuple) or len(input['rule']['vals']) != 2:
    return False
  if not isinstance(input['rule']['char'], str) or len(input['rule']['char']) != 1:
    return False
  for i in range(2):
    if not isinstance(input['rule']['vals'][i], int) or input['rule']['vals'][i] < 0:
      return False
  if input['rule']['vals'][0] > input['rule']['vals'][1]:
    return False
  return True


# 5.2.2
def eh_senha_valida(string, rule):
  vogal_counter = 0
  char_counter = 0
  vogal = 'aeiou'
  for c in string:
    if c in vogal:
      vogal_counter += 1
    if c == rule['char']:
      char_counter += 1

  if vogal_counter < 3:
    return False
  
  if char_counter < rule['vals'][0] or char_counter > rule['vals'][1]:
    return False
  
  consecutive = False
  for i in range(len(string) - 1):
    if string[i] == string[i+1]:
      consecutive = True
      break
  if not consecutive:
    return False

  return True


# 5.2.3
def filtrar_senhas(input):
  output = []
  if not isinstance(input, list):
    raise ValueError('filtrar_senhas: argumento invalido')
  for d in input:
    if not eh_utilizador(d):
      raise ValueError('filtrar_senhas: argumento invalido')
    if not eh_senha_valida(d['pass'], d['rule']):
      output.append(d['name'])
  output.sort()
  return output