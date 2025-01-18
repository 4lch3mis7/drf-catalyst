from rest_framework import generics, status
from rest_framework.permissions import AllowAny

from authusers.models import User
from drf_catalyst.response_handler import success_response

from .serializers import RegisterSerializer, UserSerializer


class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    permission_classes = (AllowAny,)

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user: User = serializer.save()
        user.set_password(serializer.validated_data.get("password"))
        user.save()

        return success_response(
            data=UserSerializer(user).data,
            message="User registered successfully",
            status_code=status.HTTP_201_CREATED,
        )
