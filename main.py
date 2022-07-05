from models import Game
import pygame
import sys
import random
from button import Button
from models.menu.credits import Credits
from models.menu.player_menu import PlayerMenu
from models.menu.player_menu_1 import PlayerMenu1
from models.menu.player_menu_2 import PlayerMenu2
from models.menu.dificult_menu import DificultMenu


class Main:
    """Clase menu"""

    def __init__(self):
        self.__game = Game()

        """Valores de pantalla"""
        self.playbutton = None
        pygame.init()
        self.width = 1280
        self.height = 720
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.screen_width = self.screen.get_rect().width
        self.screen_height = self.screen.get_rect().height
        # Pantalla
        pygame.display.set_caption("Game Menu")
        self.gray = (229, 232, 232)
        self.white = (255, 255, 255)
        # Musica
        pygame.mixer.music.load("PokemonStadium.wav")
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(0.0)
        # Juego
        self.activate = False
        self.activate_game = False
        self.activate_credits = False
        self.activate_player1 = False
        self.activate_player12 = False
        self.activate_player2 = False
        self.activate_dif = False
        self.buttons = Button(self)
        self.credit = Credits(self)
        self.playerMenu = PlayerMenu(self)
        self.playerMenu1 = PlayerMenu1(self)
        self.playerMenu2 = PlayerMenu2(self)
        self.dificultMenu = DificultMenu(self)
        # self.player = Player(self)
        self.clock = pygame.time.Clock()
        # Objetos que me pide
        self.press_button = None
        self.use_check_button = True
        self.use_check_button_player = False
        self.use_check_button_election = False
        self.use_check_button_election12 = False
        self.use_check_button_election2 = False
        self.use_check_button_dificult = False
        self.theres_two = False

    def check_button(self, mouse):

        """Comprobamos el clic"""
        if 540 <= mouse[0] <= 740 and 320 <= mouse[1] <= 370 and not self.activate_game:
            self.activate_game = True
            self.activate = True
            self.use_check_button = False
            self.use_check_button_player = True
        if 540 <= mouse[0] <= 740 and 380 <= mouse[1] <= 430 and not self.activate_game:
            self.activate_credits = True
            self.use_check_button = False
            self.use_check_button_player = True
        if 540 <= mouse[0] <= 740 and 440 <= mouse[1] <= 490:
            pygame.quit()
            sys.exit()

    def check_button_players(self, mouse):

        """Comprobamos el clic"""
        if 540 <= mouse[0] <= 740 and 310 <= mouse[1] <= 360:
            self.activate = False
            self.activate_player1 = True
            self.use_check_button_player = False
            self.use_check_button_election = True

        if 540 <= mouse[0] <= 740 and 440 <= mouse[1] <= 490:
            self.activate = False
            self.activate_player12 = True
            self.use_check_button_player = False
            self.use_check_button_election12 = True
            self.__game.set_multiplayer(True)

    def check_button_election(self, mouse):

        """Comprobamos el clic"""
        if 540 <= mouse[0] <= 740 and 320 <= mouse[1] <= 370:
            self.activate_player1 = False
            self.activate_dif = True
            self.use_check_button_election = False
            self.use_check_button_dificult = True
            self.__game.set_character1('fish')
        if 540 <= mouse[0] <= 740 and 380 <= mouse[1] <= 430:
            self.activate_player1 = False
            self.activate_dif = True
            self.use_check_button_election = False
            self.use_check_button_dificult = True
            self.__game.set_character1('robot')
        if 540 <= mouse[0] <= 740 and 440 <= mouse[1] <= 490:
            self.activate_player1 = False
            self.activate_dif = True
            self.use_check_button_election = False
            self.use_check_button_dificult = True
            self.__game.set_character1('sniper')

    def check_button_election2(self, mouse):

        """Comprobamos el clic"""
        if 540 <= mouse[0] <= 740 and 320 <= mouse[1] <= 370:
            self.activate_player2 = False
            self.activate_dif = True
            self.use_check_button_election2 = False
            self.use_check_button_dificult = True
            self.__game.set_character2('fish')
        if 540 <= mouse[0] <= 740 and 380 <= mouse[1] <= 430:
            self.activate_player2 = False
            self.activate_dif = True
            self.use_check_button_election2 = False
            self.use_check_button_dificult = True
            self.__game.set_character2('robot')
        if 540 <= mouse[0] <= 740 and 440 <= mouse[1] <= 490:
            self.activate_player2 = False
            self.activate_dif = True
            self.use_check_button_election2 = False
            self.use_check_button_dificult = True
            self.__game.set_character2('sniper')

    def check_button_election12(self, mouse):

        """Comprobamos el clic"""
        if 540 <= mouse[0] <= 740 and 320 <= mouse[1] <= 370:
            self.activate_player12 = False
            self.activate_player2 = True
            self.use_check_button_election12 = False
            self.use_check_button_election2 = True
            self.__game.set_character1('fish')
        if 540 <= mouse[0] <= 740 and 380 <= mouse[1] <= 430:
            self.activate_player12 = False
            self.activate_player2 = True
            self.use_check_button_election12 = False
            self.use_check_button_election2 = True
            self.__game.set_character1('robot')
        if 540 <= mouse[0] <= 740 and 440 <= mouse[1] <= 490:
            self.activate_player12 = False
            self.activate_player2 = True
            self.use_check_button_election12 = False
            self.use_check_button_election2 = True
            self.__game.set_character1('sniper')

    def check_button_dificult(self, mouse):

        """Comprobamos el clic"""
        if 540 <= mouse[0] <= 740 and 310 <= mouse[1] <= 360:
            self.activate_player12 = False
            self.activate_player2 = False
            self.activate_player1 = False
            self.__game.set_difficulty('normal')
            self.__game.init_game()

        if 540 <= mouse[0] <= 740 and 440 <= mouse[1] <= 490:
            self.activate_player12 = False
            self.activate_player2 = False
            self.activate_player1 = False
            self.__game.set_difficulty('hard')
            self.__game.init_game()

    def running_game(self):
        """Corre el juego más lectura de eventos"""
        coord_list = []
        for cont in range(200):
            cord_x = random.randint(0, 1280)
            cord_y = random.randint(0, 720)
            coord_list.append([cord_x, cord_y])

        while True:
            for ev in pygame.event.get():
                if ev.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                mouse = pygame.mouse.get_pos()
                if ev.type == pygame.MOUSEBUTTONDOWN and self.use_check_button == True and self.use_check_button_player == False:
                    self.check_button(mouse)
                elif ev.type == pygame.MOUSEBUTTONDOWN and self.use_check_button == False and self.use_check_button_player == True:
                    self.check_button_players(mouse)
                elif ev.type == pygame.MOUSEBUTTONDOWN and self.use_check_button == False and self.use_check_button_player == False and self.use_check_button_election == True:
                    self.check_button_election(mouse)
                elif ev.type == pygame.MOUSEBUTTONDOWN and self.use_check_button_election12 == True:
                    self.check_button_election12(mouse)
                elif ev.type == pygame.MOUSEBUTTONDOWN and self.use_check_button_election2 == True:
                    self.check_button_election2(mouse)
                elif ev.type == pygame.MOUSEBUTTONDOWN and self.use_check_button_dificult == True:
                    self.check_button_dificult(mouse)

            self.screen.fill(self.gray)

            if not self.activate_game:
                self.buttons.print_button()
                for pos_list in coord_list:
                    pygame.draw.circle(self.screen, self.white, pos_list, 3)
                    pos_list[1] += 1
                    if pos_list[1] > 720:
                        pos_list[1] = 0
            # Activamos el juego
            if self.activate_game:
                if self.activate:
                    self.playerMenu.print_button_mode()
                    for pos_list in coord_list:
                        pygame.draw.circle(self.screen, self.white, pos_list, 3)
                        pos_list[1] += 1
                        if pos_list[1] > 720:
                            pos_list[1] = 0
                if self.activate_credits:
                    self.credit.print_button_credits()
                    for pos_list in coord_list:
                        pygame.draw.circle(self.screen, self.white, pos_list, 3)
                        pos_list[1] += 1
                        if pos_list[1] > 720:
                            pos_list[1] = 0
                if self.activate_player1:
                    self.playerMenu1.print_button()
                    for pos_list in coord_list:
                        pygame.draw.circle(self.screen, self.white, pos_list, 3)
                        pos_list[1] += 1
                        if pos_list[1] > 720:
                            pos_list[1] = 0
                if self.activate_player12:
                    self.playerMenu1.print_button()
                    for pos_list in coord_list:
                        pygame.draw.circle(self.screen, self.white, pos_list, 3)
                        pos_list[1] += 1
                        if pos_list[1] > 720:
                            pos_list[1] = 0
                if self.activate_player2:
                    self.playerMenu2.print_button()
                    for pos_list in coord_list:
                        pygame.draw.circle(self.screen, self.white, pos_list, 3)
                        pos_list[1] += 1
                        if pos_list[1] > 720:
                            pos_list[1] = 0
                if self.activate_dif:
                    self.dificultMenu.print_button_mode()
                    for pos_list in coord_list:
                        pygame.draw.circle(self.screen, self.white, pos_list, 3)
                        pos_list[1] += 1
                        if pos_list[1] > 720:
                            pos_list[1] = 0

            pygame.display.flip()
            self.clock.tick(60)


if __name__ == "__main__":
    a = Main()
    a.running_game()