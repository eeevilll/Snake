import unittest
from unittest.mock import patch, Mock


from simple_snake import start, update, finish


class TestSnakeGame(unittest.TestCase):
    
    @patch('simple_snake.pygame.display.update')
    @patch('simple_snake.pygame.time.delay')
    @patch('simple_snake.pygame.quit')
    def test_start(self, mock_quit, mock_delay, mock_update):
        start()
        mock_update.assert_called_once()
        mock_delay.assert_called_once_with(1500)
        mock_quit.assert_not_called()
        
    @patch('simple_snake.pygame.event.get', return_value=[Mock(type=0)])
    @patch('simple_snake.pygame.display.update')
    @patch('simple_snake.pygame.quit')
    def test_update_exit(self, mock_quit, mock_update, mock_get_event):
        #test case when pygame ouit //////// wissal
    
        self.assertEqual(update(), 0)
        mock_update.assert_called()
        mock_quit.assert_called_once()
        
    @patch('simple_snake.pygame.event.get', return_value=[Mock(type=1, key=Mock(key=0))])
    @patch('simple_snake.pygame.display.update')
    @patch('simple_snake.pygame.quit')
    def test_update_direction_change(self, mock_quit, mock_update, mock_get_event):
        #test case when pygame keydown //////// wissal
        self.assertEqual(update(), 0)
        mock_update.assert_called()
        mock_quit.assert_not_called()
        
    @patch('simple_snake.pygame.event.get', return_value=[Mock(type=1, key=Mock(key=0))])
    @patch('simple_snake.pygame.display.update')
    @patch('simple_snake.pygame.quit')
    def test_update_no_direction_change(self, mock_quit, mock_update, mock_get_event):
        #test same case but no direction change////wissal
        self.assertEqual(update(), 0)
        mock_update.assert_called()
        mock_quit.assert_not_called()
        
    @patch('simple_snake.pygame.event.get', return_value=[Mock(type=1, key=Mock(key=1))])
    @patch('simple_snake.pygame.display.update')
    @patch('simple_snake.pygame.quit')
    def test_update_collision(self, mock_quit, mock_update, mock_get_event):
        # test when collision /////wissal
        self.assertEqual(update(), 0)
        mock_update.assert_called()
        mock_quit.assert_called_once()
        
    @patch('simple_snake.calc_food_position', side_effect=[(0, 0), (0, 0)])
    @patch('simple_snake.pygame.event.get', return_value=[Mock(type=1, key=Mock(key=0))])
    @patch('simple_snake.pygame.display.update')
    @patch('simple_snake.pygame.quit')
    def test_update_eat_food(self, mock_quit, mock_update, mock_get_event, mock_food_position):
        # test when my snake eat food //// :)
        self.assertEqual(update(), 1)
        mock_update.assert_called()
        mock_quit.assert_not_called()
        mock_food_position.assert_called()
        
    @patch('simple_snake.pygame.time.delay')
    @patch('simple_snake.pygame.quit')
    def test_finish(self, mock_quit, mock_delay):
        finish(10)
        mock_delay.assert_called_once_with(1500)
        mock_quit.assert_called_once()


if __name__ == '__main__':
    unittest.main()