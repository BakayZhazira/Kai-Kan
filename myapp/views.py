from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import requests
from .forms import ChatForm

OPENROUTER_API_KEY = "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"

def index(request):
    return render(request, 'myapp/index.html')

def about(request):
    return render(request, 'myapp/about.html')

def contact(request):
    return render(request, 'myapp/contact.html')

def login(request):
    return render(request, 'myapp/login.html')

def menu(request):
    return render(request, 'myapp/menu.html')

@csrf_exempt
def chat(request):
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        try:
            data = json.loads(request.body)
            user_message = data.get('message', '')
            bot_response = get_bot_response(user_message)
            return JsonResponse({'response': bot_response})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)

    chat_history = request.session.get('chat_history', [])

    if request.method == 'POST':
        form = ChatForm(request.POST)
        if form.is_valid():
            user_message = form.cleaned_data['user_message']
            bot_response = get_bot_response(user_message)

            chat_history.append({'user': user_message, 'bot': bot_response})
            request.session['chat_history'] = chat_history[-10:]
            return redirect('chat')
    else:
        form = ChatForm()

    return render(request, 'myapp/chat.html', {
        'form': form,
        'chat_history': chat_history
    })
def get_bot_response(user_message):
    try:
        headers = {
            "Authorization": f"Bearer {OPENROUTER_API_KEY}",
            "Content-Type": "application/json",
            "HTTP-Referer": "https://yourdomain.com/",
            "X-Title": "ChatBot KAI-KAN"
        }

        data = {
            "model": "openai/gpt-3.5-turbo",
            "messages": [
                {
                    "role": "system",
                    "content": (
                        "Ты — вежливый и информативный ассистент японского ресторана KAI-KAN. "
                        "Ресторан находится в Алматы, на ул. Сатпаева 22. Мы предлагаем японскую кухню высокого уровня: "
                        "суши, роллы, рамен, удон, сашими, бенто. Работаем каждый день с 12:00 до 23:00. "
                        "У нас есть доставка и возможность бронирования. Рассказывай про блюда, принимай запросы, предлагай помощь."
                    )
                },
                {"role": "user", "content": user_message}
            ]
        }

        response = requests.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, json=data)
        result = response.json()

        if "choices" in result:
            bot_message = result["choices"][0]["message"]["content"]
            return bot_message.strip()
        else:
            return "Извините, не удалось получить ответ от бота."
    except Exception as e:
        return f"Ошибка: {str(e)}"
