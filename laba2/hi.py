import unittest
from unittest.mock import Mock
from TowerDefense import Monster
money = 0
health = 100
class TestMonster(unittest.TestCase):
    def test_update_method(self):
        mock_monster = Mock(spec=Monster)
        mock_monster.health = 10
        mock_monster.move = Mock()
        mock_monster.killed = Mock()
        mock_monster.update()
        mock_monster.killed.assert_not_called()

    def test_die_method(self):
        mock_monster = Mock(spec=Monster)
        mock_monster.alive = True
        mock_monster.value = 5
        global money
        mock_monster.die()
        self.assertTrue(mock_monster.alive)
        self.assertEqual(money, 5)