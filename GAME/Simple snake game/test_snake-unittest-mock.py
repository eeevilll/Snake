from unittest.mock import patch
import pytest
import simple_snake

@pytest.fixture
def mock_update(request):
    with patch('pygame.display.update') as mock_update:
        yield mock_update


@pytest.fixture
def mock_calc_food_position(request):
    with patch('simple_snake.calc_food_position') as mock_calc_food_position:
        yield mock_calc_food_position



@pytest.fixture
def mock_event_get(request):
    with patch('pygame.event.get') as mock_event_get:
        yield mock_event_get

def test_update_exception(mock_event_get):
    mock_event_get.side_effect = Exception('Test Exception')
    with pytest.raises(Exception) as excinfo:
        simple_snake.update()
    assert 'Test Exception' in str(excinfo.value)
