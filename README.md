# Simple encryptor

Короче, это очень простой кодировщик файлов. ~Я тут не буду описывать как он работает~ Ещё как буду. Скажу лишь всё завязано на простом `random.shuffle()`.

Исходники написаны на Python 3.10 (в релизе есть скрипт для 3.9 и exe-файл)

## Как пользоваться
Мне было лень создавать какой либо графический интерфейс, так что всё оформлено в консоли. Но вы не дауны (надеюсь) так что разберётесь.

### 1. Выберите режим
Введите `e` чтобы закодировать файл или `d` чтобы декодировать (ну тут думаю очевидно).
### 2. Введите имя файла
Введите имя того файла который хотите закодировать/декодировать. Если файл и скрипт лежат в одной директории, просто введите его название с расширением. Если нет, то вводите абсолютный путь.
### 3. Введите ключ
Ключ - это ключ к файлу. АУФ!. Тоесть это число, которое будет использоваться при кодировке файла и которое нужно использовать при декодировке, чтобы получить исходный файл. Если ключи при кодировке/декодировке не будут совпадать, то вы получите крокозябры вместо файла.

![image](https://user-images.githubusercontent.com/102759337/187180505-5b1a8d03-a60f-4835-b388-6a286d50a0c0.png)
> Тут плохой пример, кавычки и пробелы лучше не вводить!
### 4. Терпение - мать ~мертва~ учения!
Теперь просто ждём, пока программа делает своё дело.

![image](https://user-images.githubusercontent.com/102759337/187182471-b9745db8-616e-4ce2-b5e7-b57db2e84715.png)
### 5. Принимаем результат
После вводим имя файла, в который сохранятся зашифрованные/расшифрованные данные.

![image](https://user-images.githubusercontent.com/102759337/187183020-1e8387c8-f5ca-4810-8b98-ed7bbe87fead.png)

#### В обратном направлении процедура аналогичная

## Нюансы
* Если прога вылетает когда вы вводите относительный путь, то вводите абсолютный путь. Тоесть не `prono.dick`, а `C:\Users\Butthead\Desktop\homework\prono.dick`.
* Файлы не должны быть названы кириллицей, арабской вязью, китайскими иероглифами и прочими экстравагантными символами. Тоесть, файлы должны быть с названием на латинице.
* То же самое касается пробелов и консолевских символов `"`.
* Если прога сохранила файл, а его в директории нет, то опять же вводите абсолютный путь (обращая внимание на 2-3 пункт).
* Не пихайте скрипту слишком большие файлы. Будет утечка памяти и оперативка тупо закончится. Это происходит уже на 100-150 MB (на ноутбуке в 8 GB).
* В поле для ввода ключа вводите **число** (можно отрицательное, но не длиной до Казахстана).

## Как работает

Я не буду прям в подробностях описывать как это работает и не буду придерживаться научного стиля.

1. Файл на входе преобразуется в набор значений от 0-255 (просто в байты).
2. На основе введённого ключа генерируется таблица кодирования.
Вкратце, генерируется список значений от 0 до 255, с помощью `random.shuffle()` по заранее указанному ключу в `random.seed()` список перемешивается и представляет собой что-то наподобие `[65, 25, 177, 0...67, 13, 194]`.

3. На основе этой таблицы исходный набор байтов преобразуется в зашифрованный.
Просто выбирается значение из таблицы с индексом исходного байта и это значение и есть закодированный байт.

`0 -> 65,
1 -> 25,
...
254 -> 13,
255 -> 194`

4. Новый набор байтов сохраняется в файл.

#### Декодирование происходит аналогично, только таблица строится наоборот.
## Контактная информация
Если обнаружили баги, ошибки, вылеты или персональное желание послать меня нах, то пишите сюда:
* habalyn228@outlook.com
* itsmyeighthacc@gmail.com
* [VK](https://vk.com/habalyn228)
> Спам - бан!
