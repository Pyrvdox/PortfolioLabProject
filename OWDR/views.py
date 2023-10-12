from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views import View

from OWDR.models import Donation, Institution, Category


# Create your views here.
class LandingPageView(View):
    def get(self, request):
        all_bags = Donation.objects.all().count()
        all_orgs = Institution.objects.all().count()

        fundations = Institution.objects.filter(type='fundacja')[:5]
        organizations = Institution.objects.filter(type='organizacja_pozarzadowa')[:5]
        locals = Institution.objects.filter(type='zbiorka_lokalna')[:5]

        context = {
            'all_bags':all_bags,
            'all_orgs':all_orgs,
            'funds':fundations,
            'orgs': organizations,
            'lcs':locals
        }
        return render(request, template_name='index.html', context=context)


class AddDonationView(LoginRequiredMixin, View):
    def get(self, request):
        category = Category.objects.all()
        instytutions = Institution.objects.all()
        context = {
            'category': category,
            'instytutions': instytutions
        }
        return render(request, template_name='form.html', context=context)


class RegisterView(View):
    def get(self, request):
        return render(request, template_name='register.html')
    def post(self, request):
        name = request.POST.get('name')
        surname = request.POST.get('surname')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        print(name, surname, email, password, password2)

        if password == password2:
            new_user = User.objects.create_user(first_name=name, last_name=surname, username=email, password=password)

            return render(request, template_name='login.html')
        return render(request, template_name='register.html')


class LoginView(View):
    def get(self, request):
        return render(request, template_name='login.html')

    def post(self, request):

        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('LandingPage')
        else:
            return redirect('Register')


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('LandingPage')


class FormConfirmView(View):
    def get(self, request):
        return render(request, template_name='form.html')

    def post(self, request):
        institution = request.POST['institution']
        categories = request.POST.getlist('categories')
        quantity = request.POST['bags']
        address = request.POST['address']
        phone_number = request.POST['phone']
        city = request.POST['city']
        zip_code = request.POST['zip_code']
        pick_up_date = request.POST['date']
        pick_up_time = request.POST['time']
        pick_up_comment = request.POST['more_info']
        user = request.user
        organization = Institution.objects.get(pk=institution)

        donation = Donation.objects.create(
            institution=organization,
            quantity=quantity,
            address=address,
            phone_number=phone_number,
            city=city,
            zip_code=zip_code,
            pick_up_date=pick_up_date,
            pick_up_time=pick_up_time,
            pick_up_comment=pick_up_comment,
            user=user
        )
        donation.categories.set(categories)
        donation.save()

        return redirect('thanksfordonation')


class ThanksView(View):
    def get(self, request):
        return render(request, template_name='form-confirmation.html')