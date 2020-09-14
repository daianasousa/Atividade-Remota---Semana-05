def main():
  maior = 0
  for n in range(100):
    n = int(input('Digite um número: '))
    if  n > maior:
        maior = n
  print(maior)
  
if __name__ =='__main__':
  main()
