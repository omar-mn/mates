from rest_framework import serializers
from .models import Message 
from Users.serializers import RoomUser


class MessageSerializer(serializers.ModelSerializer):
    user = RoomUser(read_only=True)
    class Meta:
        model   = Message
        fields  = ('id' , 'content','sent_at' , 'user')
        read_only_fields = ('user', 'room')
    
    def create(self, validated_data):
        user = self.context['request'].user
        room = self.context['Room']
        message = Message.objects.create(user = user , room = room , **validated_data)
        return message
    
class ModMessageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Message
        fields  = ('id' , 'content','sent_at' , 'user')
        read_only_fields = (['user'])
