from requests import get

def obtener_ip_publica():
    respuesta = get('https://api.ipify.org')
    if respuesta.status_code == 200:
        ip_publica = respuesta.text
        return ip_publica
    else:
        return None

ip = obtener_ip_publica()

if ip:
    print("La IP pública de tu equipo es:", ip)
else:
    print("No se pudo obtener la IP pública de tu equipo")
