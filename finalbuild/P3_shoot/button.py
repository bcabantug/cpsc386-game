import pygame
from global_inst import BLACK


# create buttons
def Button(windows, text, color, x, y, w, h):
    small_font = pygame.font.SysFont("comicsansms", 15, False, False)
    button_text = small_font.render(text, False, BLACK)
    rect = button_text.get_rect()
    rect.center = (x + w / 2, y + h / 2)
    pygame.draw.rect(windows, color, (x, y, w, h))
    windows.blit(button_text, rect)



