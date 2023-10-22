from collections import Counter

data1 = 1+2+3+4+5

print(data1/5)

new_data = "Roy is coding"
data = Counter(new_data)
print(data)

new_list = data.items()
print(new_list)

#value = data.values()
#print(value)


xyz = "coding is fun"
abc = Counter(xyz)
print(abc)
data2 = abc.values()
print(data2)
