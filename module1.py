import random 
nimed = []
keskmised_hinnad = []

def lapsed(): #запрашивает имена детей и генерирует случайную оценку
    n = int(input("sisestage laste arv: ")) #напишите имя ребенка
    for i in range(n): #переменная i будет выполнятся столько раз сколько будет n
        nimi = input(f"sisestage lapse nimi {i+1}: ") #напиши имя ребенка 
        nimed.append(nimi)
        keskmine_hinne = round(random.uniform(3, 5), 2) #средняя оценка округляется, возравщается случайное число
        keskmised_hinnad.append(keskmine_hinne) 
def näidata_nimi(): #показать имя
    sorted_names = sorted(zip(nimed, keskmised_hinnad)) #сортирует и обьеденяеняет именa и оценки
    for nimi, hinne in sorted_names:
        print(nimi, "-", hinne) #показывает на экран имена и оценки

def parim_hinnad(): #лучшие оценки
    parim = False  
    for nimi, hinne in zip(nimed, keskmised_hinnad):#обьеденяет оценки и имена
        if hinne == 5: #если оценка 5 это лучшая оценка
            print(nimi)
            parim = True
    if not parim: #если нету лучшей оценки
        print("Suurepäraseid õpilasi pole")

def keskmist_hinnad(): #средние оценки всех детей
    average = sum(keskmised_hinnad) / len(keskmised_hinnad) #обьеденяет оценки и возвращает длину количества элементов
    print(f"Laste keskmiste hinnete keskmine hinne: {average}") #принтует среднюю оценку

def keskmine_hind(): #средняя оценка определенного ребенка
    nimi = input("Sisesta lapse nimi: ") #ввести имя ребенка 
    if nimi in nimed:
        keskmine_hinne = sum([hinne for n, hinne in zip(nimed, keskmised_hinnad) if n == nimi]) / nimed.count(nimi) #суммирует и соединяет оценку и имя и считает среднюю оценку со всех учеников
        print(f"Õpilaste keskmine hinne {nimi}: {keskmine_hinne}") #принтует среднюю оценку и имя 
    else:
        print("Last ei leitud")

def minimum_hind(keskmised_hinnad): #минимальная оценка
    min_hind=min(keskmised_hinnad)
    min_ind = keskmised_hinnad.index(min_hind)
    nimi=nimed[min_ind]
    print(min_ind,nimi)

    
    
    pass

lapsed()

