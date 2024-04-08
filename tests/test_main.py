from main import call
import pytest


pytest.mark.timeout(50)
class TestMain:
    def test_call(self):
        assert call() == 'Geeks'
