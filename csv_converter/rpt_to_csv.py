'''
Abaqus rpt to csv converter
Author: ad2108
Version: 1.0
Date: 2025-04-05
License: MIT

Description:
    A simple script that converts the native rpt report files from Abaqus to csv.
'''

print("Csv converter:")
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
