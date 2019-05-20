class Product:
    def __init__(self, supplier: str, name: str, price: float, available: bool):
        self.supplier = supplier
        self.name = name
        self.price = price
        self.available = available

    def to_dict(self):
        return dict(
            supplier=self.supplier,
            name=self.name,
            price=self.price,
            available=self.available
        )

    def __eq__(self, other):
        return bool(self.supplier == other.supplier and
                    self.name == other.name and
                    self.price == other.price)
