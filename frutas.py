frutas={"manzana":{"precio":1500},"banana":{"precio":1000}}
total=0
totaldecompra=0
while True:
  fruta=input("ingrese la fruta que desea vender:")
  cantidad=float(input("ingrese la cantidad a vender:"))

  if fruta in frutas:
    total=frutas[fruta]["precio"] =cantidad
    totaldecompra=totaldecompra+total
    print(f"el total a pagar por{cantidad}kilos de {frutas} es: {total}")
    print("el precio de",cantidad,"kilos","de",frutas,"es de:",total)
  else:
     print("la fruta ingresada no existe en la lista")
  respuestas=input("desea vender otro producto?si/no:") 
  if respuestas=="no":
     break
  print("total de la compra es de:",totaldecompra)