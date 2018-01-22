class ExceptionFilter:
    def __init__(self, threshold):
        self.threshold = threshold

    def filter_sudden_change(self, heart_rates):
        filtered_heart_rates = []
        current_heart_rate = heart_rates[0]
        for heart_rate in heart_rates:
            if (heart_rate - current_heart_rate) / current_heart_rate < self.threshold:
                filtered_heart_rates.append(heart_rate)
                current_heart_rate = heart_rate
        return filtered_heart_rates
