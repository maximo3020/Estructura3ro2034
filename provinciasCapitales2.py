provincias={"cordoba":"cordoba","buenos aires":"la plata"}
pciaBuscarValorCapital=input("ingrese provincias a busar capital:")
x= provincias[pciaBuscarValorCapital]
print("su capital es:",x)
print("____________________________")
for p, c in provincias.items():
    print(p, ":",c)
    print("______________________")
