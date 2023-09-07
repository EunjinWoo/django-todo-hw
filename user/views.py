from django.shortcuts import render
from .models import UserModel
from django.http import HttpResponse
from django.contrib.auth import get_user_model
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
def sign_up_view(request):
    if request.method == 'GET':
        pass
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
        pass