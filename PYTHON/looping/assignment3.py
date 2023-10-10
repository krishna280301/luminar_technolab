# devisible by 3 = fizz
# devisible by 5 = buzz
# devisible by 15= fizzbuzz

for i in range(1,16):
    
    if(i%3==0):
        print("FIZZ")
    elif(i%5==0):
        print("BUZZ")
    elif(i%15==0):
        print("FIZZBUZZ")
    i=i+1
    