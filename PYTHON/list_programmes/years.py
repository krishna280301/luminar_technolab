#1800-2024
years=[y for y in range(1800,2025)]
print(years)
#century years
c_year=[y for y in range(1800,2030) if(y%100==0)]
print(f"century years are {c_year}")
#non century years
nc_year=[y for y in range(1800,3000) if(y%100!=0)]
print(f"non century years are {nc_year}")