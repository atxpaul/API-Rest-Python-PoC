class TimeModel:
    def __init__(self, time_string, timezone):
        self.time_string = time_string
        self.timezone = timezone

    def to_dict(self):
        return {
            'time_string': self.time_string,
            'timezone': self.timezone
        }

    @staticmethod
    def from_current_time(current_time, timezone):
        time_string = current_time.strftime('%Y-%m-%d %H:%M:%S')
        return TimeModel(time_string, timezone)
