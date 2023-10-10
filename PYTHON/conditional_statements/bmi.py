str="BMI CALCULATOR"
print(str)
h_cm=int(input("ENTER YOUR HEIGHT IN CM "))
h_m=h_cm/100
print(f"your height in METER is {h_m}")
w_kg=int(input("ENTER YOUR WEIGHT IN KG "))
bmi=w_kg//h_m**2
print(f"BMI is {bmi}")
if(bmi<20):
    print("YOU ARE UNDER WEIGHT")
elif(bmi<25):
    print("YOU ARE HAVING NORMAL WEIGHT")
elif(bmi<30):
    print("YOU ARE HAVING PRE OBESITY")
else:
    print("YOU ARE HAVING OBESITY")
