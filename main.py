# -*- coding: utf-8 -*-
import vk_api
from conf import app_id, token, groups_list
from time import sleep
from storage import Storage, Post
from word_checker import find_words_in_post
from telegram import Telegram


def main():
    vk_session = vk_api.VkApi(app_id=app_id, token=token)
    vk = vk_session.get_api()

    bot_storage = Storage()
    bot_telegram = Telegram()


    def read_wall(name):
        response = vk.wall.get(count=4, domain=name)  # Используем метод wall.get

        if response['items']:
            for post in response['items']:

                post_for_check = Post(post['id'], post['date'], post['text'], f"https://vk.com/{name}")

                if bot_storage.check_and_storage_post(post_for_check):
                    if find_words_in_post(post_for_check.post_text):
                        bot_telegram.send_footer()
                        bot_telegram.send(f"новый пост в {post_for_check.group_link}")
                        bot_telegram.send(post_for_check.post_text)

    for group in groups_list:
        read_wall(group)
        sleep(1)

    bot_storage.close()


if __name__ == '__main__':
    main()
