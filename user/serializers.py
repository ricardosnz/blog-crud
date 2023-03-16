import re
from django.contrib.auth import get_user_model
from rest_framework import serializers
UserModel = get_user_model()

class UserAccountSerializer(serializers.ModelSerializer):
    class Meta: 
        model=UserModel
        fields = ('id', 'username', 'name', 'last_name', 'email', 'phone', 'password', 'created')
        read_only_fields = ('id', 'created')

    def create(self, validated_data):
        user = super().create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

    def validate_phone(self, value):
        phone = re.match('(\+\d{2}[\s-]?)?\d{6,10}', value)
        if not phone: raise serializers.ValidationError('Phone invalid')
        return phone[0]

