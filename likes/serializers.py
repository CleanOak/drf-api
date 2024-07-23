from django.db import IntegrityError
from rest_framework import serializers
from .models import Like


class LikeSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')


    class Meta:
        model = Like
        filed = ['id', 'owner', 'posts', 'created_at']


    def create(self, validated_data):
        try:
            return super().create(validated_data)
        except IndexError:
            raise serializers.ValidationError({
                'detail': 'possible duplicate'
            })
