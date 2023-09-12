from fastapi import FastAPI

app = FastAPI() #variable para usar FastApi

#Creamos una función

@app.get("/") #Podemos hacer una llamada a algún lugar
async def root(): #Cuando llamamos a un servidor, la llamada es asíncrona, para que el programa pueda realizar otras cosas mientras espera la respuesta
    return "¡Hola FasApi!"

@app.get("/url")#cambiamos la ruta
async def root(): #no debemos repetir el nombre de la función, esto es solo un ejemplo
    return {"url_curso":"https://mariacedev.com"}