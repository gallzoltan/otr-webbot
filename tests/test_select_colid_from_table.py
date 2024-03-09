import otr_bot as bot
from otr_bot.models.search_table import SupportSearchTable

def test_get_cell_id():
    browser = None
    service = bot.services.SupportListService(browser)
    collist = [
        {"id": "0", "title": "title"},
        {"id": "1", "title": "support_name"},
        {"id": "2", "title": "Benyújtott"},
        {"id": "3", "title": "decision_date"},
        {"id": "4", "title": "Békéscsaba Megyei Jogú Város Önkormányzata"},
        {"id": "5", "title": "constuct_name"},
        {"id": "6", "title": "exclusion"},
        {"id": "7", "title": "title7"},
        {"id": "id1234", "title": "clickId"}
    ]
    rowlist = []
    rowlist.append(SupportSearchTable(collist=collist))
    assert service._getClickId(rows=rowlist, council="Békéscsaba", status="Benyújtott") == "id1234"