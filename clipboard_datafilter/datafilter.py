#Datasorter

import pandas as pd

print("Datafilter:")
print("Anfang:")
start = float(input())
print("Ende:")
end = float(input())
print("Schritt:")
step = float(input())
print("Abweichung:")
deviation = float(input())

#read form clipboard
data = pd.read_clipboard()

#create dataset to compare to
dataset = []

while(start <= end):
  dataset.append(start)
  start += step

#init output dataframe
dat = pd.DataFrame()

for i in dataset:
  sdata = data[data['0'] - i <= - deviation]
  sdata = data[data['0'] - i <= + deviation]
  new_row = sdata.tail(1)
  dat = dat._append(new_row, ignore_index=True)

#paste data to clipboard
dat.to_clipboard()
