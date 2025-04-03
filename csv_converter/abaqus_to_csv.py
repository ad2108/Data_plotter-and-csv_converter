# to csv rewriter

print("Csv rewriter:")
print("To exit type exit")

while True:
  print("Name of the file:")
  name = input()
  if(name == "exit"):
    break

  file = open(name, "r")
  newfile = open(name.replace(".txt", ".csv").replace(".rpt", ".csv"), "w")


  unsorted = []
  for line in file:
      unsorted.append(line.replace(";", " ").replace(",", " ").split(" "))

  for element in unsorted:
      for value in element:
          if value != "":
              if value == '\n':
                  newfile.write(value)
              else:
                  newfile.write(value + ";")

  print("Converted")
