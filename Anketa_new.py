name = input('Как вас зовут? ')
age = int(input('Сколько вам лет? '))
x = 0
print("Здраствуйте, " +str(name) + "." + " Ваш возвраст " +str(age)+".") 
print("Ваш любимый цвет? (1 - Красный, 2 - Синий, 3 - Желтый)")
color = int(input())
if color == 2:
    x += 1
print("Ваша люимая музыка? (1 - Хип-хоп, 2 - Шансон, 3 - Классика)")
music = int(input())
if music == 1:
    x += 1
print("Ваше любимое время года? (1 - Осень, 2 - зима, 3 - Весна, 4 - Лето)")
season = int(input())
if season == 4:
    x += 1
print("Ты читаешь книги? (1 - да, 2 - нет)")
reading = int(input())
if reading == 1:
    x +=1
print("Ты играешь в видеоигры? (1 - да, 2 = нет)")
game = int(input())
if game == 1:
    x += 1
print("ты умеешь готовить? (1 - да, 2 - нет)")
food = int(input())
if food == 2:
    x += 1
print("Тебе нравятся машины?(1 - да, 2 - нет)")
lovecars = int(input())
if lovecars == 1:
    x += 1
print("Ты еврей?(1 - да, 2 - нет)")
nac = int(input())
if nac == 2:
    x += 1
if x == 8:
    print("Вы мне интересны")
elif x >= 4:
    print("мы может быть подружимся")
else:
    print("Нам с вами не по пути")
