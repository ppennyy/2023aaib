# 31 28 31 30 31 30 31  31 30 31 30 31
# Big   big   Big   Big Big   Big   Big
#    28    Small Small     Small Small
a = int(input())
if a==2: print(28,end='')
elif a==4 or a==6 or a==9 or a==11: print(30,end='')
else:print(31,end='')