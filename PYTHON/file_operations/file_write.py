fw=open("D:\\CODING\LUMINAR TECHNOLAB\\luminar_projects\\file_operations\\write.txt","w")
fw.write("WRITE in FILE OPERATIONS"+"\n")
fw.write("NUMBERS from 1800 to 2024 are")
#writing 1800-2024)
for y in range(1800,2024+1):
    fw.write(str(y)+"\n")
