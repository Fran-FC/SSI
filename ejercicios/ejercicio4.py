import sys
import os
import mimetypes

def searchInPath(path, value, depth=0):
    if path[-1] != '/':
            path = path + '/'
   
        # Obtener lista de lo que hay en el directorio
    if os.access(path, os.R_OK):
        contentsDir = os.listdir(path)
        for f in contentsDir:
            # si es un archivo leer su contenido y comprobar 
            # que este contiene la cadena value
            if os.path.isfile(path+f):
                with open(path+f, 'r') as fD:
                     # Si intenta leer de un fichero que no es texto, saltará una excepción
                    try:
                        fContent = fD.read()
                        if value in fContent:
                            print(path+f) 
                    except UnicodeDecodeError:
                        pass
                    finally:
                        fD.close()
            else:
                if os.path.isdir(path+f):
                    if depth > 0:
                        searchInPath(path=path+f, value=value, depth=depth-1)
    else:
        print('No tiene permisos de lectura para el directorio {}'.format(path))
        # pass
    return


def main():
    # si solo se pasan dos argumentos, realizar busqueda solo en el 
    # directorio especificado
    if len(sys.argv) == 3:
        path = sys.argv[1]
        value = sys.argv[2]

        if not os.path.isdir(path):
            print('El directorio {} no existe'.format(path))
            return

        searchInPath(path=path, value=value)
        return

    if len(sys.argv) == 5:
        path = sys.argv[1]
        option = sys.argv[2]
        depth = sys.argv[3]
        value = sys.argv[4]

        if option != '-s' or not depth.isnumeric():
            print('Uso: python3 ejercicio4.py <path> [-s <depth>] <value>')
            return
        if int(depth) < 0:
            print('Uso: python3 ejercicio4.py <path> [-s <depth>] <value>')
            print('Depth ha de ser >= 0')
            return
        
        searchInPath(path=path, value=value, depth=int(depth))
    else:
        print('Uso: python3 ejercicio4.py <path> [-s <depth>] <value>')

if __name__ == "__main__":
    main()