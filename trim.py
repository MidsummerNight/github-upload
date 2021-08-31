import re

s_path = "G:\\200T-wire\\INT_X14Y100_wire.txt"
m_path = "G:\\200T-wire\\trimmed-raw.txt"
d_path = "G:\\200T-wire\\trimmed.txt"

origin = open(s_path, 'r', encoding = 'utf-8')
mid = open(m_path, 'w', encoding = 'utf-8')
target = open(d_path, 'w', encoding = 'utf-8')

wires = []

result = []

inter = re.compile('INT_X')

for line in origin:
    l = line.split()
    wires.append(l)

for w in wires:
    r = []
    l = len(w)
    counter = l - 3
    i = 3
    tuple_no = counter/3
    r.append(w[0:3])
    while i < len(w):
        if re.match(inter, w[i]):
            r.append(w[i:i+3])
        i = i + 3
    result.append(r)

for res1 in result:
    c = 0
    while c < len(res1):
        if c != len(res1) - 1:
            mid.writelines(str(res1[c]) + ' ')
        else:
            mid.writelines(str(res1[c]) + '\n')
        c = c + 1
'''
for line2 in mid2:
    l2 = line2.split("'").split(",")
    target.writelines(l2)
'''
#target.writelines(result)

origin.close()
mid.close()
target.close()


'''
for k in result:
    writestring = ''
    len_k = len(k)
    c1 = 0
    while c1 < len_k:
        for j in k:
            len_j = len(k)
            c2 = 0
            while c2 < len_j:
                if c2 != len_j - 1:
                    writestring = writestring + ' ' + j[c2] + " "
                    #target.writelines(j[c2] + '')
                else:
                    writestring = writestring + ' ' + j[c2] + "\n"
                    #target.writelines(j[c2] + '')
                c2 = c2 + 1
                target.writelines(writestring)
        c1 = c1 + 1
'''