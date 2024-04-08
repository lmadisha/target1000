# Target 1000 Game

## Introduction

Welcome to the Target 1000 game repository! This Python-based project simulates a mathematical dice game where the objective is to place the outcomes of dice rolls onto a 3x3 grid, aiming to get the sums of the rows as close to 1000 as possible. This game not only serves as a fun mathematical puzzle but also offers a framework for algorithmic experimentation and strategy optimization.

## Getting Started

### Prerequisites

Before you begin, ensure you have Python 3 installed on your computer. You can download Python from [python.org](https://www.python.org/downloads/).

### Installation

1.  Clone the repository to your local machine:

```bash
git clone https://github.com/atomic-maths/target1000.git
```

2.  Navigate to the cloned repository:

```bash
cd target1000
```

## Game Description

In Target 1000, players roll a dice and place each outcome on a 3x3 grid using Cartesian coordinates. The game's goal is to achieve a sum as close to 1000 as possible by adding together the numbers in each row of the grid.


### Playing the Game Manually

To play the game manually, run `manual_game.py`. This mode allows you to choose where each dice roll goes on the grid and calculates your score at the end of the game.

bash

`python manual_game.py` 

### Benchmarking Your Strategy

The repository includes a benchmarking tool, `benchmark.py`, that allows you to test your strategies implemented in `strategy.py` over 100,000 games to see how close to 1000 you can get on average.

bash

`python benchmark.py` 

## Customizing Your Strategy

To implement your own algorithm or strategy, modify the `strategy.py` file. This file contains a template strategy that you can replace with your own logic to optimize the game's outcome.

## Contributing

Contributions to the Target 1000 game are welcome! Whether it's enhancing the game mechanics, optimizing the default strategy, or fixing bugs, feel free to fork the repository and submit a pull request.

## License

This project is open-source and available under the MIT License.
