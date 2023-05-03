import sqlite3

from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate


def index_page(request):
    return render(request, 'index.html')


def login(request):
    if request.method == 'POST':
        # Отримуємо дані форми
        username = request.POST['username']
        password = request.POST['password']

        # Перевіряємо коректність введення логіна та пароля
        conn = sqlite3.connect('C:/Users/sidor/PycharmProjects/tele_web_bot/users.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE login=? AND password=?", (username, password))
        user = cursor.fetchone()
        conn.close()

        if user is not None:
            # Якщо введено коректні дані, перенаправлення на сторінку home
            return redirect('home')
        else:
            # Якщо введено некоректні дані, повідомлення про помилку та повторна відображення сторінки логіну
            return render(request, 'login.html', {'error_message': 'Невірний логін або пароль'})
    else:
        return render(request, 'login.html')


def home(request):
    return render(request, 'home.html')


def home_args(request):
    conn = sqlite3.connect('C:\\Users\\sidor\\PycharmProjects\\tele_web_bot\\users.db')
    cursor = conn.cursor()
    cursor.execute("SELECT full_name, username, user_id FROM users")
    result = cursor.fetchone()
    full_name = result[0]
    username = result[1]
    user_id = result[2]
    conn.close()
    context = {
        'full_name': full_name,
        'username': username,
        'user_id': user_id
    }
    return render(request, 'home.html', context)
