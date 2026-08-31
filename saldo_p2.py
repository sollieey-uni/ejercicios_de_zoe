saldo = 700

def retirar (monto):
    global saldo
    saldo = saldo - monto

retirar(400)
print ("el saldo es" , saldo)

 #prefiero el uso de global pq se me hace mas sencillo que utilizar return.
