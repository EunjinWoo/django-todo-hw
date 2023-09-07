from django.shortcuts import render, redirect
from .models import UserModel
from django.http import HttpResponse
from django.contrib.auth import get_user_model
from django.contrib import auth
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
def sign_up_view(request):
    if request.method == 'GET':
        user = request.user.is_authenticated  # 인증된 사용자를 user라는 변수에 입력
        if user:
            return HttpResponse('이미 로그인 되었습니다. 홈페이지 보여주기')
        else:
            return HttpResponse('회원가입 페이지')

    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        password2 = request.POST.get('password2', '')
        email = request.POST.get('email', '')

        if password != password2:
            return HttpResponse('패스워드가 일치하지 않습니다.')
        else:
            exist_user = get_user_model().objects.filter(username=username)
            if exist_user:
                return HttpResponse('같은 이름의 사용자가 존재합니다.')
            if username == '' or password == '':
                return HttpResponse('사용자 이름과 비밀번호는 필수 값입니다.')

        UserModel.objects.create_user(username=username, password=password, email=email)

    return HttpResponse('sign up succeeded')

@csrf_exempt
def sign_in_view(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')

        me = auth.authenticate(request, username=username, password=password)
        if me is not None:
            auth.login(request, me)
            return HttpResponse("로그인 완료")
        else:
            return HttpResponse('유저이름 혹은 패스워드를 확인해주세요.')

    elif request.method == 'GET':
        user = request.user.is_authenticated  # 인증된 사용자를 user라는 변수에 입력
        if user:
            return HttpResponse('이미 로그인 됨. 홈페이지 보여주기')
        else:
            return HttpResponse('로그인 페이지.')