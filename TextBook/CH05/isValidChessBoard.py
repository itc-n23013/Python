def is_valid_chess_board(board):
    piece_limits = {
        'king': 1,
        'queen': 1,
        'rook': 2,
        'bishop': 2,
        'knight': 2,
        'pawn': 8
    }

    piece_count = {'w': {}, 'b': {}}
    for color in piece_count:
        piece_count[color] = {piece: 0 for piece in piece_limits}

    def is_valid_position(position):
        return len(position) == 2 and position[0] in '12345678' and position[1]

    def is_valid_piece(piece):
        return len(piece) > 1 and piece[0] in 'wb' and piece[1:] in piece_limits

    for position, piece in board.items():
        if not is_valid_position(position) or not is_valid_piece(piece):
            return False

        color = piece[0]
        piece_type = piece[1:]
        piece_count[color][piece_type] += 1
        if piece_count[color][piece_type] > piece_limits[piece_type]:
            return False

    return piece_count['w']['king'] == 1 and piece_count['b']['king'] == 1

board = {'1h': 'bking', '6c': 'wqueen', '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking'}
print(is_valid_chess_board(board)) 

