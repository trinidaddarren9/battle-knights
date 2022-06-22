from item import Item


class Knight(Item):
    """
    Handles all of knights methods.

    Args:
        Item (object): Inherit from Item class
    """

    def __init__(
        self, name: str, x: int, y: int, item_type: str, output_name: str, defense: int = 1,
        attack: int = 1, status: str = "LIVE"
    ):
        """
        Initialize Knight
        Args:
            name (str): name.
            x (int): x coordinate.
            y (int): y coordinate.
            item_type (str): item | knight.
            output_name (str): fullname.
            defense (int, optional): base defense value. Defaults to 1.
            attack (int, optional): base attack value. Defaults to 1.
            status (str, optional): DEAD | LIVE. Defaults to "LIVE".
        """

        super().__init__(name, x, y, attack, defense, status, item_type, output_name)
        self.item = None
        self.is_dead = False
        self.final_position = []

    def dead(self, cause="DEAD"):
        """
        Declare knight as dead. Drop item in last valid cell. 
        Args:
            cause (str, optional): DEAD | DROWNED. Defaults to "DEAD".
        """
        self.is_dead = True
        self.status = cause
        self.name = self.name.lower()
        self.attack = 0
        self.defense = 0
        if cause == "DEAD":
            self.final_position = [self.x, self.y]
        else:
            self.final_position = None
        # drop item
        if self.item:
            delattr(self.item, "owner")
            self.item.update_position_on_map(new_location=[self.x, self.y])
            self.item = None
        self.update_position_on_map(
            new_location=[self.x, self.y], is_dead=True)

    def add_item(self, item: Item):
        """
        Equip item to a Knight.
        Args:
            item (Item): Item object to be equipped to a Knight.
        """
        # check if no item
        # do nothing if already have an item
        if not self.item:
            self.item = item
            self.item.owner = self
            # remove item on item list
            items = Knight.board[item.x][item.y]["item"]
            if len(items) == 1:
                # delete whole item key if item list
                Knight.board[item.x][item.y].pop("item", None)
            else:
                Knight.board[item.x][item.y]["item"].pop(0)

    def get_enhanced_skill_score(self, mode: str):
        """
        Computes for the total attack and defense score of a Knight.
        Args:
            mode (str): ATTACK | DEFENSE

        Returns:
            _type_: Total attack or defense score
        """
        extra = 0
        if mode == "defense":
            if self.item:
                extra += self.item.defense
            return self.defense + extra
        elif mode == "attack":
            if self.item:
                extra += self.item.attack
            return self.defense + extra + .5
