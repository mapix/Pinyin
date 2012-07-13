
import os

sd = dict(tuple(line.split(',')) for line in open('pinyin.dic'))
print "load dict done"

for f in os.listdir("zhuyin"):
    wz, py = f.split('.')
    if sd[wz].strip() != py.strip():
        os.system("cat zhuyin/" + f + " >> wz_py.dic")
    else:
        print wz, py, sd[wz], "########"
print "Done"

