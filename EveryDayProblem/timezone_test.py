from datetime import datetime, timedelta
from zoneinfo import ZoneInfo

def get_previous_hour_est(format_str="%Y-%m-%d %H:%M:%S"):
    try:
        est_tz = ZoneInfo("America/New_York")  # EST timezone with daylight saving handling
        now_est = datetime.now(est_tz)
        prev_hour = now_est.replace(minute=0, second=0, microsecond=0) - timedelta(hours=1)
        return prev_hour.strftime(format_str)
    except Exception as e:
        print(f"Error getting previous hour in EST: {e}")
        return None

# Example usage
print(get_previous_hour_est())
