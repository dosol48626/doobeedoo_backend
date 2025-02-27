from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSerializer
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import PasswordChangeSerializer

#이게 회원가입
class RegisterView(APIView):
    def post(self, request):

        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save() #여기서 직렬화한거 확인되면 저장하는거임.
            return Response({"message": "회원가입이 완료되었습니다.", "user": serializer.data}, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#이게 로그인
class LoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        #사실 나도 라이브러리 전부 다 알지는 못함...이거 어센틱케이트하면 알아서 해줌;;ㅎㅎ
        user = authenticate(username=username, password=password)

        if user is not None:
            refresh = RefreshToken.for_user(user)
            return Response({
                'access': str(refresh.access_token),
                'refresh': str(refresh)
            }, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

#이게 로그아웃
class LogoutView(APIView):
    def post(self, request):
        # 별도의 토큰 무효화 작업 없이 클라이언트가 토큰을 삭제하도록 안내
        return Response({"message": "로그아웃 성공. 클라이언트에서 토큰을 삭제하세요."}, status=status.HTTP_200_OK)

#이게 비밀번호 변경
class PasswordChangeView(APIView):
    def put(self, request):
        serializer = PasswordChangeSerializer(data=request.data)
        if serializer.is_valid():
            user = request.user  # 토큰 인증을 통해 현재 사용자 가져옴
            if not user.check_password(serializer.validated_data['old_password']):
                return Response({"error": "기존 비밀번호가 틀립니다."}, status=status.HTTP_400_BAD_REQUEST)
            user.set_password(serializer.validated_data['new_password'])
            user.save()
            return Response({"message": "비밀번호가 성공적으로 변경되었습니다."}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#이게 회원탈퇴  
class DeleteAccountView(APIView):
    def delete(self, request):
        user = request.user
        user.delete()
        return Response({"message": "회원 탈퇴가 완료되었습니다."}, status=status.HTTP_200_OK)


#https://www.django-rest-framework.org/api-guide/views/ 여기 참고함.
#https://www.django-rest-framework.org/api-guide/authentication/ 여기 참고함.