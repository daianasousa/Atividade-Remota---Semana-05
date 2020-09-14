def main():
  cont = 0
  cont1 = 0
  for conjunto in range(100):
    num = int(input('Digite aqui: '))
    if (num % 2) == 0:
      cont += 1
    else:
      cont1 += 1
  print(f'Voçê me informou {cont} números PARES é {cont1} números impares')

if __name__=='__main__':
  main()
