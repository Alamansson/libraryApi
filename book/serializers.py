from rest_framework import serializers
from .models import Book, BookLike, BookFavourite


class BookSerializer(serializers.ModelSerializer):

    publisher = serializers.ReadOnlyField(source='author.email')

    class Meta:
        model = Book
        fields = '__all__'

    def create(self, validated_data):
        request = self.context.get('request')
        book = Book.objects.create(
            publisher=request.user, **validated_data
        )
        return book


class BookLikeSerializer(serializers.ModelSerializer):

    class Meta:
        model = BookLike
        fields = "__all__"

    def create(self, validated_data):
        print('Works create')
        user = self.context.get('request').user
        print('User: ', user)
        validated_data['user'] = user
        print('validated_data', validated_data)
        like = BookLike.objects.create(**validated_data)
        return like


class BookFavouriteSerializer(serializers.ModelSerializer):

    class Meta:
        model = BookFavourite
        fields = "__all__"

    def create(self, validated_data):
        print('Works create')
        user = self.context.get('request').user
        print('User: ', user)
        validated_data['user'] = user
        print('validated_data', validated_data)
        favourite = BookFavourite.objects.create(**validated_data)
        return favourite






