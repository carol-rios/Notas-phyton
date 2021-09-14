import notes.notaModelo as notaModelo

def buscar(titulo):
    buscando = notaModelo.Note.buscar(titulo)
    return buscando



def registrarNota(idUser):
    print('\n --Datos de la nota:--')
    titulo = input('Titulo:  ')
    descripcion = input('Descripcion:  ')

    buscando = buscar(titulo)
    if len(buscando)!=0:
        return 'Error,ya existe una nota con ese titulo'
    else:
        try:
            nota = notaModelo.Note(idUser,titulo,descripcion)
            guardar = nota.guardar()
            return guardar
        except:
           return 'Error al registrar nota en la bd' 


def mostrarTodas():
    print('\n--Notas registradas:--')
    buscando = notaModelo.Note.buscarTodo()
    return buscando

def eliminarNota(titulo):
    buscando = buscar(titulo)
    if len(buscando)==0:
        print("Error,la nota ingresada no existe" )
    else:
        try:
            eliminar = notaModelo.Note.eliminarNota(titulo)
            return eliminar
        except:
            return 'Error al eliminar la nota en la bd'
