from module1 import *
while True:
        print("\nМеню:\n1. Отобразить имена детей в алфавитном порядке\n2. Отобразить отличника\n3. Найти среднюю оценку средних оценок детей\n4. Найти среднюю оценку ребенка\n5. Минимальная оценка \n6. Выход")
        valik = int(input("Введите номер действия: "))
        if valik == 1:
            näidata_nimi()
        elif valik == 2:
            parim_hinnad()
        elif valik == 3:
            keskmist_hinnad()
        elif valik == 4:
            keskmine_hind()
        elif valik == 5:
            minimum_hind(keskmised_hinnad)
        elif valik == 6:
            break
        else:
            print("Viga: vale sisend")
