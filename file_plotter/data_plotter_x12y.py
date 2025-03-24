# file sorter
import matplotlib.pyplot as plt

print("Abaqus txt plotter")
print("Name der Datei:")
name = input()
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
print("Legende 10 Beschriftung")
p10 = input()
print("Legende 11 Beschriftung")
p11 = input()
print("Legende 12 Beschriftung")
p12 = input()
print("Umrechnungsfaktor für x:")
faktorx = float(input())
print("Umrechnungsfaktor für y")
faktory = float(input())
print("x minimal:")
xmin = float(input())
print("x maximal:")
xmax = float(input())
print("y minimal:")
ymin = float(input())
print("y minimal:")
ymax = float(input())



# read and presort
data = open(name , "r")
unsorted = []
count = 1
for line in data:
    if count > 2:
        unsorted.append(line.replace("\n", " ").replace(";", " ").replace(",", " ").split(" "))
    count += 1

# x, y Zuweisung
x = []
y = []
z = []
a = []
b = []
c = []
d = []
e = []
f = []
g = []
h = []
i = []
j = []
for element in unsorted:
    count = 1
    for value in element:
        if value != "":
            match count % 13:
                case 1:
                    x.append(float(value) * faktorx)
                case 2:
                    y.append(float(value) * faktory)
                case 3:
                    z.append(float(value) * faktory)
                case 4:
                    a.append(float(value) * faktory)
                case 5:
                    b.append(float(value) * faktory)
                case 6:
                    c.append(float(value) * faktory)
                case 7:
                    d.append(float(value) * faktory)
                case 8:
                    e.append(float(value) * faktory)
                case 9:
                    f.append(float(value) * faktory)
                case 10:
                    g.append(float(value) * faktory)
                case 11:
                    h.append(float(value) * faktory)
                case 12:
                    i.append(float(value) * faktory)
                case 0:
                    j.append(float(value) * faktory)
            count += 1
        

#plot
plt.figure(dpi=1200)
plt.axis([xmin, xmax, ymin, ymax])
plt.plot(x, y, label=p1)
plt.plot(x, z, label=p2)
plt.plot(x, a, label=p3)
plt.plot(x, b, label=p4)
plt.plot(x, c, label=p5)
plt.plot(x, d, label=p6)
plt.plot(x, e, label=p7)
plt.plot(x, f, label=p8)
plt.plot(x, g, label=p9)
plt.plot(x, h, label=p10)
plt.plot(x, i, label=p11)
plt.plot(x, j, label=p12)
plt.title(titel)
plt.xlabel(x_achse)
plt.ylabel(y_achse)
plt.legend()
plt.grid()
plt.savefig(f"{name}.pdf")
