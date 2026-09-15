from pyscript import document, display

def calculate_total(e):
    sub = (
        float(document.getElementById('Burger').value) * document.getElementById('Burger').checked +
        float(document.getElementById('Fries').value) * document.getElementById('Fries').checked +
        float(document.getElementById('Drink').value) * document.getElementById('Drink').checked +
        float(document.getElementById('Dessert').value) * document.getElementById('Dessert').checked
    )
    
    total = sub * 1.1
    display(f"Total w/ Tax: ₱{total:.2f}", target="receipt")