### 3.1. Создание аннотированного списка библиотек для работы с текстом в Python. Формирование отчета по выполнению задания и размещение его в портфолио, персональном репозитории. 

### 3.2. Разработка сценария с реализацией операции поиска подстроки в тексте. 

```python
def main():
    input_str = input("Введите строку для поиска: ")

    searchable_str = input("Введите строку, которую мы ищем: ")
    
    choice = None
    while choice != '4':

        print('1 - поиск первого вхождения подстроки')
        print('2 - замена первой подстроки')

        print('3 - найти все вхождения подстроки' )

        print('4 - для выхода')
        choice = input("Сделайте  выбор (1..4) ")
        
        if choice == '1':
            res = search_str(searchable_str, input_str)
            print('Первое вхождение подстроки:', res)

        if choice == '2':
            rep_str = input("Строка для замены: ")
            res = search_n_replace_str(input_str,rep_str,searchable_str)
            print('Измененная строка: ', res)

            # найти функцию, позволяющую осуществлять замену подстроки строкой

        if choice == '3':
            result = 0
            res = []
            k = 0
            while k < len(input_str):
                k = input_str.find(searchable_str, k)
                if k == -1:
                    break
                else:
                    result += 1
                    res.append(k)
                    k += 1
            print('Колличесвто вхождений подстроки: ', result)
            print('Все вхождения подстроки:', res)      

def search_str(what="", where=""):
    res = where.find(what)
    return res

def search_n_replace_str(what="",  to_what="", where=""):
    res = what.replace(where, to_what);
    return res



main()
```

### 3.3. Создание скрипта для считывания данных справочных логов из текстового файла и преобразования их в CSV-формат с последующей записью в новый файл. Формирование отчета по выполнению задания и размещение его в портфолио, персональном репозитории. 

### 3.4. Реализовать программу шифрующую строку, задаваемую пользователем, с помощью алгоритма шифрования ROT13. Формирование отчета по выполнению задания и размещение его в портфолио, персональном репозитории.

```python
def main():
    print("Введиет слова которые хотите зашифровать:")
    sh = input()
    length = len(sh)
    for i in range(length):        
        print(rot(sh[i]))
    test()
def rot(arg):
    if(ord(arg) != 32 and ord(arg) < 110):
        t = ord(arg)
        t += 13
        sym = chr(t)  
    if(ord(arg) != 32 and ord(arg) >= 110):
        t = ord(arg) 
        t -= 13
        sym = chr(t)
    if(ord(arg) == 32):
        sym = arg
    return sym 
main()
```
