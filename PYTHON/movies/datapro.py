from json import load
path="D:\CODING\\LUMINAR TECHNOLAB\\luminar_projects\\movies\\mdb.json"
with open(path,encoding="utf-8") as f:
    films=load(f)                                        
#print total number of films
print(f"TOTAL NUMBER OF FILMS - {len(films)}")

# #print all movie names released in 2015
movie2015=[i.get("title") for i in films if(i.get("year")=="2015")]
print(f"MOVIES RELEASED IN 2015 ARE {movie2015}")

#print comedy genre movies
comedy_movies=[i.get("title") for i in films if("Comedy" in i.get("genres"))]
print("COMEDY MOVIES ARE")
print(comedy_movies)

# #id in range(20,30) and runtime >110
movies_filter=[i.get("title") for i in films if(i.get("id") in range(20,30+1)) and i.get("runtime")>"100"]
print("MOVIES IN RANGE 20 - 30 WITH RUNTIME GREATER THAN 110 ARE")
print(movies_filter)

#print movies with one word title
title=[i.get("title") for i in films if(len(i.get("title").split(" "))==1)]
print("MOVIES WITH ONE WORD TITLES ARE")
print(title)

#highest runtime movie with genre drama
highest=[i for i in films if("Drama" in i.get("genres"))]
maximum=max(highest,key=lambda f:int(f.get("runtime")))
print(f"DRAMA MOVIE WITH HIGHEST RUNTIME IS {maximum}")

#print all genres 
#year in which most of the movies has released
most_movies={}
for i in films:
    year=i.get("year")
    if(year in most_movies):
        most_movies[year]+=1
    else:
        most_movies[year]=1
# m_movies=max(most_movies,key=lambda m:most_movies.get(m))
# print(m_movies)

print(max((v,k) for k,v in most_movies.items()))

all_genres=[i.get("genres") for i in films]
print(all_genres)