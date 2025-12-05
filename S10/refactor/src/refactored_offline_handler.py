import time
ALERTS_ENABLED = True

def is_sensor_stale(last_update_time, threshold_seconds=60):
    """Check if the sensor data is older than threshold."""
    return (time.time() - last_update_time) > threshold_seconds

def determine_sensor_status(last_update_time):
    """
    Core logic: decide status without printing/logging.
    Returns "stale", "online", or "disabled".
    """
    if not ALERTS_ENABLED:
        return "disabled"
    if is_sensor_stale(last_update_time):
        return "stale"
    return "online"

def log_sensor_status(status):
    """Side effect: print metric if sensor is stale."""
    if status == "stale":
        print("Metric: offline_alerts_sent=1")
    elif status == "disabled":
        print("Feature disabled - rollback mode")

def process_sensor(last_update_time):
    """Combine logic and logging in a safe, readable way."""
    status = determine_sensor_status(last_update_time)
    log_sensor_status(status)
    return status
