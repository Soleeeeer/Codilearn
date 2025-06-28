from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_decode
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets, permissions
from django.contrib.auth import get_user_model
from .serializers import UserSerializer
from .permissions import IsAdminOrSelf

User = get_user_model()

class ActivateAccountView(APIView):
    def get(self, request, uid, token):
        try:
            user_id = urlsafe_base64_decode(uid).decode()
            user = get_object_or_404(User, id=user_id)
            if default_token_generator.check_token(user, token):
                user.is_active = True
                user.save()
                return Response({"message": "Аккаунт успешно активирован."}, status=status.HTTP_200_OK)
            return Response({"error": "Недействительная ссылка активации."}, status=status.HTTP_400_BAD_REQUEST)
        except Exception:
            return Response({"error": "Ошибка при активации аккаунта."}, status=status.HTTP_400_BAD_REQUEST)

class UserViewSet(viewsets.ModelViewSet):  # теперь полный CRUD
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        if self.action == 'list':
            return [permissions.IsAdminUser()]
        elif self.action in ['retrieve', 'update', 'partial_update', 'destroy']:
            return [IsAdminOrSelf()]
        return [permissions.AllowAny()]
