
import json

from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer

from .models import Conversacion, Mensaje


class ChatConsumer(WebsocketConsumer):

    def connect(self):
        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        self.room_group_name = f"chat_{self.room_name}"

        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name, self.channel_name
        )

        self.accept()

    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name, self.channel_name
        )

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]

        usuario = self.scope["user"]

        # Guardar mensaje
        self.guardar_mensaje(usuario.id, message)

        # Enviar mensaje al grupo
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                "type": "chat.message",
                "message": message
            }
        )

    def chat_message(self, event):
        message = event["message"]

        self.send(text_data=json.dumps({
            "message": message
        }))

    def guardar_mensaje(self, usuario_id, contenido):

        id1, id2 = map(int, self.room_name.split("_"))

        conversacion, creada = Conversacion.objects.get_or_create(
            usuario1_id=id1,
            usuario2_id=id2
        )

        Mensaje.objects.create(
            conversacion=conversacion,
            emisor_id=usuario_id,
            contenido=contenido
        )
