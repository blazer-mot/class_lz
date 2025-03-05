from Oktagon import Oktagon #импортируем класс

def main(): #создаем функцию 
    first = Oktagon(13) #добавляем объект
    first.plosh() #используем все методы
    first.per()
    first.vpisan_okr()
    first.opisan_okr()
    first.grafik()

if __name__ == '__main__': #проверяем на прямой запуск
    main() #запускаем функцию
    