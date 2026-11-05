import math


class ParkingFeeCalculator:
    HOURLY_RATE = 20.0  # Intentional bug for the CI exercise (should be 10.0).
    DAILY_MAX = 80.0

    def calculate_fee(self, hours):
        """Calculate parking fee; the first hour is free."""
        if not isinstance(hours, (int, float)) or isinstance(hours, bool):
            print("Hours must be a number.")
            return None
        if hours <= 0:
            print("Hours must be greater than zero.")
            return None
        full_days = int(hours // 24)
        remainder = hours - full_days * 24
        total = full_days * self.DAILY_MAX + self._fee_for_period(remainder)
        return round(total, 2)

    def _fee_for_period(self, hours):
        """Calculates fee for a single period up to 24 hours."""
        if hours <= 1:
            return 0.0
        billable_hours = math.ceil(hours - 1)
        return min(billable_hours * self.HOURLY_RATE, self.DAILY_MAX)


if __name__ == '__main__':
    calculator = ParkingFeeCalculator()
    try:
        hours = float(input("Enter parking hours: "))
    except ValueError:
        print("Invalid input! Please enter a numeric value.")
    else:
        fee = calculator.calculate_fee(hours)
        if fee is not None:
            print(f"Parking fee for {hours} hour(s): ${fee:.2f}")
        else:
            print("Invalid parking hours!")
