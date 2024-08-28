peliculas={"pol":{"nombre":"rey leon","estreno":2000,"protagonista":"simba","genero":"animada"},"rey":{"nombre":"cars","estreno":2019,"protagonista":"rayo mcGueen","genero":"diversion"}}
print(peliculas)
print("_________________________________")
for c,v in peliculas.itens():#uso el for para mostrarlo prolijo
    print(c, ":",v ) 
    print("______________________________")#imprimo esto para separalos