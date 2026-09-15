from pyscript import display, document

def calculate_total(event):
    selected_items = document.querySelectorAll('input[type="checkbox"]')
    total_sum = 0
    receipt = "Receipt: "

    for item in selected_items:
        if item.checked:
            total_sum += float(item.value)
            receipt += f"{item.id}: ₱{item.value}\n"

    tax = total_sum * 0.12
    total_sum += tax        

    receipt += f"Total w/ Tax: ₱{total_sum}"
    display(receipt, target="receipt")