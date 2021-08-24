import os
import re
s = '*\/:?"<>|--——（）《》() '
currentdir=os.getcwd()
files=os.listdir(currentdir)
for file in files:
    name = re.findall('[\u4e00-\u9fa5a-zA-Z0-9.]+', file, re.S)
    name = "".join(name)
    os.rename(file,name)
    print(file,'=====>',name)
