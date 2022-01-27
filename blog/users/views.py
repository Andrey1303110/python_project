import datetime
from django.db.models import Q
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, get_user_model
from .forms import LoginForm, UserRegisterForm, MessageForm, OfferBuyForm
from django.contrib import messages
from .models import MyUser, Message, Offer, UserOffers


def login_user(request):
    data = {
        'title': 'Login Page',
        'button_text': 'sign in',
        'form': LoginForm(),
    }
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            user = authenticate(
                username=cleaned_data['username'],
                password=cleaned_data['password'],
            )
            if user is not None:
                login(request, user)
                return redirect('news_home')
            else:
                messages.error(request, 'Вы ввели неверный пароль или логин!')
                return render(request, 'registration/login.html', data)
        else:
            messages.error(request, 'Поля были неверно заполнены!')
            return render(request, 'registration/login.html', data)
    else:
        return render(request, 'registration/login.html', data)


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Вы успешно зарегистрировались!')
            return redirect('news_home')
        else:
            messages.error(request, 'Ошибка регистрации!')
            return redirect('register')
    else:
        data = {
            'title': 'Registration Page',
            'button_text': 'registration',
            'form': UserRegisterForm(),
        }
        return render(request, 'registration/register.html', data)


def logout_user(request):
    logout(request)
    return redirect('login')


def my_profile(request):
    data = {
        'title': 'My profile',
    }
    return render(request, 'main/profile.html', data)


def chat(request):
    users_list = MyUser.objects.all()
    user = request.user
    messages = Message.objects.filter(
            Q(from_message=user) |
            Q(to_message=user)
        ).order_by('-time')
    data = {
        'users_list': users_list,
        'form': MessageForm(),
        'messages': messages
    }

    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.from_message = request.user
            instance.time = datetime.datetime.now()
            instance.save()
            return redirect('chat')

    return render(request, 'chat/main.html', data)


def all_offers(request):
    user = request.user
    offers = Offer.objects.order_by('price')
    offers_list = []

    for idx, offer in enumerate(offers):
        offers_list.append(
            {'id': idx + 1,
             'inst': offer,
             'conf': UserOffers.objects.filter(offer_title=offer, offer_owner=user)}
        )

    data = {
        'all_offers': offers_list,
        'form': OfferBuyForm(),
    }

    if request.method == 'POST':
        offer_id = int(request.POST.get('offer_id'))
        offer = Offer.objects.get(pk=offer_id)

        instance = UserOffers.objects.create(
            time=datetime.datetime.now(),
            offer_owner=request.user,
            offer_title=offer
        )
        return redirect('my_offers')

    return render(request, 'main/offers.html', data)


def my_offers(request):
    user = request.user
    confirmed_offers = []
    offers = UserOffers.objects.filter(offer_owner=user).order_by('-time')

    for idx, offer in enumerate(offers):
        confirmed_offers.append(
            {
                'id': idx + 1,
                'img': Offer.objects.get(title=offer.offer_title),
                'inst': offer,
            }
        )

    data = {
        'confirmed_offers': confirmed_offers,
        'form': OfferBuyForm(),
    }

    if request.method == 'POST':
        offer_id = int(request.POST.get('offer_id'))
        UserOffers.objects.get(pk=offer_id).delete()
        return redirect('my_offers')

    return render(request, 'main/my_offers.html', data)

