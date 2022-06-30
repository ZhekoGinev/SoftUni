class Catalogue:
    def __init__(self, name: str) -> None:
        self.name = name
        self.products = []

    def add_product(self, product_name: str):
        self.products.append(product_name)

    def get_by_letter(self, first_letter: str):
        return [p for p in self.products if p[0].lower() == first_letter.lower()]

    def __repr__(self) -> str:
        result = f"Items in the {self.name} catalogue:\n"
        result += "\n".join(sorted(self.products))
        return result
