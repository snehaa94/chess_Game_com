# ♟️ ChessArena — Full-Stack AI Chess Game

<p align="center">
  <strong>A production-ready full-stack chess application built with Python, Django, JavaScript and AI.</strong>
</p>

<p align="center">
  <a href="https://chess-game-mnzu.onrender.com">
    <strong>🌐 Live Demo</strong>
  </a>
</p>

---

## 📌 Table of Contents

* [About the Project](#-about-the-project)
* [Project Highlights](#-project-highlights)
* [Features](#-features)
* [Demo](#-demo)
* [Architecture](#-architecture)
* [Application Workflow](#-application-workflow)
* [Technology Stack](#-technology-stack)
* [Project Structure](#-project-structure)
* [Frontend](#-frontend)
* [Backend](#-backend)
* [Chess Engine](#-chess-engine)
* [AI Implementation](#-ai-implementation)
* [API Documentation](#-api-documentation)
* [Game State Management](#-game-state-management)
* [Installation](#-installation)
* [Running the Project](#-running-the-project)
* [Testing](#-testing)
* [Debugging](#-debugging)
* [Deployment](#-deployment)
* [Environment Variables](#-environment-variables)
* [SDLC](#-software-development-life-cycle)
* [Security](#-security)
* [Performance Considerations](#-performance-considerations)
* [Challenges](#-challenges-and-solutions)
* [Future Improvements](#-future-improvements)
* [Learning Outcomes](#-learning-outcomes)
* [Interview Explanation](#-interview-explanation)
* [Author](#-author)
* [License](#-license)

---

# 🎯 About the Project

**ChessArena** is a full-stack web-based chess application that allows a user to play a game of chess against a computer-controlled opponent.

The project was developed to demonstrate practical software development skills including:

* Backend development
* Frontend development
* API development
* Game-state management
* Algorithm implementation
* AI decision-making
* Testing
* Debugging
* Version control
* Deployment
* Software Development Life Cycle (SDLC)

The application uses **Django** as the backend framework and **JavaScript** for the interactive frontend.

Chess rules and legal move validation are handled using the `python-chess` library.

The computer opponent uses a **Minimax-based AI with Alpha-Beta pruning** to select moves.

---

# 🚀 Project Highlights

| Area                | Implementation               |
| ------------------- | ---------------------------- |
| Frontend            | HTML5, CSS3, JavaScript      |
| Backend             | Python + Django              |
| Chess Rules         | python-chess                 |
| AI                  | Minimax + Alpha-Beta pruning |
| Communication       | JSON APIs                    |
| Testing             | Django automated tests       |
| Version Control     | Git + GitHub                 |
| Production Server   | Gunicorn                     |
| Static Files        | WhiteNoise                   |
| Deployment          | Render                       |
| Development Process | SDLC                         |

---

# ✨ Features

## ♟️ Core Chess Features

* Human vs Computer gameplay
* Standard 8×8 chess board
* White player controlled by user
* Black player controlled by computer
* Legal chess move validation
* Piece selection
* Legal move highlighting
* Capture highlighting
* Turn management
* Check detection
* Checkmate detection
* Draw detection
* Game-over detection
* New Game functionality
* Board Flip functionality

---

## 🤖 AI Features

The computer opponent includes:

* Minimax search
* Alpha-Beta pruning
* Legal move generation
* Board evaluation
* Automated computer moves

The AI does not randomly select a move. It evaluates possible moves and searches future positions before selecting a move.

---

## 🎨 User Interface

The application contains:

* Modern dark-themed interface
* Responsive layout
* Interactive chess board
* Piece selection
* Legal move indicators
* Capture indicators
* Game status
* Turn information
* New Game button
* Flip Board button
* Responsive mobile layout

---

# 🌐 Live Demo

The deployed application is available at:

**https://chess-game-mnzu.onrender.com**

The production application runs using Django with Gunicorn and Render.

---

# 🏗️ Architecture

The application follows a simple layered architecture.

```text
                        USER
                         │
                         ▼
                ┌─────────────────┐
                │   Web Browser   │
                └────────┬────────┘
                         │
                         ▼
                ┌─────────────────┐
                │ HTML / CSS / JS │
                │    Frontend     │
                └────────┬────────┘
                         │
                    JSON / HTTP
                         │
                         ▼
                ┌─────────────────┐
                │ Django Backend  │
                │     views.py    │
                └────────┬────────┘
                         │
              ┌──────────┴──────────┐
              │                     │
              ▼                     ▼
      ┌───────────────┐     ┌───────────────┐
      │ python-chess  │     │   Chess AI    │
      │ Rule Engine   │     │ Minimax +     │
      │               │     │ Alpha-Beta    │
      └───────────────┘     └───────────────┘
              │                     │
              └──────────┬──────────┘
                         ▼
                  Updated Game State
                         │
                         ▼
                ┌─────────────────┐
                │ JavaScript UI   │
                │ Board Rendering │
                └─────────────────┘
```

---

# 🔄 Application Workflow

The complete gameplay flow works like this:

```text
User opens application
        ↓
GET /api/state/
        ↓
Django returns current board state
        ↓
JavaScript renders chess board
        ↓
User selects a piece
        ↓
JavaScript identifies legal moves
        ↓
User selects destination
        ↓
POST /api/move/
        ↓
Django receives UCI move
        ↓
python-chess validates move
        ↓
Board state is updated
        ↓
Check game status
        ↓
Computer AI calculates response
        ↓
AI selects best legal move
        ↓
Computer move applied
        ↓
Updated state returned
        ↓
JavaScript re-renders board
```

---

# 🧰 Technology Stack

## Backend

### Python

Used as the primary programming language.

Responsibilities:

* Backend logic
* Game management
* AI logic
* API handling

### Django

Used as the backend web framework.

Responsibilities:

* URL routing
* HTTP request handling
* API endpoints
* CSRF protection
* Application configuration
* Static file configuration

### python-chess

Used as the chess rule engine.

Responsibilities:

* Board representation
* Legal moves
* Move validation
* Check detection
* Checkmate detection
* Draw detection
* FEN representation
* UCI move handling

---

# 🎨 Frontend Technology

## HTML5

Used to structure:

* Header
* Game section
* Chess board
* Controls
* Feature sections
* Footer

## CSS3

Used for:

* Layout
* Responsive design
* Chess board styling
* Colors
* Buttons
* Animations
* Mobile support

## JavaScript

Used for:

* Dynamic board rendering
* Piece selection
* Move selection
* API communication
* Game state updates
* Board flipping
* New game functionality
* Legal move highlighting

---

# 🧠 Chess Engine

The application uses `python-chess` to manage chess rules.

Instead of manually implementing every chess rule, the backend uses a reliable chess library to validate moves.

This handles complex rules such as:

* Legal piece movement
* Check
* Checkmate
* Castling
* En passant
* Pawn promotion
* Draw conditions

---

# 🤖 AI Implementation

The computer opponent is based on the **Minimax algorithm**.

## What is Minimax?

Minimax is a decision-making algorithm commonly used in two-player games.

The computer considers:

> "If I make this move, what is the opponent likely to do next?"

It searches possible future positions and evaluates them.

---

## Minimax Flow

```text
Current Position
       ↓
Generate Legal Moves
       ↓
Try Each Move
       ↓
Generate Opponent Responses
       ↓
Evaluate Future Positions
       ↓
Compare Scores
       ↓
Select Best Move
```

---

# ✂️ Alpha-Beta Pruning

Minimax can become expensive because chess has many possible moves.

Alpha-Beta pruning improves Minimax by eliminating branches that do not need to be evaluated.

```text
                 Root
                  │
          ┌───────┼───────┐
          ▼       ▼       ▼
        Move A  Move B  Move C
          │       │       │
        Search  Search  Search
          │       │
          ▼       ▼
       Useful   Useful
       branch   branch

              Move C
                 ↓
          unnecessary branch
                 ↓
              PRUNED
```

This reduces unnecessary computation and makes the AI faster.

---

# 🎯 AI Decision Process

The computer:

1. Gets the current board.
2. Generates legal moves.
3. Simulates possible moves.
4. Searches future positions.
5. Evaluates positions.
6. Applies Minimax.
7. Uses Alpha-Beta pruning.
8. Selects the best available move.
9. Applies the move to the board.

---

# 🔌 API Documentation

The frontend communicates with Django through JSON-based API endpoints.

---

## 1. Get Current Game State

### Endpoint

```http
GET /api/state/
```

### Purpose

Returns the current state of the game.

### Example Response

```json
{
    "fen": "current-board-position",
    "turn": "white",
    "legal_moves": [],
    "game_over": false
}
```

The exact response depends on the current game position.

---

# 2. Make a Move

### Endpoint

```http
POST /api/move/
```

### Request

```json
{
    "uci": "e2e4"
}
```

### UCI Format

A chess move is represented using UCI notation.

For example:

```text
e2e4
```

means:

```text
e2 → e4
```

---

## Move Processing

The backend performs:

```text
Receive UCI move
      ↓
Validate move
      ↓
Apply player move
      ↓
Check game status
      ↓
Generate computer move
      ↓
Apply computer move
      ↓
Return updated state
```

---

# 3. Start New Game

### Endpoint

```http
POST /api/new-game/
```

### Purpose

Resets the board and starts a new game.

---

# 🗂️ Project Structure

```text
Chess_Game_Com/
│
├── chessgame/
│   │
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   │
│   └── game/
│       │
│       ├── __init__.py
│       ├── apps.py
│       ├── views.py
│       │
│       ├── tests/
│       │   └── test_game.py
│       │
│       ├── templates/
│       │   └── game/
│       │       └── index.html
│       │
│       └── static/
│           └── game/
│               ├── app.js
│               └── style.css
│
├── manage.py
├── requirements.txt
├── Procfile
├── render.yaml
├── SDLC.md
├── .env.example
├── .gitignore
└── README.md
```

---

# 📄 Important Files

| File               | Purpose                         |
| ------------------ | ------------------------------- |
| `manage.py`        | Django command-line utility     |
| `settings.py`      | Django configuration            |
| `urls.py`          | URL routing                     |
| `views.py`         | Game logic and API endpoints    |
| `index.html`       | Main UI                         |
| `app.js`           | Frontend game interaction       |
| `style.css`        | UI styling                      |
| `test_game.py`     | Automated tests                 |
| `requirements.txt` | Python dependencies             |
| `Procfile`         | Production server command       |
| `render.yaml`      | Render deployment configuration |
| `SDLC.md`          | SDLC documentation              |
| `.env.example`     | Environment variable example    |
| `.gitignore`       | Files excluded from Git         |

---

# 💻 Installation

## Prerequisites

Before running the project, install:

* Python 3.11+
* Git
* A modern web browser

---

## Step 1 — Clone Repository

```bash
git clone https://github.com/snehaa94/Chess_Game_Com.git
```

Move into the project:

```bash
cd Chess_Game_Com
```

---

# 🐍 Step 2 — Create Virtual Environment

Windows:

```powershell
python -m venv env
```

Activate:

```powershell
.\env\Scripts\Activate.ps1
```

If PowerShell blocks activation:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```

Then activate again:

```powershell
.\env\Scripts\Activate.ps1
```

---

# 📦 Step 3 — Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🗄️ Step 4 — Apply Migrations

```bash
python manage.py migrate
```

---

# 🧪 Step 5 — Run Tests

```bash
python manage.py test
```

---

# ▶️ Step 6 — Start Development Server

```bash
python manage.py runserver
```

Open:

```text
http://127.0.0.1:8000/
```

---

# 🔧 Development Commands

## Check Django Configuration

```bash
python manage.py check
```

## Run Tests

```bash
python manage.py test
```

## Start Server

```bash
python manage.py runserver
```

## Collect Static Files

```bash
python manage.py collectstatic
```

---

# 🧪 Testing Strategy

Testing is an important part of the project.

The application contains Django automated tests for core functionality.

Tests can be executed using:

```bash
python manage.py test
```

---

## Testing Areas

The project can test:

### API availability

Verifies that API endpoints respond correctly.

### Game initialization

Verifies that a new game starts from the correct board position.

### Legal moves

Verifies that valid chess moves are accepted.

### Invalid moves

Verifies that illegal moves are rejected.

### Game state

Verifies that the returned state contains expected information.

### New Game

Verifies that the game can be reset.

---

# 🐞 Debugging

During development, debugging involved both frontend and backend issues.

## Backend Debugging

Django development server logs were used to identify:

* HTTP errors
* API errors
* Configuration issues
* Python exceptions

Example:

```text
GET /api/state/ 200
POST /api/move/ 200
POST /api/new-game/ 200
```

A `200` response indicates a successful request.

---

## Frontend Debugging

Browser Developer Tools were used for:

* JavaScript errors
* DOM issues
* CSS problems
* API request inspection
* Console debugging

---

# 🔐 Security

The application uses Django's CSRF protection for POST requests.

The frontend sends the CSRF token with API requests.

Sensitive configuration should not be stored directly in source code.

Use environment variables for secrets and environment-specific configuration.

---

# 🌱 Environment Variables

An example environment configuration is provided in:

```text
.env.example
```

Local secrets should be stored in:

```text
.env
```

The `.env` file should not be committed to GitHub.

---

# 🚀 Deployment

The project is configured for deployment on Render.

Deployment-related files:

```text
Procfile
render.yaml
requirements.txt
```

---

# ☁️ Production Architecture

```text
                GitHub
                   │
                   ▼
                Render
                   │
                   ▼
          Install Dependencies
                   │
                   ▼
              Django App
                   │
                   ▼
               Gunicorn
                   │
                   ▼
             WhiteNoise
                   │
                   ▼
             Live Website
```

---

# ⚙️ Production Server

The application uses Gunicorn as the WSGI server.

Example production command:

```bash
gunicorn chessgame.wsgi:application
```

---

# 📦 Dependencies

Dependencies are maintained in:

```text
requirements.txt
```

The dependency file allows the same Python packages to be installed in development and production environments.

---

# 🔄 Git Workflow

The project uses Git for version control.

Typical workflow:

```bash
git status
git add .
git commit -m "Update project"
git push
```

The GitHub repository acts as the central source-code repository.

---

# 🌿 Branching

The main production branch is:

```text
main
```

Recommended workflow for future development:

```text
main
 │
 ├── feature/ai-improvements
 │
 ├── feature/user-authentication
 │
 └── feature/game-history
```

---

# 📋 Software Development Life Cycle

The project follows the major phases of SDLC.

---

## 1️⃣ Requirement Analysis

The first step was identifying the requirements.

### Functional Requirements

* User can start a chess game.
* User can select pieces.
* User can make legal moves.
* Computer can make moves.
* Game can detect game-over conditions.
* User can start a new game.
* User can flip the board.

### Non-Functional Requirements

* Responsive interface
* Fast interaction
* Maintainable code
* Secure API communication
* Deployable application
* Testable backend

---

# 2️⃣ System Design

The application was divided into:

```text
Frontend
   ↓
JavaScript
   ↓
Django API
   ↓
Chess Rule Engine
   ↓
AI Engine
```

This separation makes the application easier to maintain.

---

# 3️⃣ Implementation

The application was implemented using:

* Python
* Django
* JavaScript
* HTML
* CSS
* python-chess
* Minimax
* Alpha-Beta pruning

---

# 4️⃣ Testing

Automated tests were created for important functionality.

Manual testing was also performed by:

* Starting games
* Moving pieces
* Capturing pieces
* Testing invalid moves
* Starting new games
* Flipping the board
* Playing complete games

---

# 5️⃣ Debugging

Issues discovered during development were investigated using:

* Django logs
* Browser Developer Tools
* JavaScript console
* API responses
* HTTP status codes

---

# 6️⃣ Deployment

The application was prepared for production using:

* GitHub
* Render
* Gunicorn
* WhiteNoise

---

# 7️⃣ Maintenance

The architecture allows additional features to be added in future versions without rebuilding the entire application.

---

# 🧩 Challenges and Solutions

## Challenge 1 — Implementing Chess Rules

Chess has many complex rules.

### Solution

The `python-chess` library was used for reliable legal move validation and board management.

---

## Challenge 2 — Building Computer Intelligence

A random move generator would not provide meaningful gameplay.

### Solution

Minimax with Alpha-Beta pruning was implemented to allow the computer to evaluate possible positions.

---

## Challenge 3 — Frontend and Backend Communication

The browser needs to communicate with the Django game state.

### Solution

JSON-based API endpoints were created for:

```text
/api/state/
/api/move/
/api/new-game/
```

---

## Challenge 4 — Dynamic Board Rendering

The chess board needs to update after every move.

### Solution

JavaScript dynamically renders the board using the latest game state returned by the backend.

---

## Challenge 5 — Deployment

A Django development server is not suitable for production.

### Solution

Gunicorn was configured as the production WSGI server, with Render used for hosting.

---

# 📱 Responsive Design

The application is designed to work across different screen sizes.

Supported layouts include:

* Desktop
* Laptop
* Tablet
* Mobile

CSS media queries are used to adapt the interface.

---

# 📈 Performance Considerations

Several approaches help maintain acceptable performance:

* Alpha-Beta pruning reduces unnecessary AI searches.
* Legal moves are generated through `python-chess`.
* Frontend rendering is performed dynamically.
* Static assets are served using WhiteNoise in production.
* Gunicorn is used for production request handling.

---

# 🔮 Future Improvements

The current application can be extended significantly.

## 👤 User Authentication

Add:

* Registration
* Login
* Logout
* User profiles

---

## 💾 Game History

Store:

* Previous games
* Moves
* Results
* Player information

---

## 📊 Player Statistics

Add:

* Games played
* Wins
* Losses
* Draws
* Win percentage

---

## 🏆 Leaderboard

Create a ranking system for players.

---

## 🎚️ AI Difficulty

Introduce:

```text
Easy
Medium
Hard
Expert
```

Different difficulty levels could use different search depths and evaluation strategies.

---

## 🌐 Multiplayer

Add human-vs-human multiplayer using WebSockets.

Possible architecture:

```text
Player A
   │
   ▼
WebSocket Server
   │
   ▼
Game Session
   │
   ▼
WebSocket Server
   │
   ▼
Player B
```

---

## ⏱️ Chess Clock

Add standard chess time controls such as:

```text
5 + 0
10 + 0
10 + 5
15 + 10
```

---

## 🧠 AI Move Explanation

A future version could explain:

> Why the computer selected a particular move.

This could combine the chess engine with an AI explanation layer.

---

# 🎓 Learning Outcomes

This project provided practical experience with:

### Programming

* Python
* JavaScript

### Web Development

* Django
* HTML
* CSS
* REST-style APIs
* JSON

### Algorithms

* Minimax
* Alpha-Beta pruning
* Game-tree search

### Software Engineering

* SDLC
* Requirements
* Architecture
* Testing
* Debugging
* Deployment
* Version control

### DevOps / Deployment

* Git
* GitHub
* Gunicorn
* Render
* Static file configuration

---

# 💼 Interview Explanation

A concise way to explain the project in an interview:

> **"I developed a full-stack chess application using Python and Django where a user can play against a computer opponent. I used python-chess for legal move validation and board-state management, while the computer player uses a Minimax algorithm with Alpha-Beta pruning to select moves. The frontend is built using HTML, CSS and JavaScript and communicates with the Django backend through JSON APIs. I also added automated tests and prepared the application for deployment using Gunicorn, WhiteNoise and Render. Through this project, I worked on the complete SDLC from requirement analysis and design to implementation, testing, debugging and deployment."**

---

# 🎤 Key Interview Questions

## Why did you use Django?

Django provides a structured backend framework with routing, security, request handling and application management.

---

## Why did you use python-chess?

Implementing every chess rule manually would be complex and error-prone. `python-chess` provides reliable chess board and legal-move functionality.

---

## Why Minimax?

Minimax is suitable for two-player games because it evaluates possible future moves assuming both players try to make good decisions.

---

## Why Alpha-Beta pruning?

It reduces unnecessary Minimax calculations and improves search efficiency.

---

## How does the frontend communicate with Django?

The JavaScript frontend sends HTTP requests to Django API endpoints and receives JSON responses containing the current game state.

---

## How is a move represented?

Moves are sent using UCI notation.

For example:

```text
e2e4
```

means the piece moves from `e2` to `e4`.

---

## How did you test the application?

I used Django automated tests for core API and game functionality and also manually tested gameplay scenarios such as legal moves, invalid moves, captures, new games and game-over conditions.

---

## What was the most challenging part?

One challenging part was integrating the chess rules with the AI and frontend. The backend needed to validate every user move, update the game state, calculate the computer response and then send the updated state back to the frontend.

---

# 📸 Screenshots

Add screenshots of your application here.

Recommended structure:

```text
screenshots/
├── home.png
├── chess-board.png
├── piece-selection.png
├── computer-move.png
└── mobile-view.png
```

Then add them to this README:

```markdown
![ChessArena Home](screenshots/home.png)

![ChessArena Gameplay](screenshots/chess-board.png)

![ChessArena Mobile](screenshots/mobile-view.png)
```

---

# 📊 Project Summary

| Category             | Details                    |
| -------------------- | -------------------------- |
| Project Type         | Full-Stack Web Application |
| Domain               | Game / AI                  |
| Backend              | Django                     |
| Language             | Python                     |
| Frontend             | HTML, CSS, JavaScript      |
| Chess Engine         | python-chess               |
| AI Algorithm         | Minimax + Alpha-Beta       |
| API                  | JSON-based HTTP APIs       |
| Testing              | Django Test Framework      |
| Version Control      | Git                        |
| Repository           | GitHub                     |
| Deployment           | Render                     |
| Production Server    | Gunicorn                   |
| Static Files         | WhiteNoise                 |
| Development Approach | SDLC                       |

---

# 🏆 What This Project Demonstrates

This project demonstrates practical knowledge of:

```text
        SOFTWARE DEVELOPMENT
                 │
     ┌───────────┼───────────┐
     ▼           ▼           ▼
  Frontend    Backend       AI
     │           │           │
 HTML/CSS/JS   Django     Minimax
     │           │           │
     └───────────┼───────────┘
                 ▼
                APIs
                 │
                 ▼
              Testing
                 │
                 ▼
              Git/GitHub
                 │
                 ▼
             Deployment
```

---

# 👩‍💻 Author

## Sneha Kashyap

B.Tech Computer Science Graduate

### GitHub

https://github.com/snehaa94

---

# ⭐ Support

If you found this project interesting, please consider giving the repository a ⭐ on GitHub.

---

# 📜 License

This project is created for educational and portfolio purposes.

---

# ❤️ Final Note

ChessArena was developed as a practical software engineering project to demonstrate how a complete application can be taken from:

```text
Idea
  ↓
Requirements
  ↓
System Design
  ↓
Implementation
  ↓
AI Integration
  ↓
Testing
  ↓
Debugging
  ↓
Git/GitHub
  ↓
Deployment
  ↓
Production Application
```

**Built with Python, Django, JavaScript and AI. ♟️**
