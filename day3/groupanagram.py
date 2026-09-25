def anagram(n):
   f={}
   for i in n:
       key="".join(sorted(i))
       if key not in f:
           f[key]=[]

       f[key].append(i)
   print(f)
   return list(f.values())
    
       
       

def main():
    n= ["eat", "tea", "tan", "ate", "nat", "bat"]
    result=anagram(n)
    print(result)

if __name__=="__main__":
    main()
    