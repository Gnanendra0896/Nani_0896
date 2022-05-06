# import requests
#
# url = 'https://reqres.in/api/users/2'
#
# response = requests.delete(url)
#
# print(response.status_code)
#
# #Validation
# assert response.status_code == 204  #true
# assert response.status_code == 200 #False


#
# for x in range(1,101):
#     count = 0
#     for i in range(2,(x//2+1)):
#         if x% i == 0:
#             count = count+1
#             break
#     if count == 0 and x!=1:
#         print(x,end=',')
ls = [1, 2, 3, 4, 6, 6]
print(ls[::-2])
g = 'my self gnanendra'
o = 'ym fles'
# s = g.split()
# s1 = reversed(s)
# l =[]
# for i in s1:
#     l.append(i[::-1])
# output = ' '.join(l)
# print(output)
print(g[::-1])

import re

s = '''cat /opt/CSCOcpm/logs/ise-psc.log | grep -c "Lab@321"
0
[root@ise-3rd-vm-9 ~]#'''
matche = re.search('[0-9]', s)
print(matche)
