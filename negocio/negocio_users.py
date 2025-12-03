import requests
from prettytable import PrettyTable


def obtener_usuarios_api(url):
    tabla_usuarios = PrettyTable()
    tabla_usuarios.field_names=['N°','Nombre','Nombre Usuario','Correo','Latitud']
    respuesta = requests.get(url)
    if respuesta.status_code == 200:
        listado_usuarios = respuesta.json()
        for usuario in listado_usuarios:
            tabla_usuarios.add_row([
                usuario['id'],
                usuario['name'],
                usuario['username'],
                usuario['email'],
                usuario['address']['geo']['lat']])
    print(tabla_usuarios)