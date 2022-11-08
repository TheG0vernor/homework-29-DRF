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


# class AdCreateSerializer(serializers.ModelSerializer):
#     id = serializers.IntegerField(required=False)
#     category = serializers.SlugRelatedField(
#         queryset=Category.objects.all(),
#         slug_field='id'
#     )
#
#     class Meta:
#         model = Ad
#         fields = '__all__'
#
#     def is_valid(self, *, raise_exception=False):
#         self._category = self.initial_data.pop('category')
#         return super().is_valid(raise_exception=raise_exception)
#
#     def create(self, validated_data):
#         ad = Ad.objects.create(**validated_data)
#
#         for i in self._category:
#             category_obj, _ = Category.objects.get_or_create(
#                 name=i,
#             )
#             ad.category.add(category_obj)
#         ad.save()
#         return ad
#
#
# class AdUpdateSerializer(serializers.ModelSerializer):
#     category = serializers.SlugRelatedField(
#         required=False,
#         many=True,
#         queryset=Category.objects.all(),
#         slug_field='name'
#     )
#
#     class Meta:
#         model = Ad
#         fields = '__all__'
#
#     def is_valid(self, *, raise_exception=False):
#         self._category = self.initial_data.pop('category')
#         return super().is_valid(raise_exception=raise_exception)
#
#     def save(self):
#         ad = super().save()
#
#         for i in self._category:
#             category_obj, _ = Category.objects.get_or_create(
#                 name=i,
#             )
#             ad.category.add(category_obj)
#         ad.save()
#         return ad
#
#
# class AdDestroySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Ad
