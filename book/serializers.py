from urllib import request

from rest_framework import serializers


from .models import Book, BookReviewRating


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


class BookReviewRatingSerializer(serializers.ModelSerializer):
        # news_title = serializers.SerializerMethodField("get_news_title")

    class Meta:
        model = BookReviewRating
        fields = '__all__'

    def validate_user(self, user):
        if self.Meta.model.objects.filter(user=user).exists():
            raise serializers.ValidationError(
                "Вы уже оставляли отзыв на этот продукт"
            )
        return user



    def validate_rating(self, rating):

        if rating not in range(1, 101):
            raise serializers.ValidationError(
                "Рейтинг должен быть от 1 до 5"
            )
        return rating

    def create(self, validated_data):
        user = self.context.get('request').user
        validated_data['user'] = user
        instance_id = self.context.get('request').data.get('book')
        new_rating = self.context.get('request').data.get('rating')
        try:
            instance = BookReviewRating.objects.get(book_id=instance_id)
            rating = (instance.rating + int(new_rating)) / 2


        except:
            rating = int(new_rating)

        print('review: ', instance.review, '\nrating: ', instance.rating, '\nuser_id: ', instance.user_id,
              '\nbook_id: ', instance.book_id, '\nid', instance.id)

        validated_data['rating'] = rating
        review = BookReviewRating.objects.create(**validated_data)
        return review









