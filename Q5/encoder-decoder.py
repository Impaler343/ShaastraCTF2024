
def readf(filename):
    f = open(filename,'r')
    x = f.read()
    f.close()
    return x

def writef(filename,st):
    f = open(filename,'w')
    f.write(st)
    f.close()



def flip(n):
    b = str(bin(n))[2:]
    b = '0'*(7-len(b)) + b
    res = ''
    for i in b:
        if(i == '0'):
            res += '1'
        else:
            res += '0'
    #print(n,b,res)
    return int('0b'+res,2)

#encoder
original_code = readf("Q5/decoded.txt")
res = ""
for i in original_code:
    res += str(flip(ord(i))) + ' '
res = res[:-1]
print(res)
writef('Q5/file.txt',res)

#decoder
encoded_code = readf('Q5/file.txt')
x = encoded_code.split(' ')
sol = ""
for i in x:
    sol += chr(flip(int(i)))
print(sol)