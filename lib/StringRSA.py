from mathRSA import *


def valueError(str):
    print(str)
    return 0


# convert letter to custom ASCII
def myASCII(letter):
    if letter in ['á', 'à', 'é', 'ó', 'ç']:
        return 95 + ['á', 'à', 'é', 'ó', 'ç'].index(letter)
    return ord(letter) - 32


# convert custom ASCII to letter
def myChar(myascii):
    extra = ['á', 'à', 'é', 'ó', 'ç']
    if myascii >= 100:
        raise (valueError('myChar: invalid ascii number'))

    if myascii > 94:
        return extra[myascii - 95]
    else:
        return chr(myascii + 32)


# convert string to custom ASCII integer
def getInt(strMsg):
    res = 0
    invalid = []
    for letter in strMsg:
        ascii = ord(letter)
        if (ascii < 32 or ascii > 126) and not letter in ['á', 'à', 'é', 'ó', 'ç']:
            if letter not in invalid:
                invalid += [letter]
            letter = '?'
        res = res * 100 + myASCII(letter)

    if (len(invalid) > 0):
        print('Invalid characters replaced by \'?\'')
        for c in invalid:
            print(c, end=' ')
        print()

    return res


# convert custom ASCII integer to string
def getStr(intMsg):
    res = ''
    while intMsg > 0:
        letterInt = intMsg % 100
        intMsg //= 100
        res = myChar(letterInt) + res
    return res


# split integer in blocks (custom blocksize)
def splitMessage(intMsg, blkSz):
    cutter = 1
    while blkSz > 0:
        cutter *= 10
        blkSz -= 1

    res = []
    while intMsg > 0:
        new = intMsg % cutter
        intMsg //= cutter
        res = [new] + res

    return res


# merge blocks into integer (custom blocksize)
def mergeBlocks(blocks, blkSz):
    glue = 1
    while blkSz > 0:
        glue *= 10
        blkSz -= 1

    merged = 0
    for block in blocks:
        merged = merged * glue + block
    return merged

# encrypt/decrypt message (according to flag)
def transform(message, key, isEncrypt):
    sz1 = sz2 = digits(key[0])
    if isEncrypt:
        sz1 -= 1
    else:
        sz2 -= 1

    intMsg = getInt(message)

    blocks = splitMessage(intMsg, sz1)

    newBlocks = []
    for block in blocks:
        newBlocks += [RSA(block, key)]

    intCoded = mergeBlocks(newBlocks, sz2)

    codedMsg = getStr(intCoded)
    return codedMsg

