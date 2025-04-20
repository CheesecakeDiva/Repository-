#Задание 1:

import wikipediaapi
import requests
import time
from functools import wraps

#объект Wikipedia с указанием пользовательского агента
user_agent = "MyWikipediaApp/1.0 (https://example.com; myemail@example.com)"
wiki_wiki = wikipediaapi.Wikipedia(language='ru', user_agent=user_agent)

# Декоратор для измерения времени выполнения функции
def measure_execution_time(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()  # время начала
        result = func(*args, **kwargs)  # оригинальная функция
        end_time = time.time()  # время окончания
        execution_time = end_time - start_time  # время выполнения
        print(f"Время выполнения {func.__name__}: {execution_time:.4f} секунд")
        #func.__name__: атрибут функции, который возвращает имя функции
        #.4f число будет отображаться с плавающей точкой и с 4 знаками после запятой
        return result  # результат оригинальной функции

    return wrapper

# Функция для получения случайной статьи из Википедии
@measure_execution_time
def get_random_article():
    response = requests.get("https://ru.wikipedia.org/w/api.php", params={
        "action": "query",
        "format": "json",
        "list": "random",
        "rnlimit": 1,
        "rnnamespace": 0,
    })
    data = response.json()
    return data['query']['random'][0]['title']

# Функция для получения содержания статьи по заголовку
@measure_execution_time
def get_article_summary(title):
    page = wiki_wiki.page(title)
    if page.exists():
        return page.summary
    else:
        raise ValueError("Статья не найдена.")

if __name__ == "__main__":
    while True:
        print("Выберите действие:")
        print("1. Получить рандомную статью")
        print("2. Получить содержание статьи")
        print("3. Выход")

        choice = input("Введите номер действия: ")

        if choice == "1":
            current_page_title = get_random_article()
            print(f"Случайная статья: {current_page_title}")

        elif choice == "2":
            if 'current_page_title' in locals():
                try:
                    page_summary = get_article_summary(current_page_title)
                    print(f"Содержание статьи '{current_page_title}':\n{page_summary}")
                except Exception as e:
                    print(f"Произошла ошибка: {e}. Попробуйте другую статью.")
            else:
                print("Сначала получите рандомную статью.")

        elif choice == "3":
            print("Выход из программы.")
            break

        else:
            print("Неверный ввод. Пожалуйста, выберите действие снова.")



#Задание 2:

def requires_admin(func):
    def wrapper(user, *args, **kwargs):
        if user.get('role') != 'admin':
            raise PermissionError("У вас нет прав для выполнения этой операции")
        return func(user, *args, **kwargs)
    return wrapper

@requires_admin
def delete_user(user, username_to_delete):
    return f"User {username_to_delete} has been deleted by {user['username']}"

# Пример юзеров
admin_user = {'username': 'Alice', 'role': 'admin'}
regular_user = {'username': 'Bob', 'role': 'user'}

# Вызовы функции
try:
    print(delete_user(admin_user, 'Charlie'))
except PermissionError as e:
    print(e)

try:
    print(delete_user(regular_user, 'Charlie'))
except PermissionError as e:
    print(e)