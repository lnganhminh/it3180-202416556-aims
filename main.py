"""Ví dụ chạy AIMS-mini với một giỏ ba DVD."""
from aims.cart import Cart
from aims.dvd import DigitalVideoDisc

def create_demo_cart():
    records = (
        ("The Lion King", "Animation", "Roger Allers", 88, 19.95),
        ("Howl's Moving Castle", "Animation", "Hayao Miyazaki", 119, 24.99),
        ("Interstellar", "Science fiction", "Christopher Nolan", 169, 18.95),
    )
    cart = Cart()
    for record in records:
        cart.add_digital_video_disc(DigitalVideoDisc(*record))
    return cart

def main():
    cart = create_demo_cart()
    cart.print_cart()

if __name__ == "__main__":
    main()
