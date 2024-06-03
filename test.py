import unittest
from copy import copy
import random
from main import *

class TestAutoShips(unittest.TestCase):

    def setUp(self):
        # Инициализация генератора случайных чисел для повторяемости тестов
        random.seed(42)
        # Создаем экземпляр класса AutoShips для тестирования
        self.auto_ships = AutoShips(0)

    def test_create_start_block(self):
        # Создаем набор доступных блоков
        available_blocks = {(1, 1), (2, 2), (3, 3)}
        # Вызываем метод для создания начального блока корабля
        x, y, orientation, direction = self.auto_ships._AutoShips__create_start_block(available_blocks)
        # Проверяем, что начальный блок находится в доступных блоках
        self.assertIn((x, y), available_blocks)
        # Проверяем, что ориентация является допустимой (0 - горизонтально, 1 - вертикально)
        self.assertIn(orientation, [0, 1])
        # Проверяем, что направление является допустимым (-1 или 1)
        self.assertIn(direction, [-1, 1])

    def test_create_ship(self):
        # Создаем набор доступных блоков (вся сетка 10x10)
        available_blocks = {(x, y) for x in range(1, 11) for y in range(1, 11)}
        # Вызываем метод для создания корабля длиной 3 блока
        ship = self.auto_ships._AutoShips__create_ship(3, available_blocks)
        # Проверяем, что длина корабля равна 3
        self.assertEqual(len(ship), 3)
        # Проверяем, что каждый блок корабля находится в доступных блоках
        for block in ship:
            self.assertIn(block, available_blocks)

    def test_is_ship_valid(self):
        # Создаем валидный корабль (все блоки в пределах сетки)
        valid_ship = [(1, 1), (1, 2), (1, 3)]
        # Создаем невалидный корабль (один блок за пределами сетки)
        invalid_ship = [(1, 1), (1, 2), (11, 11)]

        # Создаем набор доступных блоков (вся сетка 10x10)
        self.auto_ships.available_blocks = {(x, y) for x in range(1, 11) for y in range(1, 11)}

        # Проверяем, что валидный корабль проходит проверку
        self.assertTrue(self.auto_ships._AutoShips__is_ship_valid(valid_ship))
        # Проверяем, что невалидный корабль не проходит проверку
        self.assertFalse(self.auto_ships._AutoShips__is_ship_valid(invalid_ship))

    def test_populate_grid(self):
        # Создаем набор доступных блоков (вся сетка 10x10)
        self.auto_ships.available_blocks = {(x, y) for x in range(1, 11) for y in range(1, 11)}
        # Вызываем метод для расстановки всех кораблей на сетке
        ships = self.auto_ships._AutoShips__populate_grid()
        # Создаем множество для отслеживания всех занятых блоков
        all_blocks = set()
        for ship in ships:
            for block in ship:
                # Проверяем, что текущий блок еще не занят другим кораблем
                self.assertNotIn(block, all_blocks)
                # Добавляем блок в множество занятых блоков
                all_blocks.add(block)
        # Проверяем, что количество кораблей равно 10
        self.assertEqual(len(ships), 10)

# Подготовка данных
class TestComputerHitsTwice(unittest.TestCase):
    def setUp(self):
        global last_hits_list, around_last_computer_hit_set, computer_available_to_fire_set
        around_last_computer_hit_set = set()

    def test_computer_hits_twice(self):
        last_hits_list = [(17, 5), (18, 5)]

        # Ожидаемое множество соседей после двух попаданий по горизонтали
        expected_set = {(16, 5), (19, 5)}
        result_set = computer_hits_twice(last_hits_list)
        self.assertEqual(result_set, expected_set)

        # Обновление глобального множества вокруг последнего попадания
        around_last_computer_hit_set.update(result_set)
        expected_around_last_computer_hit_set = {(16, 5), (19, 5)}
        self.assertEqual(around_last_computer_hit_set, expected_around_last_computer_hit_set)

    def test_computer_hits_twice_vertical(self):
        # Изменение попаданий на вертикальные
        last_hits_list = [(17, 5), (17, 6)]
        
        # Ожидаемое множество соседей после двух попаданий по вертикали
        expected_set = {(17, 4), (17, 7)}
        result_set = computer_hits_twice(last_hits_list)
        self.assertEqual(result_set, expected_set)

        # Обновление глобального множества вокруг последнего попадания
        around_last_computer_hit_set.update(result_set)
        expected_around_last_computer_hit_set = {(17, 4), (17, 7)}
        self.assertEqual(around_last_computer_hit_set, expected_around_last_computer_hit_set)

# Подготовка данных
class TestCheckHit(unittest.TestCase):
    def test_single_shoot_miss(self):
        fired_block = (2, 2)
        bomb_is_ready = False
        computer_ships_working = [[(1,1), (1,2), (1,3)], [(6, 6), (5, 6)]]
        computer_ships = computer_ships_working
        computer_ships_set = set()
        for ship in computer_ships_working:
            for block in ship:
                computer_ships_set.add(block)

        self.assertEqual(check_hit(fired_block, bomb_is_ready, computer_ships_working, computer_ships, computer_ships_set), 0)
    def test_single_shoot_hit(self):
        fired_block = (1, 2)
        bomb_is_ready = False
        computer_ships_working = [[(1,1), (1,2), (1,3)], [(6, 6), (5, 6)]]
        computer_ships = computer_ships_working
        computer_ships_set = set()
        for ship in computer_ships_working:
            for block in ship:
                computer_ships_set.add(block)

        self.assertEqual(check_hit(fired_block, bomb_is_ready, computer_ships_working, computer_ships, computer_ships_set), 1)

    def test_bomb_shoot_with_kill_and_hit(self):
        fired_block = (3, 8)
        bomb_is_ready = True
        computer_ships_working = [[(2,7), (3,7), (4,7)], [(2,9),(1,9)]]
        computer_ships = computer_ships_working
        computer_ships_set = set()
        for ship in computer_ships_working:
            for block in ship:
                computer_ships_set.add(block)

        self.assertEqual(check_hit(fired_block, bomb_is_ready, computer_ships_working, computer_ships, computer_ships_set), 4)

""" расстановка
тест умной стрельбы
тест супер атаки (бомбы)"""
if __name__ == '__main__':
    # Запускаем тесты
    unittest.main()
