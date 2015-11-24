import random

def is_mod_1(a, p):
  import pdb; pdb.set_trace()
  remainder = pow(a, p-1) % p
  return remainder == 1

def is_prime(attempts_percentage, n):
  attempts = int(attempts_percentage * n)
  for i in range(attempts):
    a = int(random.random() * (n - 1)) + 1
    if not is_mod_1(a, n):
      return False
  return True

def main():
  for i in range(2,400):
    print i
    print str(is_prime(.9, i))

if __name__ == '__main__':
  main()
