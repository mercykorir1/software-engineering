import time
from refactored_test_offline_handler import determine_sensor_status, process_sensor, ALERTS_ENABLED

def test_stale_sensor():
    last_update = time.time() - 70
    assert determine_sensor_status(last_update) == "stale"
    assert process_sensor(last_update) == "stale"

def test_fresh_sensor():
    last_update = time.time() - 30
    assert determine_sensor_status(last_update) == "online"
    assert process_sensor(last_update) == "online"

def test_alerts_disabled():
    global ALERTS_ENABLED
    ALERTS_ENABLED = False
    last_update = time.time() - 100
    assert determine_sensor_status(last_update) == "disabled"
    ALERTS_ENABLED = True
