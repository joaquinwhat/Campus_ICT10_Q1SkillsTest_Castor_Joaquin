from pyscript import document, display

def calculate_total(e):
    document.getElementById("receipt").innerHTML = ""

    item1 = document.getElementById('ting1')
    price1 = float(item1.value) * item1.checked

    item2 = document.getElementById('ting2')
    price2 = float(item2.value) * item2.checked

    item3 = document.getElementById('ting3')
    price3 = float(item3.value) * item3.checked

    item4 = document.getElementById('ting4')
    price4 = float(item4.value) * item4.checked

    subtotal = price1 + price2 + price3 + price4
    tax = subtotal * 0.12
    total = subtotal + tax

    display(f"Total w/ Tax: ₱{total:.2f}", target="receipt")