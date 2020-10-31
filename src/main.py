import random

inp = input()
passwd = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 
          'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
          'u', 'v', 'w', 'x', 'y', 'z']
sol = ''
num = 0
while inp != sol:
  sol = ''
  num += 1
  for i in range(len(inp)):
    cr = random.choice(passwd)
    sol = str(cr) + str(sol)
  print(sol, "Test case:", num)
print("The password is:",sol)
