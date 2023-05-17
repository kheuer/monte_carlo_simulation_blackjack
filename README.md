# Monte Carlo Method for Blackjack Simulation

This code demonstrates the application of the Monte Carlo method to simulate and analyze the game of Blackjack. The Monte Carlo method is a statistical technique that uses random sampling to estimate the behavior of complex systems or processes. In this case, the method is used to simulate different Blackjack strategies and evaluate their expected value and standard deviation of returns.

## Blackjack Simulation

The Game class represents a single round of Blackjack. It initializes a deck of cards and deals two cards each to the dealer and the player. The play_round method allows the player to make decisions based on a given strategy. The round continues until both the player and the dealer stand. The get_winner method determines the outcome of the round.

The run_simulation function runs multiple rounds of Blackjack using a specified player strategy and returns the expected reward and standard deviation. It keeps track of the number of wins, losses, and draws to calculate the statistics.
The code provides several predefined player strategies:

    always_hit: Always take a hit.
    never_hit: Never take a hit.
    random_policy: Make a random decision (hit or stand).
    draw_up_to_15: Draw until the player has 15 points.
    draw_up_to_16: Draw until the player has 16 points.
    draw_up_to_17: Draw until the player has 17 points.
    draw_up_to_18: Draw until the player has 18 points.
    conventional_strategy: A conventional Blackjack strategy that considers the player's points and the dealer's up card.

These strategies can be passed to the run_simulation function to evaluate their performance.
The dealer simulated here will take more cards until his cards add up to 17 or more. The player and dealers decide to take a hit or stand sequentially, if either party decides to stand they will no longer have the opportunity to take more cards. If either parties cards add up to 21 exactly they win the round immediately and if they add up to above 21 they lose the round immediately. The player goes first in each round. There is no known strategy to beat the dealer consistently under these rules (the house always wins).

## Expected Value and Standard Deviation

The expected value used in the analysis below describes the monetary return of a 1€ bet placed without ever splitting or doubling down. This value is negative because the dealer will win more often than the player as a result of the game rules. <br>
The standard deviation measures the dispersion of actual observations, the player winning is measured as a 1, the dealer winning as -1 and a draw is measured as 0. 

## Strategy Comparison

The code includes a comparison of different player strategies against each other. It runs simulations with a fixed number of observations and plots the standard deviation against the expected value for each strategy. The scatter plot shown below visualizes the performance of different strategies with respect to expected value and standard deviation after 1 Million Games.
<br>
![Image](https://github.com/kheuer/monte_carlo_simulation_blackjack/blob/main/different_policies_behaviour.png)
<br>
We can observe that the strategy to always take another card and the random policy are the only two clear outliers, their expected value is significantly lower as these strategies result in the player loosing significantly more often than winning. Further, the strategy to always take a hit has the lowest standard deviation because it looses most of the time, meaning that results are less dispersed. <br>
The other strategies are clustered closely together with the strategy to draw up to 15 and the conventional strategy described above being the best strategies. The standard deviation for all these strategies is close to 1 as they result in wins and losses almost equally often, meaning that the observations are widely dispersed.
### Behavior with increasing sample size
The code also demonstrates the behavior of the expected value and standard deviation with increasing sample size. It runs simulations with different sample sizes, ranging from 10 to 1 Million rounds, using the conventional strategy and runs the simulation 10 times for each sample size. The scatter plot shows the relationship between standard deviation and expected value for each sample size, providing insights into the convergence of the Monte Carlo method as the sample size increases. The vertical grey line shows the expected value of 0, any strategy with expected values below this line results in loosing money to the casino.
<br>
![Image]( https://github.com/kheuer/monte_carlo_simulation_blackjack/blob/main/conventional_policy_behaviour.png)
<br>
As we can see the orange points are the most widely dispersed on the plot, this can be attributed to the low sample size of only 10 games, chance plays a big part in where these simulations manifest. As the sample size increases the distinct simulations should be clustered more closely together due to the law of big numbers. We can observe this on the plot with the green points being much more closely together and all experiments with a sample size of 10 thousand games or more being indistinguishable close to each other, closely below the break-even expected value of 0 and a standard deviation close to 1.

