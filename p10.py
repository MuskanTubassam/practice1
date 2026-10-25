
class Inventory:
    def __init__(self):
        self.items = {}

    def add_item(self, name, qty, price):
        self.items[name] = (qty, price)

    def remove_item(self, name):
        if name not in self.items:
            raise KeyError(f"No item named {name}")
        del self.items[name]

    def total_value(self):
        total = 0
        for qty, price in self.items.values():
            total += qty * price
        return total

    def __len__(self):
        return len(self.items)

    def save_report(self, filename):
        with open(filename, "w") as file:
            for name, (qty, price) in self.items.items():
                file.write(f"{name}: quantity={qty}, price={price}\n")
            file.write(f"Total value: {self.total_value()}\n")


inventory = Inventory()

try:
    with open("stock.txt", "r") as file:
        for line in file:
            name = "unknown"
            try:
                name, qty, price = line.strip().split(",")
                qty = int(qty)
                price = int(price)
                inventory.add_item(name, qty, price)
            except ValueError:
                print(f"Skipping {name}: bad number")

except FileNotFoundError:
    print("Error: stock.txt file not found")
    raise SystemExit

print(f"{len(inventory)} items, total value {inventory.total_value()}")

inventory.remove_item("pen")
print(f"{len(inventory)} items, total value {inventory.total_value()}")

try:
    inventory.remove_item("laptop")
except KeyError as e:
    print(f"Error: {e}")
