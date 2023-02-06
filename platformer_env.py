import pygame
import sys
import random
import time

class Platformer:
    def __init__(self):
         # Initialize self.game
        self.game = pygame
        self.game.init()
        # Set the window size
        self.window_size = (1000, 600)
        # Create the window
        self.screen = self.game.display.set_mode(self.window_size)
        # Set the title of the window
        self.game.display.set_caption("2D Platformer")
        # Set the dimensions of the player square
        self.player_size = 50
        # Set the initial position of the player square
        self.player_pos = [500, 500]
        # Set the dimensions of the goal
        self.goal_size = 50
        # Set the position of the goal
        self.goal_pos = [900, 500]
        # Set the speed of the player
        self.death_pos = 25
        self.player_speed = 3
        self.inf = 1500
        # Create a font for displaying text
        self.font = self.game.font.Font(None, 36)

    def reset(self):
        self.game.quit()
        self.__init__()
        return [self.player_pos[0]]

    def step(self, move):
            # Check for events
        for event in self.game.event.get():
            # If the event is to quit the game, exit the game loop
            if event.type == self.game.QUIT:
                self.game.quit()
                sys.exit()
        if move == 1:
            self.player_pos[0] += self.player_speed
        if move == 0: 
            self.player_pos[0] -= self.player_speed
        """
        # Check for key press events
        keys = self.game.key.get_pressed()

        # If the left arrow key is pressed, move the player to the left
        if keys[self.game.K_LEFT]:
            player_pos[0] -= player_speed
        # If the right arrow key is pressed, move the player to the right
        if keys[self.game.K_RIGHT]:
            player_pos[0] += player_speed
        """
        # Fill the screen with white
        self.screen.fill((255, 255, 255))

        # Draw the player square
        self.game.draw.rect(self.screen, (0, 0, 0), self.game.Rect(self.player_pos[0], self.player_pos[1], self.player_size, self.player_size))

        # Draw the goal
        self.game.draw.rect(self.screen, (0, 255, 0), self.game.Rect(self.goal_pos[0], self.goal_pos[1], self.goal_size, self.goal_size))

        terminated = False
        # Check if the player has reached the goal
        if self.player_pos[0] <= self.death_pos:
            text = self.font.render("Death!", True, (0, 0, 0))
            self.screen.blit(text, (150, 250))
            terminated = True
        elif self.player_pos[0] < self.goal_pos[0] + self.goal_size and self.player_pos[0] + self.player_size > self.goal_pos[0] and self.player_pos[1] < self.goal_pos[1] + self.goal_size and self.player_pos[1] + self.player_size > self.goal_pos[1]:
            # If the player has reached the goal, display a message
            text = self.font.render("You win!", True, (0, 0, 0))
            self.screen.blit(text, (150, 250))
            terminated = True

        # Update the display
        self.game.display.flip()
        print(10*(self.inf - (self.goal_pos[0] - self.player_pos[0])))
        return [self.player_pos[0]], 10*(self.inf - (self.goal_pos[0] - self.player_pos[0])), terminated
