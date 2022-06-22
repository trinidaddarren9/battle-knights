import unittest

# from item import Item
from battle import Battle
from item import Item


class TestCase(unittest.TestCase):
    def setUp(self):
        self.battle = Battle()
        self.R = self.battle.R
        self.G = self.battle.G
        self.B = self.battle.B
        self.Y = self.battle.Y
        self.A = self.battle.A
        self.M = self.battle.M
        self.D = self.battle.D
        self.H = self.battle.H

    def tearDown(self) -> None:
        Item.reset_board()

    def testKnightMoves(self):
        self.battle.move(command="R:S")
        self.battle.move(command="R:S")
        self.battle.move(command="R:E")
        self.assertEqual(self.R.x, 2)
        self.assertEqual(self.R.y, 1)

    def testKnightGetItem(self):
        self.battle.move(command="R:S")
        self.battle.move(command="R:S")
        self.battle.move(command="R:E")
        self.battle.move(command="R:E")
        item = self.R.item
        self.assertEqual(item.name, "A")
        self.assertEqual(item.attack, 2)
        self.assertEqual(item.defense, 0)

    def testKnightDrown(self):
        self.battle.move(command="R:N")
        self.battle.move(command="Y:E")
        self.battle.move(command="B:W")
        self.battle.move(command="G:S")
        self.assertEqual(self.R.status, "DROWNED")
        self.assertEqual(self.G.status, "DROWNED")
        self.assertEqual(self.B.status, "DROWNED")
        self.assertEqual(self.Y.status, "DROWNED")

    def testKnightBattle(self):
        self.battle.move(command="R:S")
        self.battle.move(command="R:S")
        self.battle.move(command="R:S")
        self.battle.move(command="R:S")
        self.battle.move(command="R:S")
        self.battle.move(command="R:S")
        self.battle.move(command="R:S")
        self.assertEqual(self.R.status, "LIVE")
        self.assertEqual(self.B.status, "DEAD")

    def testKnightInvalidMove(self):
        self.assertEqual(self.battle.move(command="r:1"), "INVALID MOVE")
        self.assertEqual(self.battle.R.x, 0)
        self.assertEqual(self.battle.R.y, 0)


if __name__ == '__main__':
    unittest.main(verbosity=2)
