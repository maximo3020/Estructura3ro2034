zapatillas={"co1":{"modelo":"nike","material":["cuero sintetico,gamuza,malla"],"numero":40,"cantidad stock":1},
"coo2":{"modelo":"vans","material":["gamuza,lona,suela waffle de caucho"],"numero":30,"cantidad stock":1},
"cooo3":{"modelo":"puma","material":["imeva, goma"],"numero":28,"cantidad stock":1}}
while True:
 opcion=input("ingrese una de las siguientes opciones\n1 mostrar zapatillas en stok\n2 agregar zapatillas al stok\n3 salir\n")
 if opcion=="1":
    print("___________________________")
    print("---------zapatillas---------")
    print("____________________________")
    for c,v in zapatillas.items():
     print(c,":",v)
     print("________________________________")
 elif opcion=="2":
   zapatillasAgregar=input("escribe el codigo de zapatillas a agregar al stock:")
   modelo=input("escriba el modelo de zapatillas a agregar:")
   material=input("escribe el material de zapatillas a agrega:")
   numero=input("escribe el numero de zapatillas a agrega:")
   cantidaddstock=input("escribe la cantidad en stock  de zapatillas a agrega:")
   zapatillas[zapatillasAgregar]=modelo,material,numero,cantidaddstock
 elif opcion==3:
   break
