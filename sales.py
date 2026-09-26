class WeeklySales:
    def __init__(self):
        """Take input first, then store it"""
        self.sales = []
        days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

        print("Enter sales for each day:")
        for day in days:
            sale = float(input(f"{day}: "))
            self.sales.append(sale)

    def average_sales(self):
        """Calculate average sales for the week."""
        return sum(self.sales) / len(self.sales)

    def predict_next_week(self):
        """Predict sales for the next week."""
        avg = self.average_sales()
        return [round(avg, 2) for _ in range(7)]


# THIS PART RUNS THE CODE
if __name__ == "__main__":
    weekly = WeeklySales()

    print("\n--- Results ---")
    print("Your sales:", weekly.sales)
    print("Average sales:", round(weekly.average_sales(), 2))
    print("Predicted next week:", weekly.predict_next_week())