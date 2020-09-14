def texto(a):
  return f'{a} bugs no software, pegue um deles e conserte... \nTecle “Ctrl+F5" '
def texto_1():
  return f'Vamos fazer mais um café!'
def main():
  for y in range(99, 251):
    bugs = texto(y)
    print(f'{bugs}')
  print(f'{texto_1()}')


if __name__=='__main__':
  main()    
