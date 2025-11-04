
print("Привет! Это викторина по английскому языку. Тебе нужно заполнить пропущенные слова.")


name = input("Как тебя зовут? ")


print(f"Привет, {name}! Начинаем тест! Всего 5 вопросов. Напиши 'stop', чтобы выйти.")


questions = [
    "My name ___ Vova.",    
    "I ___ a coder.",       
    "I live ___ Moscow.",   
    "She ___ from London.", 
    "We ___ learning Python." 
]

answers = ["is", "am", "in", "is", "are"]


correct_answers = 0
total_score = 0
attempts = 0


for i in range(len(questions)):
    print(i + 1, questions[i])
    
    ans = input("Введите ответ: ").strip().lower()
    
    
    if ans == "stop":
        print("Завершили тест досрочно.")
        break
    
    if ans == "":
        print("Пропустили текущий вопрос.")
        continue
    
    
    if ans == answers[i]:
        print("Верно!")
        correct_answers += 1
        total_score += 10
        attempts += 1
    else:
        print(f"Неверно. Правильно: {answers[i]}")
        attempts += 1


percent = (correct_answers / attempts) * 100 if attempts > 0 else 0
print("\nИтоги:")
print(f"Вопросов всего: {len(questions)}")
print(f"Правильных ответов: {correct_answers}")
print(f"Баллов: {total_score}")
print(f"Процент правильных: {round(percent, 2)}%")