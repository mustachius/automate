#! python3
# phoneAndEmail.py - Encontra número de telefones e endereços de e-mail salvos no clipboards

import pyperclip, re

phoneRegex = re.compile(r'''(
    (\d{2}|\(\d{2}\))?       # código de área
    (\s)?              # espaço entre o DDD e o número de telefones
    (\d{4})            # primeira parte do número de telefones
    (\s|-|)?            # hífen entre os números 
    (\d{4})             # segunda parte do número de telefone

)''', re.VERBOSE)

emailRegex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+   #username
    @                   # @
    [a-zA-Z0-9.-]+      # nome do domínio 
    (\.[a-zA-Z]{2,4})    # ponto alguma coisa 

)''', re.VERBOSE)

# Encontre todas as Regex no texto salvo do Clipboard

text = str(pyperclip.paste())
matches = []

for groups in phoneRegex.findall(text):
    matches.append(groups[0])
for groups in emailRegex.findall(text):
    matches.append(groups[0])

# Copiando os resultados para o Clipboard

if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copiado para o clipboard')
    print('\n'.join(matches))
else:
    print('Nenhum número de telefone ou email encontrado') 