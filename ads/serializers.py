from rest_framework import serializers

from ads.models import Ad


class AdListSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field='first_name'
    )

    class Meta:
        model = Ad
        fields = ['id', 'name', 'author', 'price']


class AdRetrieveSerializer(serializers.ModelSerializer):
    author_id = serializers.PrimaryKeyRelatedField(
        read_only=True
    )
    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field='first_name'
    )
    category_id = serializers.PrimaryKeyRelatedField(
        read_only=True
    )

    class Meta:
        model = Ad
        exclude = ['category', 'image']


class AdCreateSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)

    class Meta:
        model = Ad
        fields = '__all__'


class AdUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        fields = '__all__'


class AdDestroySerializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
