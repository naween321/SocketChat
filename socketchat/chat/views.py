from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from itertools import combinations


@login_required
def index(request):
    users = User.objects.exclude(username=request.user.username)
    user_list = list()
    rooms = list()
    all_users = User.objects.all()
    for user in all_users:
        user_list.append(user.username)
    tup_list = list(combinations(user_list, 2))
    print(tup_list)

    for tup in tup_list:
        rooms.append(tup[0] + tup[1])
    print(rooms)
    return render(request, 'index.html', {'users': users, 'rooms': rooms})


def add_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        u = User.objects.create(username=username, email=email, password=password, is_active=True, is_staff=True)
        u.set_password(password)
        u.save()
        return redirect('login')
    else:
        return render(request, 'add_user.html')