'''
Programar cajero bancario(codigo // cta de ahorros) que permita via menu
Ingresar codigo y las siguientes operaciones(depositar, retirar,consultar saldo)

'''
codigo=[]
cuentaahorros=[]
opcion=0
while opcion!=4:
    print ('Banco Centroamerica')
    print('**********')
    print('1.Despositar: ')
    print('2.Retirar: ')
    print('3.Consultar saldo: ')
    print('4.Salir')
    opcion=int(input('Ingrese opcion: '))
    if opcion==1:
        print('Ingresar monto: ')
        print('********************************')
        monto=int(input())
        codigo.append(input('Ingrese codigo de cliente: '))
        cuentaahorros.append(input('Ingrese numero de cuenta: '))
    elif opcion==2:
        print('Ingrese monto a retirar: ')
        print('********************************')
        consultar=input('Ingrese monto: ')
        for pos in range(len(codigo)):
            if consultar==codigo[pos]:
                print('Numero de cuenta de ahorros')
                print(cuentaahorros[pos])
    elif opcion==3:
        print('Consultar saldo: ')
        print('********************************')
        for pos in range(len(codigo)):
            print('Numero de cuenta de ahorros')
            print(cuentaahorros[pos])
    
print('*************************************************')
print('*************************************************')