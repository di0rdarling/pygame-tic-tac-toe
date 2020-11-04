import sys
import pygame
from pynput import mouse
from grid import Grid


def main():
    pygame.init()

    display_size = width, height = 1000, 600
    white = 255, 255, 255
    screen = pygame.display.set_mode(display_size)

    # Set the x,y coordinates for each grid.
    # Row 1
    grid_one = Grid(0, 0)
    grid_two = Grid(100, 0)
    grid_three = Grid(200, 0)

    # Row 2
    grid_four = Grid(0, 100)
    grid_five = Grid(100, 100)
    grid_six = Grid(200, 100)

    # Row 3
    grid_seven = Grid(0, 200)
    grid_eight = Grid(100, 200)
    grid_nine = Grid(200, 200)

    grids = [grid_one, grid_two, grid_three, grid_four,
             grid_five, grid_six, grid_seven, grid_eight, grid_nine]

    # Draw each grid at the specific x,y coordinate to make a board.
    for grid in grids:
        pygame.draw.rect(screen, white, (grid.x,
                                         grid.y, grid.width, grid.height), grid.thickness)

    def handle_click(position):
        pos_x = position[0]
        pos_y = position[1]
        for grid in grids:
            if (pos_x >= grid.x and pos_x <= grid.x+100) and (pos_y >= grid.y and pos_y <= grid.y+100):
                # Draw a circle in the middle of the grid.
                pygame.draw.circle(screen, white, (grid.x+50,
                                                   grid.y+50), 30, 4)
                grid.play = 'o'

    def check_winner():
        if grid_one.play is not None:
            if(grid_one.play == grid_two.play) and (grid_one.play == grid_three.play):
                print('Winner: across top --->')
            elif grid_one.play is not None and (grid_one.play == grid_four.play) and (grid_one.play == grid_seven.play):
                print('Winner: down left --->')
            elif grid_one.play is not None and (grid_one.play == grid_five.play) and (grid_one.play == grid_nine.play):
                print('Winner: diagonally topLeft-bottomRight--->')
        elif grid_four.play is not None and (grid_four.play == grid_five.play) and (grid_four.play == grid_six.play):
            print('Winner: across middle --->')
        elif grid_seven.play is not None and (grid_seven.play == grid_eight.play) and (grid_seven.play == grid_nine.play):
            print('Winner: across bottom --->')
        elif grid_two.play is not None and (grid_two.play == grid_five.play) and (grid_two.play == grid_eight.play):
            print('Winner: down middle --->')
        elif grid_three.play is not None and (grid_three.play == grid_five.play) and (grid_three.play == grid_seven.play):
            print('Winner: diagonally topRight-bottomLeft--->')
        elif grid_three.play is not None and (grid_three.play == grid_six.play) and (grid_three.play == grid_nine.play):
            print('Winner: down right --->')

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                handle_click(pos)
                check_winner()

        pygame.display.flip()


main()
