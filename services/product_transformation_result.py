from config.log import LoggingConfiguration
from db.gs_flag_query_executer import GsFlagQueryExecutor
from services.inspection_record_fetcher import InspectionRecordFetcher


def some_logic(a, b):
    return True


def get_fixture_data(inspection_record, target_price):
    data = dict()
    return data


def set_gs_flag(fixture_id, target_price):
    logger = LoggingConfiguration.get_default_logger()
    logger.info("target_price: {}, fixture_id: {}".format(target_price, fixture_id))
    if target_price and fixture_id:
        inspection_record = InspectionRecordFetcher.fetch(fixture_id)
        if inspection_record:
            inspection_record = inspection_record[0]
            gs_flag = some_logic(inspection_record, target_price)
            GsFlagQueryExecutor.set_flag(gs_flag, get_fixture_data(inspection_record, target_price))
            return gs_flag
    return 0


def gs_logic(fixture_id, target_price):
    inspection_record = InspectionRecordFetcher.fetch(fixture_id)
    if inspection_record:
        inspection_record = inspection_record[0]
        gs_flag = some_logic(inspection_record, target_price)
        return gs_flag
    raise AssertionError("no inspection record found")
