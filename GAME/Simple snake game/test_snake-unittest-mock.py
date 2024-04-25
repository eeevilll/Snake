#hey miss eye , i wish read this i m so thankful for being understanding  me and tried to help me well so i retry to do my best in this homework and thanks
from unittest.mock import patch
import pytest
import simple_snake

@pytest.fixture
def mock_update(request):
    with patch('pygame.display.update') as mock_update:
        yield mock_update
        #this miss for explain wht and how and why i do this test :
#What
#This fixture is used for mocking the pygame.display.update function. When tests run instead of executing the actual pygame.display.update function, 
#it will execute a mock object created by unittest.mock.
#How: 
#This is achieved by using the patch context manager, which temporarily replaces the specified function (pygame.display.update) with a mock object.
#Why: This mocking is useful in unit testing, especially when you want to isolate the behavior of a specific function 
#(pygame.display.update in this case) without actually executing its real implementation.
#It allows you to control the behavior of this function within your test environment, making it easier to write focused and deterministic tests.


@pytest.fixture
def mock_calc_food_position(request):
    with patch('simple_snake.calc_food_position') as mock_calc_food_position:
        yield mock_calc_food_position
#What: Similar to the previous fixture, this fixture is used to mock a specific function (simple_snake.calc_food_position) during tests.
#How: It achieves this by utilizing the patch context manager, which temporarily replaces the specified function with a mock object.
#Why: Mocking this function allows for controlled testing of code that depends on simple_snake.calc_food_position. By replacing the actual implementation with a mock object, 
#tests can observe and verify the behavior of the surrounding code in isolation, 
#without relying on the real implementation of calc_food_position.


@pytest.fixture
def mock_event_get(request):
    with patch('pygame.event.get') as mock_event_get:
        yield mock_event_get

#What: Similarly, this fixture is used to mock a specific function (pygame.event.get) during tests.
#How: It uses the patch context manager to temporarily replace the specified function with a mock object.
#Why: By mocking pygame.event.get, tests can control and observe the behavior of code that relies on this function without executing its real implementation. 
#This facilitates isolated and focused testing.

def test_update_exception(mock_event_get):
    mock_event_get.side_effect = Exception('Test Exception')
    with pytest.raises(Exception) as excinfo:
        simple_snake.update()
    assert 'Test Exception' in str(excinfo.value)

#What: This test case verifies that simple_snake.update() correctly handles an exception raised by pygame.event.get.
#How: It sets up the mock object to raise an exception when called, then calls simple_snake.update() within a context where it expects an exception to be raised, 
#and finally checks if the raised exception contains the expected message.
#Why: This test ensures that the update function gracefully handles exceptions from its dependencies, ensuring robustness and reliability of the code.


                       #mock_test-passed
#---------------------------------------------------------------------------------
#$ pytest test.py
#============================= test session starts ==============================
#platform linux -- Python 3.10.12, pytest-8.1.1, pluggy-1.4.0
#rootdir: /home/wissal/Documents/Django PROJECT/Project/Snake/Snake/GAME/Simple snake game
#collected 1 item                                                               

#test.py .                                                                [100%]

#============================== 1 passed in 14.79s =============================
#---------------------------------------------------------------------------------





#thank you very much    wissal yahia
