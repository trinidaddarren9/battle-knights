from item import Item
from knight import Knight


class Battle:
    """
    Handles all battle events. This is where knights pickup items and fight each other.
    """

    def __init__(self):
        """
        Initialize Battle.
        """
        self.R = Knight(
            name="R",
            x=0,
            y=0,
            item_type="knight",
            output_name="red"
        )
        self.B = Knight(
            name="B",
            x=7,
            y=0,
            item_type="knight",
            output_name="blue"
        )
        self.Y = Knight(
            name="Y",
            x=0,
            y=7,
            item_type="knight",
            output_name="yellow"
        )
        self.G = Knight(
            name="G",
            x=7,
            y=7,
            item_type="knight",
            output_name="green"
        )

        self.A = Item(
            name="A",
            x=2,
            y=2,
            attack=2,
            defense=0,
            status="NOT EQUIPPED",
            item_type="item",
            priority=0,
            output_name="axe"
        )
        self.D = Item(
            name="D",
            x=2,
            y=5,
            attack=1,
            defense=0,
            status="NOT EQUIPPED",
            item_type="item",
            priority=3,
            output_name="dagger"
        )
        self.H = Item(
            name="H",
            x=5,
            y=5,
            attack=0,
            defense=1,
            status="NOT EQUIPPED",
            item_type="item",
            priority=4,
            output_name="helmet"
        )
        self.M = Item(
            name="M",
            x=5,
            y=2,
            attack=1,
            defense=1,
            status="NOT EQUIPPED",
            item_type="item",
            priority=1,
            output_name="magic_staff"
        )
        self.list_knights = [self.R, self.B, self.G, self.Y]
        self.list_items = [self.M, self.H, self.A, self.D]

    def move(self, command: str):
        """
        Moves the soldier from one cell to another. Pickup items if there are items in the cell
        then attack if there are knights.
        Args:
            command (str): format is <Knight>:<Direction>.
        """
        try:
            knight = getattr(self, command[0])
            x = knight.x
            y = knight.y
            direction = command[2]

            if direction == "N":
                x -= 1
            elif direction == "S":
                x += 1
            elif direction == "E":
                y += 1
            elif direction == "W":
                y -= 1
        except Exception as error:
            return "INVALID MOVE"

        # check if not dead
        # print(f"{knight.name} : x={x}, y={y}")
        if not knight.is_dead:
            # check if drowned

            if x <= 7 and x >= 0 and y <= 7 and y >= 0:
                # valid location
                pos = Knight.arena.board[x][y]
                # check for knight in future cell
                if "knight" in pos:
                    # fight
                    attacker_attack = knight.get_enhanced_skill_score(
                        mode="attack")
                    # get defender knight
                    defender = getattr(self, pos["knight"])
                    defender_defense = defender.get_enhanced_skill_score(
                        mode="defense")
                    # print(
                    #     f"fight {knight.name} : {attacker_attack},{defender.name}:{defender_defense}")
                    if attacker_attack > defender_defense:
                        # when attacker is higher
                        # winner attacker
                        # print(defender.x, defender.y)
                        defender.dead(cause="DEAD")

                    else:
                        # when defender is higher
                        # winner defender
                        knight.dead(cause="DEAD")
                        knight = defender
                # check for item
                if "item" in pos:
                    item = getattr(self, pos["item"][0]["name"])
                    knight.add_item(item)
                knight.update_position_on_map([x, y])
            else:
                # drowned
                knight.final_position = None
                knight.dead(cause="DROWNED")
        # print(Knight.arena.get_board())
