from fermat_little_theorem_primality_check import is_prime

rsa220 = 2260138526203405784941654048610197513508038915719776718321197768109445641817966676608593121306582577250631562886676970448070001811149711863002112487928199487482066070131066586646083327982803560379205391980139946496955261

percentage_check = .98
i = 2
while (i < rsa220):
  if is_prime(percentage_check, i):
    print '{0} is prime'.format(i)
    x = rsa220 % i
    print 'remainder after division: {0}'.format(x)
    if x == 0:
      print 'FOUND DIVISOR'
      break
  i = i + 1
