x='department'
print(x[2]+x[3]+x[4]+x[5])                           #part
print(x[0:6])                                        #depart
print(x[2:6])                                        #part


y='python'
print(y[:])                                            #python
print(y[1:])                                           #ython
print(y[4:])                                           #on
print(y[5:])                                           #n


a='python'
print(a[:6])                                             #python
print(a[:3])                                             #pyt
print(a[:1])                                             #p
print(a[2:4])                                            #th
print(a[-1])                                             #n
print(a[6])                                              #indexerror:str index out of range
print(a[:-1])                                              #pytho
print(a[:-3])
print(a[:-6])                                            #blankline

a='1234'
print(a[0]+a[-1])                                           #14
print(int(a[0])+int(a[-1]))                                 #5
print(int(a[1])+int(a[-2]))                                 #5                         



v='python'
print(v[::-1])                                              #nohtyp
print(v[::-2])                                                 #nhy
print(v[::-4])                                                 #ny