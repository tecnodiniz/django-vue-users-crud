from rest_framework import serializers
from .models import CustomUser, Address

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'
        
class UserSerializer(serializers.ModelSerializer):
    addresses = AddressSerializer(many=True)  # Remova read_only=True

    class Meta:
        model = CustomUser
        fields = '__all__'

    def create(self, validated_data):
        addresses_data = validated_data.pop('addresses', [])
        user = CustomUser.objects.create(**validated_data)
        for address_data in addresses_data:
            Address.objects.create(user=user, **address_data)
        return user

    def update(self, instance, validated_data):
        addresses_data = validated_data.pop('addresses', [])
        
        # Atualiza os campos do usuário
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        # Atualiza os endereços associados
        for address_data in addresses_data:
            Address.objects.update_or_create(
                user=instance, id=address_data.get('id'), defaults=address_data
            )

        return instance
