from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser

ACCOUNT_TYPE = [
    ('1', 'Base'),
    ('2', 'Expert'),
    ('3', 'Pro'),
]


class MyUserManager(BaseUserManager):

    def create_user(self, email, fio, telegram, money, companys, password=None, account_type=ACCOUNT_TYPE[0]):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            fio=fio,
            telegram=telegram,
            money=money,
            companys=companys,
            accout_type=account_type
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, account_type=ACCOUNT_TYPE[2]):
        user = self.create_user(
            email,
            password=password,
            fio='admin',
            telegram='admin',
            companys=0,
            money=0,
            account_type=account_type
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class MyUser(AbstractBaseUser):
    email = models.EmailField('Email', max_length=255, unique=True)
    fio = models.CharField('ФИО', max_length=100, default='', blank=False)
    telegram = models.CharField('Telegram', max_length=100, default='', blank=False)
    money = models.IntegerField('Баланс', default=0, blank=False)
    companys = models.IntegerField('Кампаний', default=0, blank=False)
    is_active = models.BooleanField(default=True, blank=False)
    is_admin = models.BooleanField(default=False, blank=False)
    account_type = models.CharField(choices=ACCOUNT_TYPE, max_length=10, default='1', verbose_name='Тип аккаунта')
    avatar = models.ImageField('Аватар', upload_to='images/', default='static/main/img/stock_avatar.png', null=True)

    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['fio', 'telegram']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin


class Message(models.Model):
    text_message = models.CharField('Текст', max_length=500, default='', blank=False)
    from_message = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    to_message = models.EmailField('Получатель', default='', blank=False)
    time = models.DateTimeField('Время отправки')

    def __str__(self):
        return self.text_message


class Offer(models.Model):
    title = models.CharField('Название', max_length=200, default='', blank=False)
    description = models.CharField('Описание', max_length=1000, default='', blank=False)
    price = models.IntegerField('Цена', default='', blank=False)
    profit = models.IntegerField('Профит', default='', blank=False)
    image = models.ImageField('Изображение', upload_to='images/', default='static/main/img/offer_default.png', null=True)

    def __str__(self):
        return self.title


class UserOffers(models.Model):
    offer_owner = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name="email_user")
    offer_title = models.ForeignKey(Offer, on_delete=models.CASCADE, related_name="title_offer")
    time = models.DateTimeField('Время добавления')

    def __str__(self):
        return str(self.offer_owner)
