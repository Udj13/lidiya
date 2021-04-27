# Пропал пропала
# Пропал человек
# Помогите найти человека
# Пропал без вести
# Безвести пропавший
# Без вести пропал/вший"
# ВниманиеРозыск #Розыск

import conf


def find_words_in_post(text: str):
    for word in conf.words_black_list:
        if text.lower().find(word) != -1:
            return False

    for word in conf.words_list:
        if text.lower().find(word) != -1:
            return True
    return False
