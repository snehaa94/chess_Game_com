# SDLC Documentation — ChessArena

## 1. Requirement Analysis
### Functional
1. User can start a new chess game.
2. User plays White against the computer.
3. System accepts only legal chess moves.
4. Computer automatically responds after a player move.
5. System detects check, checkmate, stalemate and draw states.
6. User can flip the board.
7. System exposes a health endpoint for deployment monitoring.

### Non-functional
- Responsive on desktop and mobile.
- Lightweight enough for a free hosting tier.
- Secure production defaults: secret key from environment and DEBUG disabled.
- Automated regression tests.

## 2. Design
Browser → Django JSON API → python-chess rule engine → minimax AI → session state.

The browser owns presentation state while the server is authoritative for chess legality and game state.

## 3. Implementation
- Django handles HTTP routes and sessions.
- `python-chess` handles chess rules and FEN/Move processing.
- Minimax + alpha-beta pruning selects the computer move.
- JavaScript renders the board and calls JSON APIs.
- WhiteNoise serves static files in production.

## 4. Testing
Run `python manage.py test`.
Test cases include page availability, new game state, legal move + AI response, illegal move rejection and health endpoint.

## 5. Deployment
Render runs the dependency installation and static collection, then starts Gunicorn with the Django WSGI application.

## 6. Maintenance / Future Scope
- User authentication and profiles
- Match history and leaderboard
- Difficulty levels
- PGN export/import
- Opening book
- Stronger chess engine integration
- PostgreSQL for persistent accounts and game history
