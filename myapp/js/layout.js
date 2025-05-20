
        function manageDarkMode() {
            const savedMode = localStorage.getItem('darkMode');
            const systemPrefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;

            if (savedMode === 'true' || (savedMode === null && systemPrefersDark)) {
                document.body.classList.add('dark-mode');
                updateThemeIcon(true);
            }

            const themeToggle = document.getElementById('themeToggle');
            if (themeToggle) {
                themeToggle.addEventListener('click', function() {
                    const isDark = !document.body.classList.contains('dark-mode');
                    document.body.classList.toggle('dark-mode', isDark);
                    localStorage.setItem('darkMode', isDark);
                    updateThemeIcon(isDark);
                });
            }

            function updateThemeIcon(isDark) {
                const icon = document.querySelector('#themeToggle i');
                if (icon) {
                    icon.classList.toggle('fa-moon', !isDark);
                    icon.classList.toggle('fa-sun', isDark);
                }
            }

            window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change', e => {
                if (!localStorage.getItem('darkMode')) {
                    document.body.classList.toggle('dark-mode', e.matches);
                    updateThemeIcon(e.matches);
                }
            });
        }

        document.addEventListener('DOMContentLoaded', manageDarkMode);

        /*chat*/
        $(document).ready(function(){

    // Устанавливаем CSRF токен для всех AJAX-запросов
    $.ajaxSetup({
        headers: { "X-CSRFToken": $('meta[name="csrf-token"]').attr('content') }
    });

    // Открыть чат
    $('#open-chat').click(function(){
        $('#chat-modal').css('display', 'flex');
    });

    // Закрыть чат
    $('#close-chat').click(function(){
        $('#chat-modal').hide();
    });

    // Клик по кнопке отправки
    $('#send-button').click(function(){
        sendMessage();
    });

    // Отправка по Enter
    $('#message-input').keypress(function(e){
        if(e.which == 13){
            sendMessage();
        }
    });

    function sendMessage() {
        var message = $('#message-input').val();
        if (message.trim() === '') return;

        // Показать сообщение пользователя
        $('#chat-box').append('<div><b>Вы:</b> ' + message + '</div>');

        // Отправка запроса на сервер
        $.ajax({
            url: "/chat/",  // URL правильный
            type: "POST",
            contentType: "application/json",
            data: JSON.stringify({ 'message': message }),
            success: function(response){
                $('#chat-box').append('<div><b>Бот:</b> ' + response.response + '</div>');
                $('#message-input').val('');
                $('#chat-box').scrollTop($('#chat-box')[0].scrollHeight);
            },
            error: function(xhr, status, error) {
                $('#chat-box').append('<div><b>Ошибка:</b> не удалось отправить сообщение.</div>');
            }
        });
    }
});