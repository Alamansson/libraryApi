from rest_framework import serializers


class FavouriteSerializer(serializers.Serializer):
    book_id = serializers.IntegerField(min_value=1)


