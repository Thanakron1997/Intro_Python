# Counts Peaks with python
n = input()

data2 = list(map(int,n.split(' ')))
print(data2)

prev = data2[0] or 0.001
threshold = 0.5
peaks2 = []

for num, i in enumerate(data2[1:], 1):
    if (i - prev) / prev > threshold:
        peaks2.append(num)
    prev = i or 0.001
if len(peaks2) == 1:
    print(0)
else:
     print(len(peaks2))
