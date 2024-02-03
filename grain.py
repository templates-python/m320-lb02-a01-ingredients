class Grain:
    def __str__(self):
        """
        string representation of a grain
        """
        return f"Grain(name='{self.name}', price={self.price}, allergen='{self.allergen}')"
