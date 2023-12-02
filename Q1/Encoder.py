s = 'cvpbPGSarkg_gvzr_Vyy_gel_2_ebhaqf_bs_ebg13_jdJBFOXJ'
z = 'shaastraCTF'
c1 = 'abcdefghijklmnopqrstuvwxyz'
c2 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def n(a):
    if(a in c1):
        return ord(a)-96
    elif(a in c2):
        return ord(a)-64
def rot(a,n):

    if(a in c1):
        return c1[(c1.index(a)+n)%26]
    if(a in c2):
        return c2[(c2.index(a)+n)%26] 


def simple_encode(s):
    x = s[0]
    for i in range(len(s)-1):
        x += rot(s[i],n(s[i+1]))
    x += s[-1]
    return x
f = simple_encode(z)
print(f)
# What they are supposed to print out to see the pattern
for i in range(len(f)):
    try:
        print(n(z[i]),ord(f[i])-ord(z[i]))
    except:
        print(" ",ord(f[i])-64)
