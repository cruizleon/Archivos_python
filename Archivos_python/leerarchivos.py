# Este progrma permite leer un archivo de texto en python
archivo = open ('Archivo1.txt','r')
mensaje = archivo.read()
print(mensaje)
archivo.close()