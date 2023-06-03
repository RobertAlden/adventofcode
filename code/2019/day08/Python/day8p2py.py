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


#layers.sort(key=lambda x:x.count('0'))
#print([i.count('0') for i in layers])
print(layers)

image = []
for i in layers:
    temp = []
    for h in range(height):
        temp += [i[h:h+width]]
    image += [temp]

#print(image)
overlay = [list(i) for i in list(zip(*layers))]

final_image = []
for p in overlay:
    m = -1
    p = [x for x in p[::-1] if x != '2']
    final_image.append(p[-1])
final_image = "".join(final_image)
print(final_image)
f = []
for h in range(height):
    f += [final_image[h*width:h*width+width]]

for i in f:
    for c in i:
        if c == '0':
            print(' ',end="")
        else:
            print('X',end="")
    print("")