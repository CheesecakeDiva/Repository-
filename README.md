Декораторы

Задача 1. Измерьте с помощью декоратора measure_execution_time продолжительность HTTP запроса к произвольному url (можно взять код из первых уроков по ботам)

Задача 2. 
Описание задачи:
Необходимо разработать декоратор requires_admin, который будет использоваться для проверки роли пользователя перед выполнением защищенной функции. Если роль пользователя не соответствует требуемой, декоратор должен выбрасывать исключение PermissionError. В противном случае функция должна выполняться корректно.
Пример использования:

Функция delete_user отвечает за удаление пользователей. Она должна быть доступна только для пользователей с ролью "admin".  Если пользователь, вызывающий эту функцию, не является администратором, необходимо остановить выполнение функции и выбросить PermissionError.

@requires_admin
def delete_user(user, username_to_delete):
    return f"User {username_to_delete} has been deleted by {user['username']}."



# Пример юзеров
admin_user = {'username': 'Alice', 'role': 'admin'}
regular_user = {'username': 'Bob', 'role': 'user'}

# Вызовы функции
print(delete_user(admin_user, 'Charlie')) # Должно отработать
print(delete_user(regular_user, 'Charlie')) # Должно рейзить PermissionError
