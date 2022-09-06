"""

Домашнее задание №1

Условный оператор: Сравнение строк

* Написать функцию, которая принимает на вход две строки
* Проверить, является ли то, что передано функции, строками. 
  Если нет - вернуть 0
* Если строки одинаковые, вернуть 1
* Если строки разные и первая длиннее, вернуть 2
* Если строки разные и вторая строка 'learn', возвращает 3
* Вызвать функцию несколько раз, передавая ей разные праметры 
  и выводя на экран результаты

"""
def string_func(stroka1, stroka2):
  if type(stroka1) != type('s') or type(stroka2) != type('s'):
    return '0'
  if stroka1 == stroka2:
    return 1
  if len(stroka1) != len(stroka2) and stroka2 == 'learn':
    return 3
  elif len(stroka1) != len(stroka2) and len(stroka1) > len(stroka2):
    return 2
  
    

def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    print(string_func('aa',2)) # 0
    print(string_func('aa','aa') )# 1
    print(string_func('aaaa','aa') )# 2
    print(string_func('aaaabbbccc','learn')) # 3
    
if __name__ == "__main__":
    main()
