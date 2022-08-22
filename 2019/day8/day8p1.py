with open("input.txt") as f:
    data = f.read()

#print(data)
width = 25
height = 6
size = width * height
layer_num = len(data)//size
layers = []
for i in range(layer_num):
    layers += [data[i*size:i*size+size]]


layers.sort(key=lambda x:x.count('0'))
print([i.count('0') for i in layers])
print(layers[0].count('1') * layers[0].count('2'))

image = []
for i in layers:
    temp = []
    for h in range(height):
        temp += [i[h:h+width]]
    image += [temp]

#print(image)