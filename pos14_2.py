class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def display_details(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Price: ₹{self.price:.2f}")

    def apply_discount(self, percent):
        discount_amount = self.price * (percent / 100)
        self.price -= discount_amount

book1 = Book("Maths", "R.D. Sharma", 450)
book2 = Book("Physics", "H.C. Verma", 550)
book3 = Book("Chemistry", "O.P. Tandon", 400)

print("Book 1 Details:")
book1.display_details()
print("\nBook 2 Details:")
book2.display_details()
print("\nBook 3 Details:")
book3.display_details()

book2.apply_discount(10)
print("\nBook 2 Details after 10% discount:")
book2.display_details()