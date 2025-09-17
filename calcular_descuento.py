# Definimos la función
def calcular_descuento(monto_total, porcentaje_descuento=10):
    """
    Calcula el monto de descuento y el total a pagar.
    :param monto_total: Total de la compra
    :param porcentaje_descuento: Porcentaje de descuento (por defecto 10%)
    :return: (descuento, total_a_pagar)
    """
    descuento = monto_total * (porcentaje_descuento / 100)
    total_a_pagar = monto_total - descuento
    return descuento, total_a_pagar

# Programa principal
# 1ª llamada: usando el porcentaje por defecto (10%)
monto1 = 100  # por ejemplo $100
descuento1, total1 = calcular_descuento(monto1)
print(f"Para una compra de ${monto1}, el descuento es de ${descuento1:.2f} y el total a pagar es ${total1:.2f}")

# 2ª llamada: indicando un porcentaje diferente (por ejemplo 20%)
monto2 = 200  # por ejemplo $200
descuento2, total2 = calcular_descuento(monto2, 20)
print(f"Para una compra de ${monto2} con 20% de descuento, el descuento es de ${descuento2:.2f} y el total a pagar es ${total2:.2f}")
