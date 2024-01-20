Documentacion
----------------------------

Informacion

- Nombre: Smania Matias Ezequiel
- Email: matiasezequielsmania@gmail.com
- DNI: 40910931

Proyecto: Challenge Teknos APIs REST


Imagen
----------------------------
![](https://github.com/SmaniaMatias20/ChallengeTeknos/blob/master/images/image.png)

Descripcion del proyecto

Desarrollo de una APIs REST en Python utilizando el framework FastAPI. Este proyecto tiene como funcion gestionar mensajes en diferentes carpetas (archivos) y para ello cuenta con cuatro endpoints.

@app.get("/{models}")
- Obtiene las carpetas correspondientes al modelo proporcionado en la URL.

@app.get("/folders/messages/{models}")
- Obtiene mensajes filtrados según los parámetros especificados (remitente, destinatario, asunto) en la URL.

@app.post("/folders/messages/create/{models}")
- Crea un nuevo mensaje y lo guarda en la carpeta proporcionada en la URL.

@app.delete("/folders/messages/delete/{models}/{message_id}")
- Elimina un mensaje según el ID proporcionado en la URL.

No permite crear dos mensajes con el mismo ID y una vez eliminado, el mensaje se guarda en el archivo "trash".

Comando para correr el servidor: uvicorn main:app --reload

Link al video del proyecto
----------------------------

- Link: https://youtu.be/bGzSAQ65Kvk?si=dfzrY4JMQDe7lz-f 
