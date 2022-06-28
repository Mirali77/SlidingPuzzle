import init
from init import *

# Цикл игры
running = True
while running:
    # держим цикл на правильной скорости
    clock.tick(FPS)

    # Название окна
    pygame.display.set_caption('Sliding Puzzle')

    # Ввод процесса (события)
    for event in pygame.event.get():
        # проверить закрытие окна
        if event.type == pygame.QUIT:
            running = False
        if game:
            if event.type == pygame.MOUSEBUTTONDOWN and not init.drag_flag:
                tile_table.tile_clicked(event)
            if event.type == pygame.MOUSEBUTTONUP:
                tile_table.tile_unclicked()
        else:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if yes_message.rect.collidepoint(event.pos):
                    game = True
                    tile_table.repair()
                elif no_message.rect.collidepoint(event.pos):
                    running = False
    # Обновление
    if init.drag_flag:
        tile_table.tile_dragging()
    if game:
        game = not tile_table.check()
        if not game:
            tile_table.clear()
    all_sprites.update()
    screen.fill(BLUE)
    all_sprites.draw(screen)
    if not game:
        gio_message.draw()
        pa_message.draw()
        yes_message.draw()
        no_message.draw()

    # Визуализация (сборка)
    pygame.display.flip()

pygame.quit()
