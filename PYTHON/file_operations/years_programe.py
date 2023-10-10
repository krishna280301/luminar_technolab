f=open("D:\\CODING\LUMINAR TECHNOLAB\\luminar_projects\\file_operations\\years.txt","w")
for y in range(1800,2025):
    f.write(str(y)+"\n")
f.close()
f_read=open("D:\\CODING\LUMINAR TECHNOLAB\\luminar_projects\\file_operations\\years.txt","r")
ly_write=open("D:\\CODING\LUMINAR TECHNOLAB\\luminar_projects\\file_operations\\leap_years.txt","w")
ly_write.write("LEAP YEARS ARE"+"\n")
for year in f_read:
    year=int(year)
    if(year%100==0) and (year%4==0):
        ly_write.write(str(year)+"\n")
    elif(year%100!=0) and (year%4==0):
        ly_write.write(str(year)+"\n")
ly_write.close()
f_read=open("D:\\CODING\LUMINAR TECHNOLAB\\luminar_projects\\file_operations\\years.txt","r")
ny_write=open("D:\\CODING\LUMINAR TECHNOLAB\\luminar_projects\\file_operations\\noemal_years.txt","w")
ny_write.write("NORMAL YEARS ARE")
for year in f_read:
    year=int(year)
    if(year%4!=0):
        ny_write.write(str(year)+"\n")


