from django.contrib.auth import authenticate, login, logout
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class LoginView(APIView):
    """
    Ручка для входа грузчика в систему.
    """
    def post(self, request):
        passport = request.data.get("passport")
        password = request.data.get("password")

        if not passport or not password:
            return Response(
                {"detail": "Passport and password are required."},
                status=status.HTTP_400_BAD_REQUEST
            )

        user = authenticate(request, username=passport, password=password)
        if user is not None:
            login(request, user)  # Создаёт сессию для пользователя
            return Response({"detail": "Login successful."}, status=status.HTTP_200_OK)
        
        return Response(
            {"detail": "Invalid passport or password."},
            status=status.HTTP_401_UNAUTHORIZED
        )


class LogoutView(APIView):
    """
    Ручка для выхода грузчика из системы.
    """
    def post(self, request):
        logout(request)  # Удаляет текущую сессию пользователя
        return Response({"detail": "Logout successful."}, status=status.HTTP_200_OK)


class CheckAuthView(APIView):
    """
    Ручка для проверки аутентификации.
    """
    def get(self, request):
        if request.user.is_authenticated:
            return Response(
                {"detail": "User is authenticated.", "user": str(request.user)},
                status=status.HTTP_200_OK
            )
        return Response({"detail": "User is not authenticated."}, status=status.HTTP_401_UNAUTHORIZED)
