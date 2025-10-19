**Pygame Ping Pong**

A classic Ping Pong (Pong) game built with Python + Pygame.
Play against an AI opponent, with smooth controls, collision handling, scoring, and sound effects.
Includes replay options and a clean game-over screen.

**Features**

✅ Smooth paddle movement (W / S keys)
✅ AI opponent tracks the ball automatically
✅ Improved ball collision (no passing through paddles)
✅ Game Over screen when a player reaches the score limit
✅ Replay system — choose Best of 3 / 5 / 7 or exit
✅ Sound effects for:Paddle hits , Wall bounces,Scoring

**Folder structure**

pygame-pingpong/
├── main.py                      # Main game file
├── requirements.txt             # Python dependencies
├── game/
│   ├── game_engine.py           # Core game loop and logic
│   ├── paddle.py                # Paddle class
│   └── ball.py                  # Ball class and behavior
├── sounds/
│   ├── paddle_hit.wav           # Paddle hit sound
│   ├── wall_hit.wav             # Wall bounce sound
│   └── score.wav                # Scoring sound
└── README.md                    # Project documentation

└── README.md

**Sound Setup**

Add 3 sound files inside the sounds/ folder:paddle_hit.mp3,wall_hit.mp3,score.mp3

Use free sounds from https://pixabay.com/sound-effects/

**Installation & Running**
1.Clone this repository:
git clone https://github.com/<your-username>/pingpong.git
cd pingpong 

2.Install dependencies:
pip install -r requirements.txt

3.Run the game:
python main.py


**Game Rules**

First to reach 5 points wins by default.
After a win, choose:
Press 3, 5, or 7 → set Best of 3 / 5 / 7
Press ESC → Exit the game.

**Expected Behavior**

Smooth paddle and ball motion
AI plays competitively
Ball rebounds off walls and paddles
Score updates correctly
Game ends and restarts smoothly with replay options

**License**
This project is open-source and free to use for learning or personal projects.



