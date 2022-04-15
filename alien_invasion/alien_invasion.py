import sys
import pygame
from settings import Settings
from cook import Cook
from bullet import Bullet
from chicken import Chicken

class AlienInvasion:

    def __init__(self):
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

        self.cook = Cook(self)
        self.bullets = pygame.sprite.Group()
        self.chickens = pygame.sprite.Group()


    def _create_fleet(self):
        chicken = Chicken(self)
        chicken_width = chicken.rect.width
        available_space_x = self.settings.screen_width - (2 * chicken_width)
        number_chickens_x = available_space_x // (2 * chicken_width)

        for chicken_number in range(number_chickens_x):
            chicken = Chicken(self)
            chicken.x = chicken_width + 2 * chicken_width * chicken_number
            chicken.rect.x = chicken.x
            self.chickens.add(chicken)

    def run_game(self):
        while True:
            self._check_events()
            self.cook.update()
            self.bullets.update()
            self._update_screen()

    def _check_events(self):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

                elif event.type == pygame.KEYDOWN:
                    self._check_keydown_events(event)
                elif event.type == pygame.KEYUP:
                    self._check_keyup_events(event)


    def _check_keydown_events(self, event):
            if event.key == pygame.K_RIGHT:
                self.cook.moving_right = True
            elif event.key == pygame.K_LEFT:
                self.cook.moving_left = True
            elif event.key == pygame.K_z:
                sys.exit()
            elif event.key == pygame.K_SPACE:
                self._fire_bullet()

    def _check_keyup_events(self, event):
            if event.key == pygame.K_RIGHT:
                self.cook.moving_right = False
            elif event.key == pygame.K_LEFT:
                self.cook.moving_left = False

    def _fire_bullet(self):
        new_bullet = Bullet(self)
        self.bullets.add(new_bullet)

    def _update_screen(self):
            self.screen.fill(self.settings.bg_color)
            self.cook.blitme()
            for bullet in self.bullets.sprites():
                bullet.draw_bullet()
            self.chickens.draw(self.screen)

            pygame.display.flip()


if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()