import pytest
import unittest


INTEGRATION_IS_NOT_ACTIVE = True


class TestModels(unittest.TestCase):

    @pytest.mark.skip
    def test_given_conditions_when_do_something_then_result(self):
        pass

    @pytest.mark.skipif(INTEGRATION_IS_NOT_ACTIVE, reason="integration tests conditions are not active")
    def test_given_other_conditions_when_do_something_then_result(self):
        pass
