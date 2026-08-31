MONEDA = "C$"
IVA = 0.15


def agregar_producto(inventario, nombre, precio, cantidad):
    producto = {
        "nombre": nombre,
        "precio": precio,
        "cantidad": cantidad
    }
    
    inventario.append(producto)


def calcular_valor_total(inventario):
    resultado = 0
    
    for producto in inventario:
        resultado = resultado + (producto["precio"] * producto["cantidad"])
    
    return resultado


def mostrar_inventario(inventario):
    print("INVENTARIO")
    
    for producto in inventario:
        print(
            producto["nombre"],
            "- Precio:", MONEDA, producto["precio"],
            "- Cantidad:", producto["cantidad"]
        )


inventario = []

agregar_producto(inventario, "Camisa", 500, 2)
agregar_producto(inventario, "Pantalón", 800, 1)
agregar_producto(inventario, "Zapatos", 1200, 1)

mostrar_inventario(inventario)

subtotal = calcular_valor_total(inventario)
impuesto = subtotal * IVA
total = subtotal + impuesto

print("Subtotal:", MONEDA, subtotal)
print("IVA:", MONEDA, impuesto)
print("Total:", MONEDA, total)
