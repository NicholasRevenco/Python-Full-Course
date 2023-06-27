file = open("input_no_punctuation.txt")
x = file.readlines()
x = [line.strip() for line in x]
file.close()

sentence = ""
for i in range(len(x)):
  for j in range(len(x[i])):
    if j == 0:
      take = x[i][0]
    else: 
      if x[i][j] == " ":
        sentence += take + "ay "
        take = x[i][j+1]
      elif j == len(x[i])-1:
        sentence += x[i][j] + take + "ay "
      elif take != x[i][j]:
        sentence += x[i][j]
  sentence += "\n"
new = open("output_no_prunctuation.txt", "w+")
new.write(sentence + "\n")
new.close()
print(sentence)