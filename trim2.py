import re

m_path = "G:\\200T-wire\\trimmed-raw.txt"
d_path = "G:\\200T-wire\\trimmed.txt"

mid = open(m_path, 'r', encoding = 'utf-8')
target = open(d_path, 'w', encoding = 'utf-8')

#r1 = re.compile("[],'+")

for line2 in mid:
    l2 = line2.replace(',', " ")
    l2 = l2.replace("'", "")
    l2 = l2.replace("] [", "] : [")
    target.writelines(l2)

mid.close()
target.close()