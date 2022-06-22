class Arena:
    """
    Handles creation of Board and getting the latest updates on the board
    """

    def __init__(self):
        """
        Initialize Arena and creates board variable.
        """
        self.board = self.create_board()

    def create_board(self):
        """
        Creates board for the game
        Returns:
            list: list of dictionaries which represents row and column
        """
        board = []
        for x_pos in range(0, 8):
            row = [{"x": x_pos, "y": y_pos} for y_pos in range(0, 8)]
            board.append(row)
        return board

    def get_board(self):
        """
        Returns:
            str: formatted board
        """
        map_str = f"{' _'*8}\n"
        for row in self.board:
            row_str = ""
            for data in row:
                if "knight" in data:
                    name = data['knight']
                elif "item" in data:
                    name = data['item'][0]["name"]
                elif "final_position" in data:
                    name = data["final_position"]
                else:
                    name = "_"

                if data == row[-1]:
                    row_str += f"{name}|"
                elif data == row[0]:
                    row_str += f"|{name}|"
                else:
                    row_str += f"{name}|"
            map_str += row_str + "\n"
        return map_str
