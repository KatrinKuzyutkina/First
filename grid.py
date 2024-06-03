import pygame
import random
import copy

class Grid: # сетка
    
    def __init__(self, title, offset):
        self.title = title
        self.offset = offset
        self.__draw_grid()
        self.__add_nums_letters_to_grid()
        self.__sign_grid()

    def __draw_grid(self):
        for i in range(11):
            pygame.draw.line(screen, BLACK, (left_margin + self.offset * block_size, upper_margin + i * block_size), 
                             (left_margin + (10 + self.offset) * block_size, upper_margin + i * block_size), 1)
            pygame.draw.line(screen, BLACK, (left_margin + (i + self.offset) * block_size, upper_margin), 
                             (left_margin + (i + self.offset) * block_size, upper_margin + 10 * block_size), 1)

    def __add_nums_letters_to_grid(self):
        for i in range(10):
            num_ver = font.render(str(i + 1), True, BLACK)
            letters_hor = font.render(LETTERS[i], True, BLACK)
            num_ver_width = num_ver.get_width()
            num_ver_height = num_ver.get_height()
            letters_hor_width = letters_hor.get_width()

            screen.blit(num_ver, (left_margin - (block_size // 2 + num_ver_width // 2) + self.offset * block_size, 
                upper_margin + i * block_size + (block_size // 2 - num_ver_height // 2)))
            screen.blit(letters_hor, (left_margin + i * block_size + (block_size // 2 - 
                letters_hor_width // 2) + self.offset * block_size, upper_margin + 10 * block_size))

    def __sign_grid(self):       
        player = font.render(self.title, True, BLACK)
        sign_width = player.get_width()
        screen.blit(player, (left_margin + 5 * block_size - sign_width // 2 + self.offset * block_size, 
            upper_margin - block_size // 2 - font_size))
