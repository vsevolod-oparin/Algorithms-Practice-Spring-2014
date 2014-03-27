def foo(x, y):
  # x > 0 and y > 0
  u, v = y, x

  while x != y:
    if x > y:
      x = x - y
      v = v + u
    else:  # y > x
      y = y - x
      u = u + v

  return (x + y) / 2, (u + v) / 2

