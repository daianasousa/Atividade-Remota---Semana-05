def texto(a):
  return f'{a} bugs no software, pegue um deles e conserte...'

def main():
  for y in range(99, 251):
    bugs = texto(y)
    print(f'{bugs}')

if __name__=='__main__':
  main()    
