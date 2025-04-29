#() [] {}

user_string = input("Введите скобочную последовательность, используя только символы (,),[,],{,}:\n ")

brackets_open = ['(', '[', '{'] #открывающие скобки
brackets_close = [')', ']', '}'] #закрывающие скобки

stack = []
flVerify = True #флаг

for current_char in user_string:
    if current_char in brackets_open: #если скобка открывающая, то
        stack.append(current_char) #добавляем в стек открывающую скобку
    elif current_char in brackets_close: #если скобка закрывающая
        if len(stack) == 0: #смотрим, пуст ли стек, если стек пуст, значит у нас
            flVerify = False #нет сохранённых откр. скобок = нет пары = не подходит
            break


        last_open = stack.pop() #извлекаем последнюю добавленную в стек открывающую скобку
        if last_open == "(" and current_char == ")":
            continue
        if last_open == "[" and current_char == "]":
            continue
        if last_open == "{" and current_char == "}":
            continue

        flVerify = False
        break

if flVerify and len(stack) == 0:
    print("Скобочная последовательность сбалансирована")
else:
    print("Скобочная последовательность не сбалансирована")

