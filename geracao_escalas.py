# lista de oitavas com sustenidos e bemois
sustenidos = ['DO', 'DO#', 'RE', 'RE#', 'MI', 'FA', 'FA#', 'SOL', 'SOL#', 'LA', 'LA#', 'SI']
bemois = ['DO', 'REb', 'RE', 'MIb', 'MI', 'FA', 'SOLb', 'SOL', 'LAb', 'LA', 'SIb', 'SI']

def gerar_escala(fundamental, oitava, modo):
  escala = []
  # localizando a fundamental na oitava
  indice = oitava.index(fundamental)
  # definindo intervalos baseado no índice
  intervalos_maior = [0, 2, 4, 5, 7, 9, 11]
  intervalos_menor = [0, 2, 3, 5, 7, 8, 10]
  if modo != 'menor':
    modo = 'maior'

  for i in range(12):
    if indice > 11:
      indice = 0   
    if i in intervalos_maior and modo == 'maior':
      escala.append(oitava[indice])
    elif i in intervalos_menor and modo == 'menor':
      escala.append(oitava[indice])
    indice += 1

  # adicinando a oitava justa
  escala.append(fundamental)

  return escala 


fundamental = input('Digite a fundamental: ')
modo = input('Digite o modo [menor/maior]: ')

if fundamental in sustenidos and fundamental != 'FA':
  print(f'Escala: {gerar_escala(fundamental, sustenidos, modo)}')
elif fundamental in bemois:
  print(f'Escala: {gerar_escala(fundamental, bemois, modo)}')
else:
  print('Fundamental inválida!')