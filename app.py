import os

from flask import (Flask, redirect, render_template, request,
                   send_from_directory, url_for)
from heyoo import WhatsApp

app = Flask(__name__)


@app.route('/')
def index():
   print('Request for index page received')
   return render_template('index.html')

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route('/hello', methods=['POST'])
def hello():
   name = request.form.get('name')

   if name:
       print('Request for hello page received with name=%s' % name)
       return render_template('hello.html', name = name)
   else:
       print('Request for hello page received with no name or blank name -- redirecting')
       return redirect(url_for('index'))




@app.route("/enviar/", methods=["POST", "GET"])
def enviar():
    #TOKEN DE ACCESO DE FACEBOOK
    token='EAAN4B7AYCJkBOZC29AOF0kkF6POyznnqZAw2bjaMeSQrfsqyEeG6aY5J7mDZA5LfM6BvZB0D36hFpwHtLeUQabpUOLlRRzcZBYT9LHf4rAPTvciEN5kFLWyapbqmBgLaHPNLmDZAh3e9LftrXnZB6IbBVeAebPtwLSaXPtN4IAayYKwChXI8XAfj9Rfr8KMSZBfuEaMBGRQl2GIidjN7NxGRW0UuuRXFYvr02hoZD'
    #IDENTIFICADOR DE NÚMERO DE TELÉFONO
    idNumeroTeléfono='663003266888103'
    #TELEFONO QUE RECIBE (EL DE NOSOTROS QUE DIMOS DE ALTA)
    telefonoEnvia='573118467617'
    #MENSAJE A ENVIAR
    textoMensaje="Hola novato saludos"
    #URL DE LA IMAGEN A ENVIAR
    urlImagen='https://i.imgur.com/r5lhxgn.png'
    #INICIALIZAMOS ENVIO DE MENSAJES
    mensajeWa=WhatsApp(token,idNumeroTeléfono)
    #ENVIAMOS UN MENSAJE DE TEXTO
    mensajeWa.send_message(textoMensaje,telefonoEnvia)
    #ENVIAMOS UNA IMAGEN
    mensajeWa.send_image(image=urlImagen,recipient_id=telefonoEnvia,)
    return "mensaje enviado exitosamente"




if __name__ == '__main__':
   app.run()
