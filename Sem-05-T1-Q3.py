def main():
  soma = 0
  for num in range(100):
    numero = int(input('Digite um número: '))
    soma += numero
    media = soma / 100
  print(f'{media:.2f}')

if __name__=='__main__':
  main()  
