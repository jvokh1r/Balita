from django.shortcuts import render, redirect
from .forms import FormContact
from .models import Contact


def index(request):
    form = FormContact(request.POST or None)
    if form.is_valid():
        form.save()
    if request.method == "POST":
        # name = request.POST.get('ism')
        # phone = request.POST.get('phone')
        # email = request.POST.get('email')
        # msg = request.POST.get('msg')
        # Contact.objects.create(name='name', phone='phone', email='email', msg='msg')
        return redirect('/contact')
    # context = {
    #     'form': form,
    # }

    return render(request, 'contact.html', {})


