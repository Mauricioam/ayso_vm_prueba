import platform, os

print("Sistema:", platform.system(), platform.release())
print("Distribución:", platform.freedesktop_os_release()["PRETTY_NAME"])
print("Núcleos:", os.cpu_count())



## Caja del kiosco - 1
valid_name = False
while not valid_name:
    buyer_name = input(" Ingresa tu nombre para comprar: ")
# Valido que no este vacio ni tampoco ingrese números
    if len(buyer_name) and buyer_name.isalpha():

        valid_name = True
        valid_products = False

    else:
        print("Debe ingresar un nombre válido para continuar  ")

while not valid_products:
# Valido que no este vacio ni tampoco ingrese números
            product_amount = input("Ingrese la cantidad de productos: ")

            #valido q no este vacio y sea un numero enterp
            
            if(len(product_amount) and product_amount.isdigit()):

                valid_products = True
                product_amount = int(product_amount)

            else:
                print("No ingresó productos o ingresó un valor erróneo. Ingrese cantidad de productos en números enteros.")


    # declaro valores iniciales en 0
price_w_discount = 0
total_no_discounts = 0
total_w_discount = 0

#itereación por cada producto
for item in range(1,product_amount+1):
    valid_price = False
    #validación de precio
    while not valid_price:
        product_price = input(f"Ingrese el precio del producto {item}: ")

        if(len(product_price) and product_price.isdigit()):
            valid_price = True
        else:
            print("Valor vacio o incorrecto. Ingrese números enteros")
    product_price = int(product_price)
    
    #validación del descuento
    valid_discount = False
    while not valid_discount:
        has_discount = input("Ingrese si este producto tiene descuento: S/N ")
        if(len(has_discount) and len(has_discount) < 2 and has_discount.isalpha()):
            has_discount = has_discount.lower()
            #tenemos q validar solo las dos letras s o n
            if(has_discount == "s" or has_discount == "n"):
                valid_discount = True
            else:
                print("Solo se permite s o n")
        else:
            print("Ingrese valor válido.")

    total_no_discounts += product_price
    if(has_discount == "s"):
        product_price = product_price * 0.9
    total_w_discount += product_price

    print("\n")
    print(f"Cliente: {buyer_name}")
    print(f"Cantidad de productos: {product_amount}")
    print("\n")
    print(f"Producto {item} - Precio: {product_price} Descuento (S/N): {has_discount}")
    print(f"Total sin descuento: {total_no_discounts:.2f}")
    print(f"Total con descuento: {total_w_discount:.2f}")
    print(f"Ahorro: {total_no_discounts - total_w_discount:.2f}")
    print(f"Promedio por producto: {total_w_discount/product_amount:.2f}")