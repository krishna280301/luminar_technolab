# 1**3
# 2**3
# 3**3
# cube sum of digit
# 1-extraction
# 2-find cube
# 3-sum
# 4-flooring

num=371
original=num
sum=1
while(num!=0):
    digit=num%10
    cube=digit**3
    sum=sum+cube
    num=num//10
print(sum)
print("armstrong" if num==original else "not armstrong")