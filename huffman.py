class tree(object):
   
    def __init__(self,left,right,data):
        self.left = left
        self.right = right
        self.data = data

def sort(o):
    l = []
    for i in o:
       l.append(tree(None,None,i))
    while len(l)!=1:
         f = l.pop()
         s = l.pop()
         h = (f.data[0]+s.data[0],f.data[1]+s.data[1])
         l.append(tree(f,s,h))
         l = sorted(l,reverse =True,key = lambda y:y.data[-1])
    z = l.pop()
    return z
         
def encode(z,i):
        dig = []
        while i!=z.data[0]: 
             if i in z.left.data[0]:
                  dig.append('0')
                  z=z.left
             elif i in z.right.data[0]:
                  dig.append('1')
                  z=z.right  
        hai = ''.join(dig)
        return hai

def decode(r,z):
     new = z
     word = ''
     for i in r:
         if i == "1":
              z = z.right
         elif i == "0":
              z = z.left
         if z.left == None or z.right == None:
              word = word + z.data[0] 
              z = new
     return word

def main():
    d = {}
    o = []
    res = ''
    q = ''
    s = raw_input("Enter the string to encode")
    for c in s:
        if c not in d:
            d[c] = 0
        d[c]+= 1
    o = sorted(d.items(),reverse = True, key = lambda x:x[1])
    z = sort(o)
    for i in s:
        d = encode(z,i)
        str(d)
        res=res+d    
    print"Here is the encoded string",res
    r = raw_input("Enter the digit to decode") 
    q = decode(r,z)
    print "Here is the decoded digit",q

if __name__ == "__main__":
  main()

