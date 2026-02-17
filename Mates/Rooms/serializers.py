from .models import Room , MemberShip
from rest_framework import serializers
from Users.serializers import RoomUser


class ViewRooms(serializers.ModelSerializer):
    is_member = serializers.SerializerMethodField()
    owner = RoomUser(read_only=True)

    class Meta:
        model = Room
        fields = ('id' , 'name' , 'description' , 'category' , 'owner' , 'is_member')
    
    def get_is_member(self,obj):
        user    = self.context['request'].user
        room    = obj.id
        Mes     = MemberShip.objects.filter(user = user  , room = room).first()

        if Mes :
            if Mes.leftDate is None:
                obj = True
                return obj
            else: 
                obj = False
                return obj
        else:
            obj = False
            return obj




class CreateRoomSerializer(serializers.ModelSerializer):
    owner = RoomUser(read_only=True)
    class Meta:
        model = Room
        fields = ('name' , 'description' , 'category' , 'owner' , 'is_member')

    def create(self, validated_data):
        user = self.context['request'].user
        room = Room.objects.create(owner = user , **validated_data)
        MemberShip.objects.create(user = room.owner , room = room , role = 'owner')
        return room


class Join_MS(serializers.ModelSerializer):
    
    class Meta:
        model = MemberShip
        fields = ('user' , 'room' , 'role' , 'leftDate')
        read_only_fields = (['user' , 'room' , 'role'])

    def create(self, validated_data):
        user = self.context['request'].user
        room = self.context['room']
        MeS = MemberShip.objects.create(user = user , room = room , role = 'member' , **validated_data)
        return MeS




##############################################################################

# class MSserializer(serializers.ModelSerializer):
#     model = MemberShip
#     fields = ('user' , 'room' , 'role')

# class RoomSerializer(serializers.ModelSerializer):
#     owner = serializers.ReadOnlyField(source='owner.username')
#     is_member = serializers.SerializerMethodField()
#     role = serializers.SerializerMethodField()

#     class Meta:
#         model = Room
#         fields = ('name' , 'description' , 'created_date' , 'owner' , 'category' , 'is_member' , 'role')

#     def create(self, validated_data):
#         MSserializer.save(user = self.owner , room = self , role = 'owner')
#         return Room.objects.create(**validated_data)

#     def get_is_member(self, obj):
#         user = self.context['request'].user
#         if not user.is_authenticated:
#             return False
#         return MemberShip.objects.filter(
#             user=user,
#             room=obj,
#             leftDate__isnull=True
#         ).exists()

#     def get_role(self, obj):
#         user = self.context['request'].user
#         if not user.is_authenticated:
#             return None
#         ms = MemberShip.objects.filter(
#             user=user,
#             room=obj,
#             leftDate__isnull=True
#         ).first()
        # return ms.role if ms else None