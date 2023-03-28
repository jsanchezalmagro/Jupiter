import numpy as np

def mac(m1,m2,s):
    return (m1*m2)+s

def mac_std(m1, m2, s, n_word, n_frac):
    max = ((2**(n_word-1))-1)
    min = -((2**(n_word-1))-1)

    aux = int((m1*m2/2**n_frac)+s)
    if aux > max:
        aux = max
        print("Warning over")
    elif aux < min:
        aux = min
        print("Warning under")
    return aux

def to_std(real, n_word=16, n_frac=12):
    max = ((2**(n_word-1))-1)
    min = -((2**(n_word-1))-1)
    LSB = (2**(n_word-n_frac))/((2**n_word)-1)
    aux = int(real/LSB)
    if aux > max:
        aux = max
        print("Warning over")
    elif aux < min:
        aux = min
        print("Warning under")
    return aux

def to_real(integer, n_word=16, n_frac=12):
    LSB = (2**(n_word-n_frac))/((2**n_word)-1)
    return integer*LSB

m1 = to_std(0.23, n_word=18, n_frac=14)
m2 = to_std(2.23, n_word=18, n_frac=14)
s  = to_std(2.23, n_word=18, n_frac=14)

result = mac_std(m1,m2, s, n_word=18, n_frac=14)

print(to_real(result, n_word=18, n_frac=14))
print((0.23*2.23)+2.23)
