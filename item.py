from arena import Arena


class Item:
    """
    Base class for Item and Knight. Responsible for updating positions of Item and Knight in map.
    """
    arena = Arena()
    board = arena.board

    @classmethod
    def reset_board(cls):
        """
        Resets the board class variable.
        """
        Item.board = Item.arena.create_board()

    def __init__(
        self, name: str, x: int, y: int, attack: int, defense: int, status: str,
        item_type: str, output_name: str, priority: int = 0
    ):
        """_summary_

        Args:
            name (str): name.
            x (int): x coordinate.
            y (int): y coordinate.
            attack (int): attack value
            defense (int): defense value
            status (str): EQUIPPED | NOT EQUIPPED
            item_type (str): item | knight
            output_name (str): fullname
            priority (int, optional): 0 is the highest. Defaults to 0.
        """

        self.name = name
        self.attack = attack
        self.defense = defense
        self.x = x
        self.y = y
        self.status = status
        self.item_type = item_type
        self.priority = priority
        self.output_name = output_name
        self.update_position_on_map()

    def update_position_on_map(self, new_location=[], is_dead=False):
        """
        Edits board properties base on the moves

        Args:
            new_location (list, optional): x and y coordinates .If empty will use self.x and self.x. Defaults to [].
            is_dead (bool, optional): _description_. Defaults to False.
        """
        if len(new_location) != 0:
            # for updating location
            x = new_location[0]
            y = new_location[1]
            # delete previous location
            Item.board[self.x][self.y].pop(self.item_type, None)
            # update Knight object
            self.x = x
            self.y = y
        if is_dead:
            # add lowercased name in map
            Item.board[self.x][self.y]["final_position"] = self.name
        else:
            if self.item_type == "item":
                if "item" in Item.board[self.x][self.y]:
                    # arrange by priority
                    items = Item.board[self.x][self.y]["item"]
                    items.append(
                        {"name": self.name, "priority": self.priority})
                    items = sorted(items, key=lambda p_key: p_key['priority'])
                else:
                    items = [{"name": self.name, "priority": self.priority}]
                Item.board[self.x][self.y]["item"] = items
            else:
                Item.board[self.x][self.y][self.item_type] = self.name
