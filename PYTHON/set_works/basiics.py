st1={10,20,30,40}
st2={30,40,50,60}
st1.add(200)
print(st1) #to add something , but , we cant predict the location
union=st1.union(st2) #to combine two sets
print(union)
intersection=st1.intersection(st2) #to print common elements in two sets
print(intersection)
difference=st1.difference(st2) #to remove elements from one set which are common
print(difference)
st1.remove(20) #to remove an element from a set, but, will return an error
print(st1)
st1.discard(10) #also used to remove an element, but, wont return an error
print(st1)
st1.pop() #used to remove a random element
sd=st1.symmetric_difference(st2) #print elements which are not common in two sets
print(sd)