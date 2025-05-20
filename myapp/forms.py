from django import forms

class ChatForm(forms.Form):
    user_message = forms.CharField(
        label='Ваше сообщение',
        widget=forms.TextInput(attrs={
            'placeholder': 'Введите ваше сообщение...',
            'class': 'chat-input',
            'id': 'userInput'
        }),
        max_length=500,
        required=True
    )