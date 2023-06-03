import unittest
from unittest.mock import MagicMock
from game import Game
from TowerDefense import TowerDefenseGame, TowerDefenseGameState
from TowerDefense import MyButton

money = 100
displayTower = None


class MyButtonTestCase(unittest.TestCase):
    def setUp(self):
        self.button = MyButton(100, 100, 200, 200)  # Create a MyButton instance for testing

    def test_checkPress_with_click_inside_button(self):
        self.assertTrue(self.button.checkPress(True, 150, 150))

    def test_checkPress_with_click_outside_button(self):
        self.assertFalse(self.button.checkPress(True, 300, 300))

    def test_pressed(self):
        # Test the pressed method of MyButton (to be overridden in derived classes)
        self.assertIsNone(self.button.pressed())

    def test_paint(self):
        canvas_mock = MagicMock()  # Create a MagicMock object for the canvas
        self.button.paint(canvas_mock)
        canvas_mock.create_rectangle.assert_called_with(
            100, 100, 200, 200, fill="red", outline="black"
        )


class TestTowerDefenseGame(unittest.TestCase):

    def setUp(self):
        self.game = TowerDefenseGame()

    def test_game_inherits_from_game_class(self):
        self.assertIsInstance(self.game, Game)

    def test_game_initial_state_is_idle(self):
        self.assertEqual(self.game.state, TowerDefenseGameState.IDLE)

    def test_game_can_set_state_to_spawning(self):
        self.game.set_state(TowerDefenseGameState.SPAWNING)
        self.assertEqual(self.game.state, TowerDefenseGameState.SPAWNING)

    def test_game_can_set_state_to_wait_for_spawn(self):
        self.game.set_state(TowerDefenseGameState.WAIT_FOR_SPAWN)
        self.assertEqual(self.game.state, TowerDefenseGameState.WAIT_FOR_SPAWN)







