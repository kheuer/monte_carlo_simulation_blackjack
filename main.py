import numpy as np
import matplotlib.pyplot as plt

full_deck = 4 * [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, None]

class Game:
    def __init__(self, player_function):
        self.deck = full_deck[:]
        
        self.player_function = player_function
        
        self.player_stands = False
        self.dealer_stands = False
        
        self.game_is_over = False
        
        # Give the Dealer 2 cards to start
        
        
        self.dealer_points = self.add_card(0, self.deck.pop(np.random.randint(len(self.deck))))
        self.dealer_upcard = self.dealer_points
        self.dealer_points = self.add_card(self.dealer_points, self.deck.pop(np.random.randint(len(self.deck))))
        
        # Give the Player 2 cards to start
        self.player_points = self.add_card(0, self.deck.pop(np.random.randint(len(self.deck))))
        self.player_points = self.add_card(self.player_points, self.deck.pop(np.random.randint(len(self.deck))))
        
        
    def play_round(self):
        if not self.player_stands and self.player_function(self.player_points, self.dealer_upcard):
            self.player_points = self.add_card(self.player_points, self.deck.pop(np.random.randint(len(self.deck))))
            
            if self.player_points == 21:         # the Player has won the game
                self.game_is_over = True
                return
            elif self.player_points > 21:        # the Player is Bust
                self.player_stands = True
            
        else:
            self.player_stands = True
        
        if not self.dealer_stands and self.dealer_points <= 17:         # the Dealer will only stand if his cards add up to 18 or more
            card = self.deck.pop(np.random.randint(len(self.deck)))
            self.dealer_points = self.add_card(self.dealer_points, card)
            
            if self.dealer_points == 21:        # the Dealer has won the game
                self.game_is_over = True
                return
            elif self.dealer_points > 21:       # The Dealer is Bust
                self.dealer_stands = True
        else:
            self.dealer_stands = True
            
        if self.dealer_stands and self.player_stands :
            self.game_is_over = True
            return
    
    
    def get_winner(self):
        # returns True is Player won and False if Dealer won, None if the round is a draw
        
        if self.player_points > 21:                         # player lost because cards are too high
            return False
        elif self.dealer_points > 21:                       # dealer lost because cards are too high
            return True
        elif self.player_points > self.dealer_points:       # the player wins if he has more points
            return True
        elif self.player_points < self.dealer_points:       # the player wins if he has more points
            return False
        else:                                               # the round is a draw
            return None
        
    
    def add_card(self, current_points, card):
        if card is None and current_points + 11 <= 21:      # this is an ace which can be used for 11 points
            return current_points + 11
        elif card is None:                            # this is an ace which would put the hands value above 21
            return current_points + 1
        else:                                               # this is a regular card
            return current_points + card
            

def run_simulation(player_function, n_rounds):
    n_wins = 0
    n_losses = 0

    for i in range(n_rounds):
        game = Game(player_function)
        while not game.game_is_over:
            game.play_round() 
        winner = game.get_winner()
        if winner is None:          # Game is a draw
            pass
        elif winner:               # Player won
            n_wins += 1
        else:                       # Dealer Won
            n_losses += 1
            
    n_draws = n_rounds - n_wins - n_losses
    
    cumulative_reward = n_wins - n_losses
    expected_reward = cumulative_reward / n_rounds
    variance = (n_wins * ((1 - expected_reward) ** 2) + \
                         n_losses * ((-1 - expected_reward) ** 2) + \
                         n_draws * ((0 - expected_reward) ** 2) \
                             ) / n_rounds
        
    return expected_reward, variance ** 0.5


always_hit = lambda player_points, dealer_upcard: True
never_hit = lambda player_points, dealer_upcard: False
random_policy = lambda player_points, dealer_upcard: np.random.choice([True, False])
draw_up_to_15 = lambda player_points, dealer_upcard: True if player_points <= 14 else False
draw_up_to_16 = lambda player_points, dealer_upcard: True if player_points <= 15 else False
draw_up_to_17 = lambda player_points, dealer_upcard: True if player_points <= 16 else False
draw_up_to_18 = lambda player_points, dealer_upcard: True if player_points <= 17 else False

def conventional_strategy(player_points, dealer_upcard):
    if player_points >= 17:
        return False
    elif player_points <= 11:
        return True
    elif dealer_upcard >= 7:
        return True
    else:
        return False

policies = {
    "Conventional Strategy": conventional_strategy,
    "Random Policy": random_policy,
    "Draw until Player has 15 points": draw_up_to_15,
    "Draw until Player has 16 points": draw_up_to_16,
    "Draw until Player has 17 points": draw_up_to_17,
    "Draw until Player has 18 points": draw_up_to_18,
    "Always Fold": never_hit,
    "Always take a hit": always_hit
    }


# Compare different strategies against each other
n_observations = 1_000_000
for desc, function in policies.items():
    expected_value, standard_deviation = run_simulation(function, n_observations)
    plt.scatter(standard_deviation, expected_value, label=desc)
    print(standard_deviation, expected_value, desc)
plt.xlabel("Standard Deviation")
plt.ylabel("Expected Value")
plt.legend()
plt.show()


# show the behaviour of Return/SD with different sample sizes
colors = plt.cm.get_cmap("tab10")
for i in range(10):
    for n_rounds in 10**np.arange(1, 7):
        expected_value, standard_deviation = run_simulation(conventional_strategy, n_rounds)
 
        if not i:
            plt.scatter(standard_deviation, expected_value, label=f"n={n_rounds}", color=colors(str(n_rounds).count("0")))
        else:
            plt.scatter(standard_deviation, expected_value, color=colors(str(n_rounds).count("0")))
plt.xlabel("Standard Deviation")
plt.ylabel("Expected Value")
plt.title("Conventional Policy")
plt.legend()
