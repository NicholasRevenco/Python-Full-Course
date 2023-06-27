
file = open("input.txt")
x = file.readlines()
x = [line.strip() for line in x]
file.close()


dictionary = {}
for i in range(len(x)-1):
  if i % 2 == 1:
    dictionary[x[i]] = x[i-1]

print(dictionary)