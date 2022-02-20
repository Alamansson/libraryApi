from rest_framework import serializers


class LikeSerializer(serializers.Serializer):
    book_id = serializers.IntegerField(min_value=1)





