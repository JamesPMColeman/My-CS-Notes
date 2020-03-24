from unittest import skipIf
from unittest.mock import Mock, patch
from mocking_practice.constants import SKIP_REAL
from nose.tools import assert_list_equal, assert_true, assert_is_none
from mocking_practice.services import get_uncompleted_todos, get_todos


class TestTodos(object):
    @classmethod
    def setup_class(cls):
        cls.mock_get_patcher = patch('mocking_practice.services.requests.get')
        cls.mock_get = cls.mock_get_patcher.start()

    @classmethod
    def teardown_class(cls):
        cls.mock_get_patcher.stop()

    def test_getting_todos_when_response_is_ok(self):
        # Configure the mock to return a response with an OK status code.
        self.mock_get.return_value.ok = True

        todos = [{
            'userId': 1,
            'id': 1,
            'title': 'Make the bed',
            'completed': False
        }]

        self.mock_get.return_value = Mock()
        self.mock_get.return_value.json.return_value = todos

        # Call the service, which will send a request to the server.
        response = get_todos()

        # If the request is sent successfully, then I expect a response to be returned.
        assert_list_equal(response.json(), todos)

    def test_getting_todos_when_response_is_not_ok(self):
        # Tell the mock to return not ok for return_value
        self.mock_get.return_value.ok = False

        # Call service. Service will send a request to the server
        response = get_todos()

        # If the request is sent unsuccessfully expect response to be None
        assert_is_none(response)


class TestUncompletedTodos(object):
    @classmethod
    def setup_class(cls):
        cls.mock_get_todos_patcher = patch('mocking_practice.services.get_todos')
        cls.mock_get_todos = cls.mock_get_todos_patcher.start()

    @classmethod
    def teardown_class(cls):
        cls.mock_get_todos_patcher.stop()

    def test_getting_uncompleted_todos_when_response_is_not_none(self):
        """ Unit test for mocking_practice.services.get_todos()'
        * should get a list if return value is ok
        """
        todo1 = {
            'userId': 1,
            'id': 1,
            'title': 'Make the bed',
            'completed': False
        }
        todo2 = {'userId': 1,
                 'id': 2,
                 'title': 'Walk the dog',
                 'completed': True
                 }

        # The Mock is told to return OK as it takes the .get() methods place
        # todos = the .json return_value
        self.mock_get_todos.return_value = Mock()
        self.mock_get_todos.return_value.json.return_value = [todo1, todo2]

        # Call service. Service will retrieve a list of false completed todos
        uncompleted_todos = get_uncompleted_todos()

        # Confirm that the mock was called
        assert_true(self.mock_get_todos.called)

        # Confirm that todos where filtered by completeness (incompleteness)
        assert_list_equal(uncompleted_todos, [todo1])

    def test_getting_uncompleted_todos_when_todos_is_none(self):
        # Tell the mock to return not ok for return_value
        self.mock_get_todos.return_value = None

        # Call the service, which will return an empty list
        uncompleted_todos = get_uncompleted_todos()

        # Confirm that the mock was called
        assert_true(self.mock_get_todos.called)

        # Confirm an empty list was returned
        assert_list_equal(uncompleted_todos, [])


@skipIf(SKIP_REAL, 'Skipping tests that hit the real API server')
def test_integration_contract():
    """ Unit test that checks the typ of data being retreived by
    mocking_proactice.services.update_todos.request.get
    """
    # Get the actual API
    actual = get_todos()
    actual_keys = actual.json().pop().keys()

    # Get the mocked API
    with patch('mocking_practice.services.requests.get') as mock_get:
        mock_get.return_value.ok = True
        mock_get.return_value.json.return_value = [{
            'userId': 1,
            'id': 1,
            'title': 'Make the bed',
            'completed': False
        }]

        mocked = get_todos()
        mocked_keys = mocked.json().pop().keys()

    # An object from the actual API and an object from the mocked API
    # should have the same data structure
    assert_list_equal(list(actual_keys), list(mocked_keys))