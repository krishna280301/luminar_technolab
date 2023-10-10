line=[1,2,4,5,6,3,7,8]
#printing sqaures easity
square=[i**2 for i in line]
print(square)
#printing cubes easily
cube=[n*n*n for n in line]
print(cube)
#printing even numbers
even=[i for i in line if(i%2==0)]
print(even)
#printing numbers greater than 5
more=[i for i in line if(i>5)]
print(more)