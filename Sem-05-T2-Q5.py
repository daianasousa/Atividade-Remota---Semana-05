def prestacao(a, b):
  return f'{a}x de R$ {b:.2f}'

def calculo( d, e):
  return d / e

def main():
  compra = float(input('Digite o valor do produto:R$ '))
  for p in range(1, 25):
    pagamento = calculo(compra, p)
    prestacao1= prestacao(p, pagamento)
    print(f'{prestacao1}')


if __name__=='__main__':
  main()
