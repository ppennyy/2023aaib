a = [1, 3, 5, 7, 9, 11, 13, 15, 17]
for i in range(4): # 上面寫法不好, 不應該寫死 數字的範圍
  print('第i個數字是', a[i] )
print('上面的迴圈不好, 下面的迴圈才會伸縮自如/全部都照顧到')
N = len(a) # 要先知道有幾個數字
for i in range(N): # 才能在 for迴圈裡,得到正確的range
  print('第i個數字是', a[i] )