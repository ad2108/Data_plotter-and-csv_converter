# to csv rewriter

print("Csv rewriter:")
print("Name of the file:")
name = input()

file = open(name, "r")
newfile = open(name.replace(".txt", ".csv"), "w")


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
