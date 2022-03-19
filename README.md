# lidiya
Лидия, простейший скрипт мониторящий новые посты в определенных группах ВКонтакте на наличие ключевых слов и отправляющий появившиеся посты в чат Телеграм.
Написан для нужд добровольческого поискового отряда ЛизаАлерт в Мордовии.
https://en.wikipedia.org/wiki/Liza_Alert

Используются библиотеки:
vk-api
pyTelegramBotAPI
sqlite3

## Установка

### Скрипт

Создаем каталог, например 
```
mkdir /myvenv/lida13-bot
```
Копируем туда скрипты main.py.
Открываем и вбиваем настройки.


### Создание виртуального окружения
```
python3 -m venv /myvenv/lida13-bot
```

Переходим в этот каталог, затем активируем:
```
. bin/activate
```

Устанавливаем зависимости:
```
pip3 install vk-api
pip3 install pyTelegramBotAPI
```

Делаем файл исполнимым:
```
chmod +x main.py
```

Выходим из окружения:
```
deactivate
```

### База данных
В любой программе (например SQLiteStudio) создаем базу и кидаем её на сервер.

Структура:
```
CREATE TABLE Posts (
  num       INTEGER PRIMARY KEY AUTOINCREMENT,
  post_id   INTEGER,
  post_date INTEGER
);
```

### Получение токена ВКонтакте
Приложение создается вот тут: https://vk.com/apps?act=manage
Нам будет нужен AppID и Token

Авторизацию не используем, в нашем случае стены публичные, доступны и без неё.

### Создание бота Телеграм
Всё как обычно. Пишем @BotFather, получаем ключик.
Самый простой способ узнать идентификаторы нужных чатов это запустить (как угодно, хоть локально), следующий скриптик:
```
import telebot

bot = telebot.TeleBot("key api")

@bot.message_handler(commands=['userinfo'])
def send_userinfo(message):
    chat_id = str(message.chat.id)
    user_id = message.from_user.id
    bot.send_message(chat_id, "Chat_id:" + str(chat_id) + ", User_id:" + str(user_id))

if __name__ == '__main__':
    bot.polling()
```
Добавляем бота в нужный чат поиском по имени (его всё равно туда добавлять), и пишем ему команду "/userinfo", он ответит ID чата (обычно начинается с минуса).


### Настройки скрипта
Создаем файл conf.py (в репозитории его нет!)
Названия групп берем из адресной строки (только группа, не адрес целиком)

```
token = ""
app_id = ""
groups_list = {"группа1", "группа2"}

key_api = ""

chat_id = ""

words_list = {"пропал", "найти человека", "пропав", "безвести", "без вести", "розыск"}
words_black_list = {"кража", "фальшивка"}
```

words_list - список тех слов, которые нам интересны

words_black_list - стоп слова, новости с которыми можно не показывать


## Автоматический запуск

Для того чтобы скрипт запускался автоматически каждое утром,
копируем файлы .service и .timer в /etc/systemd/system/

Затем следует обновить сервисы:
```
systemctl daemon_reload
```

Можно проверить, что всё работает:
```
systemctl start locarus_emailer_bot.service
```

Разовый запуск таймера для проверки:
```
systemctl start lida13-bot.timer
```

Включить:
```
systemctl enable lida13-bot.timer
```

Сейчас таймер настроен так, чтобы запускать скрипт три раза в час.

Всё готово. 
