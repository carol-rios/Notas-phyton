import users.funcionesUsuario as funcionesUsuario
import notes.notaFunciones as notaFunciones

def iniciar():
    
    print('---BIENVENIDO/A---')
    print('Que desea hacer?  \n   Crear usuario(registro) \n   Iniciar sesion(acceder)')
    opcion=input('Escriba la opcion que desea ejecutar:   ')
    
    if opcion!='registro' and opcion!='acceder':
        print('Opcion invalida')
    else:
        if opcion == 'registro':
            registrarUser = funcionesUsuario.registrarUsuario()
            print(registrarUser)
        else:
            login = funcionesUsuario.logiando()
            if login[0] != True:
                print(login)
            else:
                idUser = login[2]
                print(f'\n Bienvenid@ {login[1]}')
                accion=''
                while accion !='salir':
                    print('\n--Menu:--')
                    print('   Crear nota (crear): \n   Mostrar notas (mostrar): \n   Eliminar nota (eliminar): \n   Salir (salir):')
                    accion = input('Elija la opcion que desea ejecuar:  ')
                    
                    if accion == 'crear':
                        registrarNote = notaFunciones.registrarNota(idUser)
                        print(registrarNote)
                    elif accion == 'mostrar':
                        notas = notaFunciones.mostrarTodas()
                        for nota in notas:
                            print(f'{nota[2]} => {nota[3]}  \n')
                    elif accion == 'eliminar':
                        notas = notaFunciones.mostrarTodas()
                        for nota in notas:
                            print(f'{nota[2]}')
                        notaEliminada = input("Elija la nota que desea eliminar:")
                        eliminar = notaFunciones.eliminarNota(notaEliminada)
                        print(eliminar)
                    elif accion == 'Salir':
                        print('')
                    else:
                        print('Accion invalida')

    

iniciar()