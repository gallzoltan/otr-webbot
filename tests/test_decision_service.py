import pytest
from otr_bot.services.decision_service import DecisionService

@pytest.fixture
def service():
  return DecisionService(browser=None)

def test_split_by_dots(service):
  s = "4.1.1.; 9.2.; 9.4.;18."
  # cat_list = [x.strip() for x in s.split(";") if x.strip()]
  assert service._split_by_dots('4.1.1.') == ('4.', '4.1.', '4.1.1.')
  assert service._split_by_dots('9.2.') == ('9.', '9.2.')
  assert service._split_by_dots('9.4.') == ('9.', '9.4.')
  assert service._split_by_dots('18.') == ('18.',)