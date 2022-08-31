import math

path = 'out_10000.txt'

f = open(path, encoding="UTF-8")

obj = eval(f.read())

f.close()

kanjisum = 0

for elem in obj :
    kanjisum += elem[1]

obj.reverse()

f2 = open('./out_per.txt', 'w', encoding='UTF-8')
f3 = open('./kanjilist.txt', 'r', encoding='UTF-8')
kanjilist = [f3.read().split(",")]
print(f3.read())
f3.close()
print(len(kanjilist[0]))
kanjilist.append(kanjilist[0][0:80])
kanjilist.append(kanjilist[0][80:240])
kanjilist.append(kanjilist[0][240:440])
kanjilist.append(kanjilist[0][440:642])
kanjilist.append(kanjilist[0][642:835])
kanjilist.append(kanjilist[0][835:1026])
frequency = []
grade = []
elemperlist = [[],[],[],[],[],[]]
for elem in obj :
    if elem[0] in kanjilist[0]:
        elemper = elem[1]/(kanjisum/100)
        print(elem[0] + " " + str(round(elemper,3)) + " %")
        f2.write(elem[0] + " " + str(round(elemper,3)) + " %\n")

        frequency.append(elemper)
        for i in range(6) :
            if(elem[0] in kanjilist[i + 1]):
                grade.append(i + 1)
                elemperlist[i].append(math.log10(elemper) - 2)
f2.close()

from platform import freedesktop_os_release
import pandas as pd

df = pd.DataFrame({"学年[年生]":grade,
                   "出現頻度[%]":map(lambda x:math.log10(x) - 2, frequency),
                  })

import matplotlib.pyplot as plt
from matplotlib import rcParams

rcParams["font.family"]     = "sans-serif"
rcParams["font.sans-serif"] = "MS Gothic"

print(df.corr())

fig, ax = plt.subplots()
ax.boxplot((elemperlist))
plt.show()
fig.savefig("WikiBoxplot.png")
