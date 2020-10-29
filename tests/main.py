from pylovepdf.ilovepdf import ILovePdf
import os

# Crea el directorio si este no existe
def createPath():
    userName = os.path.expanduser('~')
    pathName = '\Documents\MagicPdf'
    totalPath = userName + pathName

    print(totalPath)

    if not os.path.exists(totalPath):
        os.mkdir(totalPath)
    return totalPath

# Lista los archivos en un directorio
def listDir(dir):
    file = os.listdir(dir)
    return file

# Funcion principal
def pdfMainfunction(outPath, file, option): #recibe el directorio de salida, el archivo y la opcion

    # print(file, option)
    
    ilovepdf = ILovePdf(
        "project_public_1ed8cbf7ceb806075f868bc7ff18aeb3_VMWJR9477e2776bb332c4b14fc072c70919a7",
        verify_ssl=True,
    )
    
    task = ilovepdf.new_task(option)
    task.add_file(file)
    task.set_output_folder(outPath)
    task.execute()
    task.download()
    task.delete_current_task()
    
# Ejecucion del programa
os.system('cls') # Solo para windows

try:
    fpath = createPath()
    print("\n>>Directorio Creado Correctamente! \n\nSu directorio es: " + fpath + "\n")
    
except:
    print("Ah ocurrido un error al crear el escritorio")
    
a = input("Coloque un archivo pdf en su directorio y presione enter para continuar...")

fFiles = ''.join(listDir(fpath)) # se listan los archivos y se convierten en un string
stringPath = fpath + "\\" + fFiles # se junta el directorio del usuario y nombres de archivos para utilizar en la funcion principal
option = "compress" # opcion que recibe la libreria

pdfMainfunction(fpath, stringPath, option)

print("Tarea completada con exito!!!")
x = input("\nPreciona Enter para salir...")
exit()