import pytest
from otr_bot.services.decision_service import DecisionService

@pytest.fixture
def service():
  return DecisionService(browser=None)

@pytest.mark.parametrize("cat_list, expected_result", [
  ("4.1.1.", ('4.', '4.1.', '4.1.1.')),
  ("9.2.", ('9.', '9.2.')),
  ("9.4.", ('9.', '9.4.')),
  ("18.", ('18.',)),
])

def test_split_by_dots(service, cat_list, expected_result):
  '''
    Test the _split_by_dots() method
    s = "4.1.1.; 9.2.; 9.4.;18."
  '''
  assert service._split_by_dots(cat_list) == expected_result  