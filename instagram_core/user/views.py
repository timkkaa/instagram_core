from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import TemplateView
from user.models import CustomUser





class CreateNewPostView(View):

    def post(self, request, *args, **kwargs):
        current_user = self.request.user  # получаем пользователя который хочет загрузить публикацию

        data = request.POST
        files = request.FILES

        Publication.objects.create(
            preview_image=files['image-upload'],
            author=current_user,
            description=data['description']
        )
        return redirect('home-url')

class MakeLoginView(View):
    template_name = 'login.html'

    def post(self, request, *args, **kwargs):
        data = request.POST
        username = data['username']
        password = data['password']

        user = CustomUser.objects.get(username=username)
        print('пользователь ', user)

        correct = user.check_password(password)
        print('коррект равен ', correct)

        if correct == True:
            login(request, user)
            return render(request, 'login.html', context={'logged_in': True})
        else:
            return render(request, 'login.html', context={'logged_in': False})


class LoginView(TemplateView):
    template_name = 'login.html'

class MakeRegistrationView(View):
    template_name = 'sign_up.html'

    def post(self, request, *args, **kwargs):
        data = request.POST

        password = data['password']  # Берем только одно поле пароля
        username = data['username']
        first_name = data['first_name']
        last_name = data['last_name']

        if CustomUser.objects.filter(username=username).exists():
            return render(request, 'sign_up.html')

        user = CustomUser.objects.create_user(
            username=username, password=password,
            first_name=first_name, last_name=last_name,
        )

        return render(request, 'profile-url')

class RegistrationView(TemplateView):
    template_name = 'sign_up.html'

class MyProfilePageView(TemplateView):
    template_name = "profile.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        current_user = self.request.user

        # followers_count = current_user.my_followers.all().count()
        # following_count = current_user.my_following.all().count()
        followers_count = 55
        following_count = 55

        # publications_count = current_user.my_publications.all().count()
        publications_count = 55
        context.update({
            'followers_count': followers_count,
            'following_count': following_count,
            'publications_count': publications_count,
            'user': current_user,
        })

        return context


class HomeView(TemplateView):
    template_name = 'home.html'
