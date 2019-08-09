import pandas as pd
import array
import time

# df = pd.DataFrame({'mm':[]})
# # df = pd.DataFrame({'YD': [], 'MT': [], 'Index': []})
# a = array.array('d',(0 for i in range(0,10)))
# a[1] =20.3232323
# print(a)
# for j in range(10):
#     df = df.append({'mm':[a[j]]}, ignore_index=True)
#
# df.to_csv('fileCSV.csv',index=False)
yard = 10
sum = 20

f = open('fileCSV.csv','a')
f.write('\n{0},{1}'.format(yard,time.time()))
f.close()