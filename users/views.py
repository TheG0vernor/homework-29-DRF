import json

from django.core.exceptions import ValidationError
from django.core.paginator import Paginator
from django.db.models import Count
from django.http import JsonResponse
from serializers import *
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView

from avito.settings import TOTAL_ON_PAGE
from users.models import User, Location


class UserListView(ListAPIView):
    model = User

    def get(self, request, *args, **kwargs):
        super().get(self, request, *args, **kwargs)

        self.object_list = self.object_list.annotate(ads=Count('ad'))  # подсчёт объявлений для автора
        self.object_list = self.object_list.prefetch_related('locations').order_by('username')  # сортировка авторов

        paginator = Paginator(object_list=self.object_list, per_page=TOTAL_ON_PAGE)
        page_number = request.GET.get('page', 1)
        page_object = paginator.get_page(page_number)

        users = []
        for user in page_object:
            users.append({
                "id": user.id,
                "first_name": user.first_name,
                "last_name": user.last_name,
                "username": user.username,
                "password": user.password,
                "role": user.role,
                "age": user.age,
                "locations": list(map(str, user.locations.all())),
                "total_ads": user.ads,
            })

        response = {'items': users,
                    "total": paginator.count,
                    'num_pages': paginator.num_pages
                    }

        return JsonResponse(response, json_dumps_params={'ensure_ascii': False})


class UserDetailView(RetrieveAPIView):
    model = User

    def get(self, request, *args, **kwargs):
        user = self.get_object()

        return JsonResponse({
            "id": user.id,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "username": user.username,
            "password": user.password,
            "role": user.role,
            "age": user.age,
            "locations": list(map(str, user.locations.all()))
        }, json_dumps_params={'ensure_ascii': False})


class UserCreateView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer


class UserUpdateView(UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserUpdateSerializer


class UserDeleteView(DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserDestroySerializer
