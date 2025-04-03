# file sorter
import matplotlib.pyplot as plt

print("Abaqus txt plotter")
print("Name der Datei1:")
name1 = input()
print("Name der Datei2:")
name2 = input()
print("Name der Datei3:")
name3 = input()
print("Name der Datei4:")
name4 = input()
print("Name der Datei5:")
name5 = input()
print("Name der Datei6:")
name6 = input()
print("Name der Datei7:")
name7 = input()
print("Name der Datei8:")
name8 = input()
print("Name der Datei9:")
name9 = input()
print("Titel:")
titel = input()
print("X-Achsen Beschriftung")
x_achse = input()
print("Y-Achsen Beschriftung")
y_achse = input()
print("Legende 1 Beschriftung")
p1 = input()
print("Legende 2 Beschriftung")
p2 = input()
print("Legende 3 Beschriftung")
p3 = input()
print("Legende 4 Beschriftung")
p4 = input()
print("Legende 5 Beschriftung")
p5 = input()
print("Legende 6 Beschriftung")
p6 = input()
print("Legende 7 Beschriftung")
p7 = input()
print("Legende 8 Beschriftung")
p8 = input()
print("Legende 9 Beschriftung")
p9 = input()
print("Faktor für x:")
faktorx = float(input())
print("Faktor für y:")
faktory = float(input())
print("xmin:")
xmin = float(input())
print("xmax:")
xmax = float(input())
print("ymin:")
ymin = float(input())
print("ymax:")
ymax = float(input())


# read and presort
data1 = open(name1 , "r")
unsorted1 = []
count = 1
for line1 in data1:
    if count > 2:
        unsorted1.append(line1.replace("\n", " ").replace(";", " ").replace(",", " ").split(" "))
    count += 1

data2 = open(name2 , "r")
unsorted2 = []
count = 1
for line2 in data2:
    if count > 2:
        unsorted2.append(line2.replace("\n", " ").replace(";", " ").replace(",", " ").split(" "))
    count += 1

data3 = open(name3 , "r")
unsorted3 = []
count = 1
for line3 in data3:
    if count > 2:
        unsorted3.append(line3.replace("\n", " ").replace(";", " ").replace(",", " ").split(" "))
    count += 1

data4 = open(name4 , "r")
unsorted4 = []
count = 1
for line4 in data4:
    if count > 2:
        unsorted4.append(line4.replace("\n", " ").replace(";", " ").replace(",", " ").split(" "))
    count += 1

data5 = open(name5 , "r")
unsorted5 = []
count = 1
for line5 in data5:
    if count > 2:
        unsorted5.append(line5.replace("\n", " ").replace(";", " ").replace(",", " ").split(" "))
    count += 1

data6 = open(name6 , "r")
unsorted6 = []
count = 1
for line6 in data6:
    if count > 2:
        unsorted6.append(line6.replace("\n", " ").replace(";", " ").replace(",", " ").split(" "))
    count += 1

data7 = open(name7 , "r")
unsorted7 = []
count = 1
for line7 in data7:
    if count > 2:
        unsorted7.append(line7.replace("\n", " ").replace(";", " ").replace(",", " ").split(" "))
    count += 1

data8 = open(name8 , "r")
unsorted8 = []
count = 1
for line8 in data8:
    if count > 2:
        unsorted8.append(line8.replace("\n", " ").replace(";", " ").replace(",", " ").split(" "))
    count += 1

data9 = open(name9 , "r")
unsorted9 = []
count = 1
for line9 in data9:
    if count > 2:
        unsorted9.append(line9.replace("\n", " ").replace(";", " ").replace(",", " ").split(" "))
    count += 1


# x, y Zuweisung
x1 = []
x2 = []
x3 = []
x4 = []
x5 = []
x6 = []
x7 = []
x8 = []
x9 = []
y = []
z = []
a = []
b = []
c = []
d = []
e = []
f = []
g = []
for element1 in unsorted1:
    count = 1
    for value1 in element1:
        if value1 != "":
            if count % 2 == 1:
                x1.append(float(value1) * faktorx)
            elif count % 2 == 0:
                y.append(float(value1) * faktory)
            count += 1

for element2 in unsorted2:
    count = 1
    for value2 in element2:
        if value2 != "":
            if count % 2 == 1:
                x2.append(float(value2) * faktorx)
            elif count % 2 == 0:
                z.append(float(value2) * faktory)
            count += 1

for element3 in unsorted3:
    count = 1
    for value3 in element3:
        if value3 != "":
            if count % 2 == 1:
                x3.append(float(value3) * faktorx)
            elif count % 2 == 0:
                a.append(float(value3) * faktory)
            count += 1

for element4 in unsorted4:
    count = 1
    for value4 in element4:
        if value4 != "":
            if count % 2 == 1:
                x4.append(float(value4) * faktorx)
            elif count % 2 == 0:
                b.append(float(value4) * faktory)
            count += 1


for element5 in unsorted5:
    count = 1
    for value5 in element5:
        if value5 != "":
            if count % 2 == 1:
                x5.append(float(value5) * faktorx)
            elif count % 2 == 0:
                c.append(float(value5) * faktory)
            count += 1

for element6 in unsorted6:
    count = 1
    for value6 in element6:
        if value6 != "":
            if count % 2 == 1:
                x6.append(float(value6) * faktorx)
            elif count % 2 == 0:
                d.append(float(value6) * faktory)
            count += 1

for element7 in unsorted7:
    count = 1
    for value7 in element7:
        if value7 != "":
            if count % 2 == 1:
                x7.append(float(value7) * faktorx)
            elif count % 2 == 0:
                e.append(float(value7) * faktory)
            count += 1

for element8 in unsorted8:
    count = 1
    for value8 in element8:
        if value8 != "":
            if count % 2 == 1:
                x8.append(float(value8) * faktorx)
            elif count % 2 == 0:
                f.append(float(value8) * faktory)
            count += 1


for element9 in unsorted9:
    count = 1
    for value9 in element9:
        if value9 != "":
            if count % 2 == 1:
                x9.append(float(value9) * faktorx)
            elif count % 2 == 0:
                g.append(float(value9) * faktory)
            count += 1
#plot
plt.figure(dpi=1200)
plt.axis([xmin, xmax, ymin, ymax])
plt.plot(x1, y, label=p1)
plt.plot(x2, z, label=p2)
plt.plot(x3, a, label=p3)
plt.plot(x4, b, label=p4)
plt.plot(x5, c, label=p5)
plt.plot(x6, d, label=p6)
plt.plot(x7, e, label=p7)
plt.plot(x8, f, label=p8)
plt.plot(x9, g, label=p9)
plt.title(titel)
plt.xlabel(x_achse)
plt.ylabel(y_achse)
plt.legend()
plt.grid()
plt.savefig(f"{name1}.pdf")
