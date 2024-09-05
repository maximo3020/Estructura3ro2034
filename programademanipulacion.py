zapatillas={"co1":{"modelo":"nike","material":["cuero sintetico,gamuza,malla"],"numero":40,"cantidad stock":1},
"coo2":{"modelo":"vans","material":["gamuza,lona,suela waffle de caucho"],"numero":30,"cantidad stock":1},
"cooo3":{"modelo":"puma","material":["imeva, goma"],"numero":28,"cantidad stock":1}}
while True:
 if opcion=="1":
    print("___________________________")
    print("---------zapatillas---------")
    print("____________________________")
    for c,v in zapatillas.items():
     print(c,":",v)
     print("________________________________")