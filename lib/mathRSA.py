import random

from sympy import mod_inverse


def digits(number):
    dig = 0
    while number > 0:
        dig += 1
        number //= 10
    return dig

def modbinexp(a, b, C):
    a = a % C
    if b == 0:
        return 1
    res = modbinexp(a, b // 2, C)
    res = (res * res) % C
    if b % 2 == 1:
        res = (res * a) % C
    return res

def generatekeys():
    f = open("../primes.primes.txt","r")
    largeprimes = f.readlines()
    f.close()

    p,q,N = 0,0,0
    while(q==p):
        p,q = int(random.choice(largeprimes)[:-1]),int(random.choice(largeprimes)[:-1])

    N = p*q
    Mod = (p-1)*(q-1)

    e = Mod

    while e%Mod == 0:
        e = random.randomint(2,Mod-1)

    publickey = (N,e)
    privatekey = (N,mod_inverse(e,Mod))

    return (privatekey,publickey)

# apply RSA algorithm
def RSA(value, key):
    mod = key[0]
    exp = key[1]

    encryptrdmessage = modbinexp(value,exp,mod)

    return encryptrdmessage


