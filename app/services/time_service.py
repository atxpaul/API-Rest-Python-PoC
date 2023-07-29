from datetime import datetime
from app.models.time_model import TimeModel


def get_current_time():
    current_time = datetime.now()
    timezone = 'UTC'
    return TimeModel.from_current_time(current_time, timezone)
