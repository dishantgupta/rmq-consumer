from config.log import LoggingConfiguration
from config.settings import settings
from rabbitmq.gs_flag_consumer import GsFlagRmqConsumer
from services.product_transformation_result import gs_logic


def test__gs_logic():
    # sample prod fixture ids
    _env = settings.env
    LoggingConfiguration.initialize_logger()
    message = "GS LOGIC TEST CASE FAILED"
    print ("*"*100, "Running Test Cases", "*"*100)
    if _env == "stage":
        assert gs_logic("1021985318", 550000) == 0, message
        assert gs_logic("1028525411", 550000) == 0, message
    else:
        assert gs_logic("1152388959", 290000) == 0, message
        assert gs_logic("1060545354", 525000) == 0, message
    print("*" * 100, "Test Cases Execution Successful", "*" * 100)


if __name__ == "__main__":
    test__gs_logic()
    LoggingConfiguration.initialize_logger()
    consumer = GsFlagRmqConsumer()
    consumer.consume()


# CREATE TABLE ABC_gs_flag (id INT AUTO_INCREMENT,fixture_id INT NOT NULL,gs_flag INT NOT NULL DEFAULT 0,
# timestamp TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP, PRIMARY KEY ( id ), KEY(fixture_id));


# ALTER TABLE ABC_gs_flag ADD extra_data JSON;
