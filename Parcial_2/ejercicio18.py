productos = {
    "nuez":300,
    "jabon":20,
    "platano":30,
    "avena":30,
    "leche":32
}

#for producto in productos:
for producto, valor in productos.items():
    print("Articulo: ",producto)
    print("Precio: $",valor)
  

