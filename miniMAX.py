def minimax(board, depth, maximizing_player):
    if depth == 0 or board.is_game_over():
        return evaluate(board)
    if maximizing_player:
        value = -float('inf')
        for move in board.legal_moves:
            board.push(move)
            value = max(value, minimax(board, depth - 1, False))
            board.pop()
        return value
    else:
        value = float('inf')
        for move in board.legal_moves:
            board.push(move)
            value = min(value, minimax(board, depth - 1, True))
            board.pop()
        return value
