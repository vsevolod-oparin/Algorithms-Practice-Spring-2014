def gcd(x, y):
  if x == y:
    return x
  if x % 2 == 0 and y % 2 == 0:
    return gcd(x / 2, y / 2) * 2
  if x % 2 == 0:
    return gcd(x / 2, y)
  if y % 2 == 0:
    return gcd(x, y / 2)
  return gcd(y, x - y) if x > y else gcd(x, y - x)
