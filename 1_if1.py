"""

Домашнее задание №1

Условный оператор: Возраст

* Попросить пользователя ввести возраст при помощи input и положить 
  результат в переменную
* Написать функцию, которая по возрасту определит, чем должен заниматься пользователь: 
  учиться в детском саду, школе, ВУЗе или работать
* Вызвать функцию, передав ей возраст пользователя и положить результат 
  работы функции в переменную
* Вывести содержимое переменной на экран

"""
def occupation(age):
   if age<0 or age>120: return 'error'
   elif age>0 and age<6: return 'daycare'
   elif age>6 and age<18: return 'school'
   elif age>18 and age<22: return 'university'
   elif age>22 and age<120: return 'work'

def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    age=int(input('Введите возраст '))
    print(occupation(age))

if __name__ == "__main__":
    main()