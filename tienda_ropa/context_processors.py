from datetime import datetime

def fecha_context(request):
    fecha = datetime.now()
    return {"fecha": fecha}

def info_context(request):
    telefono = 3584664299
    mail =  "tienda@tienda.com"
    direccion = "Tejerina 783"
    return {
        "telefono": telefono,
        "email" : mail,
        "direccion" : direccion,
    }