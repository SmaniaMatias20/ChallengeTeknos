Documentacion
----------------------------

Informacion

- Nombre: Smania Matias Ezequiel
- Email: matiasezequielsmania@gmail.com
- DNI: 40910931

Proyecto: Challenge Teknos API Rest


Imagen
----------------------------
![](https://github.com/SmaniaMatias20/ChallengeTeknos/blob/master/images/image.png)

Descripcion del proyecto

Desarrollo de una APIs REST en Python utilizando el framework FastAPI. Este proyecto tiene como funcion gestionar mensajes en 
diferentes carpetas (archivos) y para ello cuenta con cuatro enpoints.

@app.get("/{models}")
- Obtiene las carpetas correspondientes al modelo proporcionado en la URL.

@app.get("/folders/messages/{models}")
- Obtiene mensajes filtrados según los parámetros especificados (remitente, destinatario, asunto) en la URL.

@app.post("/folders/messages/create/{models}")
- Crea un nuevo mensaje y lo guarda en la carpeta proporcionada en la URL.

@app.delete("/folders/messages/delete/{models}/{message_id}")
- Elimina un mensaje según el ID proporcionado en la URL.

No permite crear dos mensajes con el mismo ID y una vez eliminado, el mensaje se guarda en el archivo "trash".

Link al video del proyecto
----------------------------

Obtener mensajes: 

Obtener mensajes: 

Crear mensajes:

Eliminar mensajes: 
