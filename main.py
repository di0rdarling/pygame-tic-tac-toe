import sys
import pygame
import random
from grid import Grid


def main():
    pygame.init()
    pygame.font.init()
    myfont = pygame.font.SysFont('Comic Sans MS', 30)

    display_size = width, height = 1000, 600
    white = 255, 255, 255
    screen = pygame.display.set_mode(display_size)

    # Set the x,y coordinates for each grid.
    board_x = 350
    board_y = 150
    row_top_x = board_x
    row_middle_x = board_x+100
    row_bottom_x = board_x+200
    column_left_y = board_y
    column_middle_y = board_y+100
    column_right_y = board_y+200

    # Row 1
    grid_one = Grid(row_top_x, column_left_y)
    grid_two = Grid(row_middle_x, column_left_y)
    grid_three = Grid(row_bottom_x, column_left_y)

    # Row 2
    grid_four = Grid(row_top_x, column_middle_y)
    grid_five = Grid(row_middle_x, column_middle_y)
    grid_six = Grid(row_bottom_x, column_middle_y)

    # Row 3
    grid_seven = Grid(row_top_x, column_right_y)
    grid_eight = Grid(row_middle_x, column_right_y)
    grid_nine = Grid(row_bottom_x, column_right_y)

    board = [grid_one, grid_two, grid_three, grid_four,
             grid_five, grid_six, grid_seven, grid_eight, grid_nine]

    # Draw each grid at the specific x,y coordinate to make a board.
    for grid in board:
        pygame.draw.rect(screen, white, (grid.x,
                                         grid.y, grid.width, grid.height), grid.thickness)

    def handle_player_turn(mouse_position):
        success = False
        mouse_pos_x = mouse_position[0]
        mouse_pos_y = mouse_position[1]
        for grid in board:
            if (mouse_pos_x >= grid.x and mouse_pos_x <= grid.x+100) and (mouse_pos_y >= grid.y and mouse_pos_y <= grid.y+100) and grid.play is None:
                # Draw a circle in the middle of the grid.
                pygame.draw.circle(screen, white, (grid.x+50,
                                                   grid.y+50), 30, 4)
                grid.play = 'player'
                success = True

        return success

    def handle_computer_turn():
        success = False
        attempts = 5
        while not success and attempts >= 0:
            index = random.randint(0, len(board)-1)
            selected_grid = board[index]
            if selected_grid.play is None:
                # Draw a cross in the middle of the grid.
                pygame.draw.line(screen, white,
                                 (selected_grid.x+10, selected_grid.y+90), (selected_grid.x+90, selected_grid.y+10), 4)
                pygame.draw.line(screen, white,
                                 (selected_grid.x+10, selected_grid.y+10), (selected_grid.x+90, selected_grid.y+90), 4)
                selected_grid.play = 'computer'
                success = True
            else:
                attempts -= 1

        return success

    def check_winner():
        # Check to see if valid series of plays have been played on the board.
        winner = ''
        if board[0].play is not None:
            if(board[0].play == board[1].play) and (board[0].play == board[2].play):
                winner = grid_one.play
            elif (board[0].play == board[3].play) and (board[0].play == board[6].play):
                winner = grid_one.play
            elif (board[0].play == board[4].play) and (board[0].play == board[8].play):
                winner = grid_one.play
        elif board[3].play is not None and (board[3].play == board[4].play) and (board[3].play == board[5].play):
            winner = grid_four.play
        elif board[6].play is not None and (board[6].play == board[7].play) and (board[6].play == board[8].play):
            winner = grid_seven.play
        elif board[1].play is not None and (board[1].play == board[4].play) and (board[1].play == board[7].play):
            winner = grid_two.play
        elif board[2].play is not None and (board[2].play == board[4].play) and (board[2].play == board[6].play):
            winner = grid_three.play
        elif board[2].play is not None and (board[2].play == board[5].play) and (board[2].play == board[8].play):
            winner = grid_three.play

        return winner

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                player_success = handle_player_turn(pos)
                if player_success:
                    computer_success = handle_computer_turn()
                    if computer_success:
                        check_winner()

        winner = check_winner()
        if winner is not '':
            textsurface = myfont.render(
                winner + ' wins!', False, (255, 255, 255))
            screen.blit(textsurface, (420, 70))

        pygame.display.flip()


main()
