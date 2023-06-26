from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from .models import Book, BookRecord, BookReview, User


class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("username", "email", "password")


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["pk", "username", "avatar"]

    def update(self, instance, validated_data):
        if "file" in self.initial_data:
            file = self.initial_data.get("file")
            instance.avatar.save(file.name, file, save=True)
            return instance
        # this call to super is to make sure that update still works for other fields
        return super().update(instance, validated_data)


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = (
            "pk",
            "title",
            "author",
            "publication_year",
            "featured",
            "favorite_count",
        )


class BookDetailSerializer(serializers.ModelSerializer):
    reviews = serializers.HyperlinkedRelatedField(
        many=True, read_only=True, view_name="book_review_detail"
    )

    class Meta:
        model = Book
        fields = (
            "pk",
            "title",
            "author",
            "publication_year",
            "featured",
            "reviews",
            "favorite_count",
        )
        validators = [
            UniqueTogetherValidator(
                queryset=Book.objects.all(), fields=["title", "author"]
            )
        ]


class BookRecordSerializer(serializers.ModelSerializer):
    book = BookSerializer(read_only=True)
    reader = serializers.SlugRelatedField(read_only=True, slug_field="username")

    class Meta:
        model = BookRecord
        fields = ("pk", "book", "reader", "reading_state")


class BookReviewSerializer(serializers.ModelSerializer):
    book = serializers.SlugRelatedField(read_only=True, slug_field="title")
    reviewed_by = serializers.SlugRelatedField(read_only=True, slug_field="username")

    class Meta:
        model = BookReview
        fields = ("pk", "body", "book", "reviewed_by")
