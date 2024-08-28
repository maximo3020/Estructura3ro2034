recetas={"milanesa":{"carne":"200gm","pan rallado":"300gm","huevos":"3"},"empanada de carne":{"tapa de epanada":"10","carne molida":"300gm","cebolla":"3"}}
BuscarValorRecetas=input("ingrese recetas a busar :")
x= recetas[BuscarValorRecetas]
print("su recetas es:",x)
print("____________________________")


for c,v in recetas.items():
    print(c, ":",v)
    print("________________________________________")  