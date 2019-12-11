from django.http import JsonResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.core.validators import validate_email,ValidationError #이메일값
from django.contrib.auth import authenticate,login,logout

class BaseView(View):
    
    @staticmethod
    def response(data={}, message='',status=200):
        result = {
            'data': data,
            'message': message,
        }
        return JsonResponse(result, status=status)


#회원가입
class UserCreateView(BaseView):
    @method_decorator(csrf_exempt) #장고에세 post로 이용할때 발생하는 문제를 보안하는 문법
    def dispatch(self, request, *args, **kwargs):
        return super(UserCreateView, self).dispatch(request, *args, **kwargs)
    
    #검증로직
    def post(self, request):
        # Restful 하게 하기 위해선 POST, DELETE 다 나누어야 하지만, 편의상 POST만 사용하도록 하겠다.
        username = request.POST.get('username', '')
        if not username:
            return self.response(message='아이디를 입력해주세요.', status=400)
        password = request.POST.get('password', '')
        if not password:
            return self.response(message='패스워드를 입력해주세요.', status=400)
        email = request.POST.get('email', '')
        try:
            validate_email(email)
        except ValidationError:
            return self.response(message='올바른 이메일을 입력해주세요.', status=400)

        try:
            user = User.objects.create_user(username, email, password)
        except IntegrityError:
            return self.response(message='이미 존재하는 아이디입니다.', status=400)

        return self.response({'user.id': user.id})


#로그인
class UserLoginView(BaseView):
    @method_decorator(csrf_exempt) #장고에세 post로 이용할때 발생하는 문제를 보안하는 문법
    def dispatch(self, request, *args, **kwargs):
        return super(UserLoginView, self).dispatch(request, *args, **kwargs)
    
    def post(self,request):
        username = request.POST.get('username','')
        if not username:
            return self.response(message='아이디를 입력하세요',status = 400)
        password = request.POST.get('password','')
        if not password:
            return self.response(message='비밀번호를 입력하세요', status = 400)
        
        user = authenticate(request, username = username, password = password)
        if user is None:
            return self.response(message='아이디혹은 비밀번호가 틀렸습니다.', status=400)
        
        login(request,user)
        return self.response()

#로그아웃
class UserLogoutView(BaseView):
    def get(self,request):
        logout(request)
        return self.response()
    