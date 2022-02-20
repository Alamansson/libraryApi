from rest_framework import serializers


from .models import Book


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









