def gcd(a, b):
  if (a % b == 0):
    return b
  else:
    return gcd(b, a % b)

def lcm(a, b):
  return a * b // gcd(a, b)  

def manyLCM(a, b, n):
  if (n == b):
    return lcm(a, b)
  else:
    return manyLCM(lcm(a, b), b + 1, n)

def main():
  x = int(input("Enter first value: "))
  y = int(input("Enter second value: "))

  print(manyLCM(x, x+1, y))

main()
