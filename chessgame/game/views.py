import json
import random
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.http import require_GET, require_POST
from django.views.decorators.csrf import ensure_csrf_cookie
import chess

# Simple deterministic evaluation for a lightweight, free-to-deploy AI.
VALUES = {chess.PAWN: 100, chess.KNIGHT: 320, chess.BISHOP: 330, chess.ROOK: 500, chess.QUEEN: 900, chess.KING: 20000}

def score(board):
    if board.is_checkmate():
        return -999999 if board.turn else 999999
    if board.is_stalemate() or board.is_insufficient_material() or board.can_claim_fifty_moves():
        return 0
    value = 0
    for piece_type, piece_value in VALUES.items():
        value += len(board.pieces(piece_type, chess.WHITE)) * piece_value
        value -= len(board.pieces(piece_type, chess.BLACK)) * piece_value
    value += 10 * (board.legal_moves.count() if board.turn == chess.WHITE else -board.legal_moves.count())
    return value

def minimax(board, depth, alpha=-10**9, beta=10**9):
    if depth == 0 or board.is_game_over():
        return score(board), None
    moves = list(board.legal_moves)
    # Shuffle equal choices to make the AI less repetitive while remaining simple.
    random.shuffle(moves)
    maximizing = board.turn == chess.WHITE
    best_move = None
    if maximizing:
        best = -10**9
        for mv in moves:
            board.push(mv)
            val, _ = minimax(board, depth - 1, alpha, beta)
            board.pop()
            if val > best:
                best, best_move = val, mv
            alpha = max(alpha, best)
            if beta <= alpha: break
        return best, best_move
    best = 10**9
    for mv in moves:
        board.push(mv)
        val, _ = minimax(board, depth - 1, alpha, beta)
        board.pop()
        if val < best:
            best, best_move = val, mv
        beta = min(beta, best)
        if beta <= alpha: break
    return best, best_move

def get_board(request):
    fen = request.session.get('fen')
    try:
        return chess.Board(fen) if fen else chess.Board()
    except ValueError:
        request.session.pop('fen', None)
        return chess.Board()

def save_board(request, board):
    request.session['fen'] = board.fen()
    request.session.modified = True

def payload(board, message=''):
    return {
        'fen': board.fen(),
        'turn': 'white' if board.turn == chess.WHITE else 'black',
        'legal_moves': [m.uci() for m in board.legal_moves],
        'last_move': request_last_move(board),
        'game_over': board.is_game_over(),
        'result': board.result() if board.is_game_over() else None,
        'status': message or status_text(board),
    }

def request_last_move(board):
    if not board.move_stack:
        return None
    return board.peek().uci()

def status_text(board):
    if board.is_checkmate(): return 'Checkmate!'
    if board.is_stalemate(): return 'Stalemate.'
    if board.is_insufficient_material(): return 'Draw: insufficient material.'
    if board.is_check(): return ('White' if board.turn else 'Black') + ' is in check.'
    return ('White' if board.turn else 'Black') + ' to move.'

@require_GET
@ensure_csrf_cookie
def home(request):
    if 'fen' not in request.session:
        save_board(request, chess.Board())
    return render(request, 'game/index.html')

@require_GET
def state(request):
    return JsonResponse(payload(get_board(request)))

@require_POST
def new_game(request):
    save_board(request, chess.Board())
    return JsonResponse(payload(chess.Board(), 'New game started. You are White.'))

@require_POST
def move(request):
    board = get_board(request)
    try:
        data = json.loads(request.body or '{}')
        uci = data.get('uci', '')
        mv = chess.Move.from_uci(uci)
    except (ValueError, json.JSONDecodeError):
        return JsonResponse({'error': 'Invalid move format.'}, status=400)
    if board.turn != chess.WHITE:
        return JsonResponse({'error': 'It is the computer\'s turn.'}, status=400)
    if mv not in board.legal_moves:
        return JsonResponse({'error': 'Illegal chess move.'}, status=400)
    san = board.san(mv)
    board.push(mv)
    if not board.is_game_over() and board.turn == chess.BLACK:
        _, ai_move = minimax(board, 2)
        if ai_move is not None:
            ai_san = board.san(ai_move)
            board.push(ai_move)
        else:
            ai_san = None
    else:
        ai_san = None
    save_board(request, board)
    data = payload(board)
    data.update({'player_move': san, 'computer_move': ai_san})
    return JsonResponse(data)

@require_GET
def health(request):
    return JsonResponse({'status': 'ok', 'service': 'python-chess-game'})
