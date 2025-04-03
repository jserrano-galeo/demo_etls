import pytest
import unittest


INTEGRATION_IS_NOT_ACTIVE = True


class TestTasksBasic(unittest.TestCase):

    @pytest.mark.skip
    def test_given_conditions_when_run_task_then_result(self):
        pass

    @pytest.mark.skipif(INTEGRATION_IS_NOT_ACTIVE, reason="integration tests conditions are not active")
    def test_given_other_conditions_when_run_task_then_result(self):
        pass
