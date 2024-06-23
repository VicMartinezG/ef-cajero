'''
Programar empresa automotriz(codigo, marca, modelo, año, color y precio)
que permita ingresar, consultar, listar y eliminar los autos de la empresa

'''
codigo=[]
marca=[]
modelo=[]
año=[]
color=[]
precio=[]
opcion=0
posicion=0
while opcion!=5:
    print ('Concesionaria Automotriz')
    print('**********')
    print('1.Ingresar: ')
    print('2.Consultar: ')
    print('3.Listar: ')
    print('4.Actualizar: ')
    print('5.Salir')
    opcion=int(input('Ingrese opcion: '))
    if opcion==1:
        print('Ingresar articulos: ')
        print('********************************')
        codigo.append(input('Ingrese codigo: '))
        marca.append(input('Ingrese marca: '))
        modelo.append(input('Ingrese modelo: '))
        año.append(input('Ingrese año: '))
        color.append(input('Ingrese color: '))
        precio.append(input('Ingrese precio: '))
    elif opcion==2:
        print('Buscar articulos: ')
        print('********************************')
        consultar=input('Ingrese codigo: ')
        for pos in range(len(codigo)):
            if consultar==codigo[pos]:
                print('MARCA  MODELO  AÑO  COLOR  PRECIO')
                print(marca[pos]+'  '+modelo[pos]+'  '+año[pos]+'  '+color[pos]+'  '+precio[pos])
    elif opcion==3:
        print('Listar articulos: ')
        print('********************************')
        for pos in range(len(codigo)):
            print('MARCA  MODELO  AÑO  COLOR  PRECIO')
            print(marca[pos]+'  '+modelo[pos]+'  '+año[pos]+'  '+color[pos]+'  '+precio[pos])
    elif opcion==4:
        print('Actualizar articulos: ')
        print('********************************')
        consultar=input('Ingrese codigo: ')
        for pos in range(len(codigo)):
            if consultar==codigo[pos]:
                marca[pos]=input('Ingrese marca: ')
                modelo[pos]=input('Ingrese modelo: ')
                año[pos]=input('Ingrese año: ')
                color[pos]=input('Ingrese color: ')
                precio[pos]=input('Ingrese precio:')
            print('Elemento actualizado...')
print('*************************************************')
print('*************************************************')
print('Saliendo del sistema')
print('Saliendo del sistema...')