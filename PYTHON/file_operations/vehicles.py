f=open("D:\\CODING\LUMINAR TECHNOLAB\\luminar_projects\\file_operations\\numbers.txt","r")
all_numbers=[line.rstrip("\n") for line in f]
print(f"ALL NUMBERS ARE {all_numbers}")
kerala_number=[ knum for knum in all_numbers if(knum.startswith("kl"))]
print(f"KERALA NUMBERS ARE {kerala_number}")