
import json
from battle import Battle


def get_final_output(battle):
    """
    create an output formatted according to requirements

    Args:
        battle (Battle): Object that contains all details.

    Returns:
        dict: finale_state_format
    """
    details = {}
    # output for knights
    for knight in battle.list_knights:
        coordinates = lambda x: [x.x, x.y] if x.status != "DROWNED" else None
        item = lambda x: x.item.output_name if x.item else x.item

        details[knight.output_name] = [
            coordinates(knight),
            knight.status,
            item(knight),
            int(knight.get_enhanced_skill_score(mode="attack") - .5),
            int(knight.get_enhanced_skill_score(mode="defense"))
        ]
    # output for items
    for item in battle.list_items:
        coordinates = lambda x: [[x.owner.x, x.owner.y], True] if hasattr(x, "owner") else [
            [x.x, x.y], False]
        details[item.output_name] = coordinates(item)
    return details


def read_txt_file():
    """
    Opens moves.txt and parse it to become usable command for the knight to move.
    Returns:
        list: list of cmmands
    """
    with open("moves.txt", "r") as f:
        moves = f.read().split("\n")
    if moves[0] == 'GAME-START':
        moves.pop(0)
    if moves[-1] == 'GAME-END':
        moves.pop()
    return moves


def run():
    """
    Starts the whole process.
    Reads the moves then commands the knights to move
    """
    battle = Battle()
    print("GAME-START")
    print(battle.R.arena.get_board())
    for move in read_txt_file():
        response = battle.move(move)
        # uncoomment code below to see movements
        # print(battle.R.arena.get_board())
        if response:
            raise Exception("Invalid Move. Please check moves.txt")
    final_state = get_final_output(battle)
    with open("final_state.json", "w") as outfile:
        json.dump(final_state, outfile)
    print(battle.R.arena.get_board())
    print("GAME-END")


if __name__ == "__main__":
    run()
