word=input()
print(word)
store=dict()
print(store)
store['p']=23
store['Q']=12
store['w']=22
store[12]=11
store["hello"]=222
print(store)
allkeys=store.keys()
print(allkeys)

for ele in allkeys:
    print(ele,store[ele])
for ch in "abcdef":
    print(ch)
for val in [12,13,43,2,1,3,4,5]:
    print(val) 
