import unittest
from unittest.mock import patch
import random
import pygame
from simple_snake import calc_food_position, check_collisions, update

class TestSnakeGame(unittest.TestCase):


    @patch('random.randrange')
    def test_calc_food_position(self, mock_randrange):
      
        mock_randrange.side_effect = [10, 20]
        
     
        position = calc_food_position(bias=(10, 10))
        
   
        expected_position = (10, 20)
        self.assertEqual(position, expected_position)

    def test_check_collisions(self):
 
        mock_snake = [[10, 20], [10, 30], [20, 30], [30, 30]]
        

        self.assertFalse(check_collisions(mock_snake))

        mock_snake.append([10, 20])

        self.assertTrue(check_collisions(mock_snake))

    @patch('simple_snake.quit')
    def test_update(self, mock_quit):

        with patch('simple_snake.calc_food_position') as mock_calc_food_position:
            mock_calc_food_position.return_value = (50, 50)

            score = update()

            self.assertEqual(score, 0)

if __name__ == '__main__':
    unittest.main()
