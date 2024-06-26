![CI/CD GitHub Actions](https://github.com/KatrinKuzyutkina/First/actions/workflows/main.yml/badge.svg)
[![Coverage Status](https://coveralls.io/repos/KatrinKuzyutkina/First/badge.svg?branch=main)](https://coveralls.io/github/KatrinKuzyutkina/gtest?branch=main)
[![Quality Gate](https://sonarcloud.io/api/project_badges/measure?project=KatrinKuzyutkina_First&metric=alert_status)](https://sonarcloud.io/dashboard?id=KatrinKuzyutkina_First)
[![Bugs](https://sonarcloud.io/api/project_badges/measure?project=KatrinKuzyutkina_First&metric=bugs)](https://sonarcloud.io/summary/new_code?id=KatrinKuzyutkina_First)
[![Code smells](https://sonarcloud.io/api/project_badges/measure?project=KatrinKuzyutkina_First&metric=code_smells)](https://sonarcloud.io/dashboard?id=KatrinKuzyutkina_First)

# Игра "Битва Кораблей"
**Битва Кораблей** - это захватывающая боевая игра, в которой пользователь соревнуется против компьютера, стреляя по кораблям на игровом поле. 
Игровое поле представляет собой сетку 10x10 клеток, где каждая клетка имеет свои координаты.
Каждый игрок имеет несколько кораблей различного размера, которые располагаются на игровом поле.
*Игра реализована на языке Python с помощью библитеки Pygame.*

**Пользователю необходимо потопить все корабли противника, попадая по их координатам.**
## Правила игры
- Игроки по очереди делают ходы, указывая координаты на игровом поле для стрельбы.
- Если игрок попадает по кораблю противника, то получает дополнительный ход.
- У игрока есть бомба, которая активируется после 5 попаданий в координату корабля противника. Бомба поражает сетку 3x3.
- Когда все клетки одного из кораблей противника подбиты, корабль считается потопленным.
- Побеждает тот игрок, который первым потопит все корабли противника.
## Реализация
1. Расстановка кораблей на поле:
   - Пользователь может самостоятельно размещают корабли на поле или с помощью режима "Авто" приложение случайным образом расставлит корабли.
   - Проверяется, не пересекаются ли корабли, не выходят ли за пределы поля, расположены ли все корабли.
   - Если хотя бы одно условие неверно, игрок получает сообщение с содержанием ошибки.
2. Ход игрока:
   - Игрок делает ход, указывая координаты выстрела на поле противника.
   - Проверяется, попал ли игрок в корабль противника.
   - Если игрок попал, то корабль противника повреждается и игрок получает дополнительный ход.
   - Если игрок не попал, то ход переходит к противнику.
   - Под полем противника игрок может увидеть свой последний ход.
3. Ход компьютера:
   - Компьютер случайным образом выбирает координаты для выстрела по полю игрока.
   - Если компьютер попадает в координату корабля противника, следующий ход он делает вправо, влево, вверх или вниз от последней клетки, в которую попал.
   - Если компьютер попал, то корабль противника повреждается и компьютер получает дополнительный ход.
   - Если компьютер не попал, то ход переходит к игроку.
   - Под полем противника компьютер может увидеть свой последний ход.
4. Проверка окончания игры:
   - Проверяется, остались ли еще живые корабли на поле.
   - Происходит перебор всех клеток поля и проверки состояния каждой клетки.
   - Определение окончания игры при потоплении всех кораблей одного из игроков.

## Диаграммы
* [**Функциональные модели**](docs/functions.md)
* [**Структурные модели**](docs/struct.md)
* [**Поведенческие модели**](docs/behavior.md)
* [**Перечень тестов**](docs/descriptions.md)

***
*Автор: Кузюткина Екатерина*

