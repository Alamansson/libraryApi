from rest_framework import serializers


class ReviewSerializer(serializers.Serializer):
    book_id = serializers.IntegerField(min_value=1)







