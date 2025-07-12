import tkinter as tk
import random

# Val som spelaren och datorn kan göra
CHOICES = ["sten", "sax", "påse"]

# Slumpa datorns val
def get_computer_choice():
    return random.choice(CHOICES)

# Avgör vinnaren
def determine_winner(player, computer):
    if player == computer:
        return "Oavgjort! Försök igen."
    elif (player == "sten" and computer == "sax") or \
         (player == "sax" and computer == "påse") or \
         (player == "påse" and computer == "sten"):
        return "Du vann! 🎉"
    else:
        return "Du förlorade! 😢"

# När spelaren gör ett val
def play(choice):
    computer_choice = get_computer_choice()
    result = determine_winner(choice, computer_choice)
    result_label.config(
        text=f"Du valde: {choice}\nDatorn valde: {computer_choice}\n\n{result}"
    )

    # Ändra färg beroende på resultat
    if "vann" in result:
        result_label.config(bg="#d4edda", fg="#155724")  # Grön bakgrund
    elif "förlorade" in result:
        result_label.config(bg="#f8d7da", fg="#721c24")  # Röd bakgrund
    else:
        result_label.config(bg="#fff3cd", fg="#856404")  # Gul bakgrund

    # Om spelet är klart, inaktivera knapparna
    if "vann" in result or "förlorade" in result:
        disable_buttons()

# Inaktivera alla valknappar
def disable_buttons():
    for button in buttons:
        button.config(state="disabled")

# Starta om spelet
def reset_game():
    result_label.config(text="Välj sten, sax eller påse för att börja.",
                        bg="#f0f0f0", fg="black")
    for button in buttons:
        button.config(state="normal")

# Skapa huvudfönstret
root = tk.Tk()
root.title("Sten Sax Påse")
root.geometry("400x400")
root.configure(bg="#e6f2ff")  # Ljusblå bakgrund

# Yttre ram
frame = tk.Frame(root, bg="#e6f2ff", padx=20, pady=20)
frame.pack(expand=True)

# Titel
title_label = tk.Label(frame, text="🪨✂️📄  Sten - Sax - Påse", font=("Helvetica", 20, "bold"), bg="#e6f2ff", fg="#003366")
title_label.pack(pady=10)

# Resultatetikett
result_label = tk.Label(frame, text="Välj sten, sax eller påse för att börja.", font=("Helvetica", 14), width=40, height=6, bg="#f0f0f0", relief="sunken", wraplength=300)
result_label.pack(pady=10)

# Skapa knappar för val
buttons = []
colors = {"sten": "#a3c9a8", "sax": "#f4d35e", "påse": "#ee6c4d"}
for choice in CHOICES:
    btn = tk.Button(frame,
                    text=choice.capitalize(),
                    font=("Helvetica", 14),
                    width=12,
                    bg=colors[choice],
                    activebackground="white",
                    command=lambda c=choice: play(c))
    btn.pack(pady=5)
    buttons.append(btn)

# Reset-knapp
reset_button = tk.Button(frame, text="🔁 Spela igen", font=("Helvetica", 12), bg="#cccccc", command=reset_game)
reset_button.pack(pady=10)

# Starta GUI
root.mainloop()
