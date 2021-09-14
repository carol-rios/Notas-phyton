import users.modeloUsuario as modeloUsuario 

def buscar(email):
    #[(10, 'name', 'last name', 'email', 'password', datetime.date(2021, 9, 7))]
    buscando = modeloUsuario .User.buscar(email)
    return buscando


def registrarUsuario():
    print('\n --Datos de usuaio:-- ')
    nombre = input('Ingrese su nombre:   ')
    apellidos = input('Ingrese sus apellidos:   ')
    email = input('Ingrese su email:   ')
    password = input('Ingrese su contraseña:   ')

    buscando = buscar(email)
    
    if len(buscando)!=0:
        return 'Email de ususario ya existe'
    else:
        try:
            usuario = modeloUsuario .User(nombre,apellidos,email,password)
            guardar = usuario.guardar()
            return guardar
        except:
            return 'Error al registrar usuario en la bd'

def logiando():
    print('\n--Datos de usuaio:--')
    email = input('Ingrese su email:   ')
    password = input('Ingrese su contraseña:   ')
    
    buscando = buscar(email)

    if len(buscando)==0:
        return 'Este usuario no existe'
    else:
        passwordBD = buscando[0][4]
        if passwordBD!=password:
            return ['Contraseña no valida','']
        else:
            return [True,buscando[0][1],buscando[0][0]]
