def fact(n, p):
  alpha = 1
  k = 0
  for v in range(1, n + 1):
    beta = v
    while beta % p == 0:
      beta /= p
      k += 1
    alpha = alpha * beta % p
  return (alpha, k)
