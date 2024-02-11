# Game State Strategist for Manchester City FC

## Introduction

The Game State Strategist is a cutting-edge tool designed to revolutionize football match strategies for Manchester City FC by providing real-time, data-driven positioning recommendations against Liverpool. Leveraging detailed player statistics and live match data, this tool aims to optimize player positions on the field, enhancing Manchester City's performance and strategic advantage.

## Project Objective

This tool's primary goal is to utilize live game data, including player coordinates, ball possession, the current score, and elapsed match time, to recommend optimal positioning for Manchester City FC players. By doing so, it seeks to increase the team's chances of scoring, maintaining possession, and ultimately winning the match against Liverpool.

## Features

- **Real-Time Optimization**: Generates positioning recommendations in real-time based on the current state of the match.
- **Data-Driven Decisions**: Utilizes a rich dataset, including player statistics from FBRef and live match data, to inform recommendations.
- **Strategic Insights**: Offers strategic positioning advice to avoid offsides and maximize offensive and defensive opportunities.
- **Dynamic Adaptation**: Adjusts recommendations as the game progresses, reflecting changes in score, possession, and player performance.

## Getting Started

### Prerequisites

- Python 3.8 or higher
- Necessary Python libraries (listed in `requirements.txt`)

### Installation

1. Clone the repository to your local machine:

```bash
git clone https://github.com/avijeetranawat/StrategAI.git
```

2. Change into the project directory:
```bash
cd StrategAI
```

3. Install the required Python libraries:
```bash
pip install -r requirements.txt
```

### Usage

To utilize the Game State Strategist, you need to provide input data in a specific JSON format, including details such as player coordinates, current score, ball possession, and elapsed time.

1. Prepare your input data in the required format. Refer to `data_processing/input.json` for guidance.

2. Execute the strategy script with the path to your input data:
```bash
python strategist.py --input path_to_your_input.json
```
3. Review the output JSON file for the optimized player positions.

### Input Format

```json
{
    "ManchesterCity": {
        "Coordinates": {
            "Ederson": [1.97, -3.52],
            "Julián Álvarez": [0.97, 4.08],
            "Stefan Ortega": [-2.61, -4.09],
            "Phil Foden": [0.78, -0.88],
            "Kyle Walker": [-3.04, -3.39],
            "Bernardo Silva": [1.85, 2.73],
            "Rodri": [-0.31, -3.16],
            "Mateo Kovačić": [-2.31, 0.5],
            "Erling Haaland": [-1.35, 3.39],
            "Nathan Aké": [-3.0, -2.77],
            "Jeremy Doku": [-1.02, 4.37]
        },
        "Score": 1
    },
    "Liverpool": {
        "Coordinates": {
            "Luis Díaz": [-1.97, 2.64],
            "Darwin Núñez": [-2.76, 3.15],
            "Dominik Szoboszlai": [1.71, 0.36],
            "Virgil van Dijk": [-1.68, -1.51],
            "Cody Gakpo": [-3.02, 0.55],
            "Harvey Elliott": [1.13, -0.47],
            "Trent Alexander-Arnold": [-2.07, -2.11],
            "Alexis Mac Allister": [-1.35, 0.51],
            "Alisson": [1.44, -3.65],
            "Ryan Gravenberch": [-0.81, 1.21],
            "Joe Gomez": [-3.12, -1.82]
        },
        "Score": 2,
        "BallPossession": "Luis Díaz"
    },
    "TimeElapsedInMinutes": 45
}
```

### Output Format

```json
{
    "ManchesterCity": {
        "OptimizedCoordinates": {
            "Ederson": [1.97, -3.52],
            "Julián Álvarez": [0.97, 4.08],
            "Stefan Ortega": [-2.61, -4.09],
            "Phil Foden": [0.78, -0.88],
            "Kyle Walker": [-3.04, -3.39],
            "Bernardo Silva": [1.85, 2.73],
            "Rodri": [-0.31, -3.16],
            "Mateo Kovačić": [-2.31, 0.5],
            "Erling Haaland": [-1.35, 3.39],
            "Nathan Aké": [-3.0, -2.77],
            "Jeremy Doku": [-1.02, 4.37]
        }
    },
    "Reason": "1-line summary"
}
```
Ensure that player coordinates are within the specified range, and the game state details are accurately represented.

### Acknowledgments

- Thanks to FBRef for providing comprehensive player statistics.
- Special thanks to Manchester City FC and Liverpool FC, whose competitive spirit inspired this project.