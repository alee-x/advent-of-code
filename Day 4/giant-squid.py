import numpy as np


def readfile():
    fname = 'input.txt'
    line_counter, board_counter = 0, 0
    drawn_numbers, bingo_boards, tmp_board, blank_boards = [], [], [], []
    with open(fname, "r") as fd:
        for line in fd.read().splitlines():
            # check if it's the first line, because this is our bingo numbers
            if line_counter == 0:
                drawn_numbers = np.array([int(x) for x in line.split(",")])
                line_counter += 1
                continue
            # check if the line is blank, if it is then reset the board_counter
            if len(line) > 0 and board_counter < 6:
                row_numbers = np.array([int(x) for x in line.split(" ") if x != ''])
                tmp_board.append(row_numbers)
                board_counter += 1
                line_counter += 1
            if board_counter == 5:
                bingo_boards.append(np.array(tmp_board))
                blank_boards.append(np.zeros(shape=(5, 5), dtype=bool))
                tmp_board = []
                board_counter = 0
    return drawn_numbers, np.array(bingo_boards), np.array(blank_boards)


def winning_score(board, mask, number_called):
    sum_unmarked = np.sum(board[~mask])
    return number_called * sum_unmarked


def partone(drawn_numbers, bingo_boards, board_masks):
    score = False
    for number in drawn_numbers:
        for count, board in enumerate(bingo_boards):
            rows, cols = np.where(board == number)
            if len(rows) > 0 and len(cols) > 0:
                board_masks[count][rows[0]][cols[0]] = True
            # does this board mask now have a full row or columns of Trues?
            full_column = np.any(np.all(board_masks[count], axis=0))
            full_row = np.any(np.all(board_masks[count], axis=1))
            if full_column or full_row:
                score = winning_score(board, board_masks[count], number)
                break
        if score is not False:
            break
    return score


def parttwo(drawn_numbers, bingo_boards, board_masks):
    number_at_win_index = np.full(len(bingo_boards), -1)
    for count, board in enumerate(bingo_boards):
        while number_at_win_index[count] == -1:
            for inx, number in enumerate(drawn_numbers):
                rows, cols = np.where(board == number)
                if len(rows) > 0 and len(cols) > 0:
                    board_masks[count][rows[0]][cols[0]] = True
                full_column = np.any(np.all(board_masks[count], axis=0))
                full_row = np.any(np.all(board_masks[count], axis=1))
                if full_column or full_row:
                    number_at_win_index[count] = inx
                    break
    score = winning_score(bingo_boards[np.argmax(number_at_win_index)],
                          board_masks[np.argmax(number_at_win_index)],
                          drawn_numbers[np.max(number_at_win_index)])
    return score


if __name__ == "__main__":
    drawn_numbers, bingo_boards, blanks = readfile()
    print(partone(drawn_numbers, bingo_boards, blanks))
    drawn_numbers, bingo_boards, blanks = readfile()
    print(parttwo(drawn_numbers, bingo_boards, blanks))