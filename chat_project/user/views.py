from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framwork import status
from .serializers import *


class Register(APIView):
    def post(self, request):
        serializers = UserSerializer(data=request.data)
        if serializers.is_valid():
            user = serializers.save()

            token = TokenObtainPairSerializer.get_token(user)
            refresh_token = str(token)
            access_token = str(token.access_token)
            res = Response(
                {
                    "user": serializers.data,
                    "message": "회원가입 완료",
                    "token": {
                        "access": access_token,
                        "refresh": refresh_token
                    }
                },
                status = status.HTTP_200_OK
            )

            res.set_cookie("access", access_token, httponly=True)
            res.set_cookie("refresh", access_token, httponly=True)

            return res
        return Response(serializers.errors, status = status.HTTP_400_BAD_REQUEST)


class Login(APIView):
    pass


class Logout(APIView):
    pass