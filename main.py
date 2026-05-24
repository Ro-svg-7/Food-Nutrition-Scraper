import tkinter as tk

root = tk.Tk()
root.geometry("650x550")
root.title("Food Nutrition Srcaper")
root.configure(bg="#5DF2A7")

status_text = tk.StringVar()
status_text.set("Waiting for the food...")

def get_metrics():

    calories_label.config(text="Calories: 23")
    protein_label.config(text="Protein: 1g")
    fat_label.config(text="Fat: 2g")
    carbs_label.config(text="Carbohydrates: 21g")

title_label = tk.Label(
    root,
    text="Food Nutrition Scraper",
    font=("Arial", 24, "bold"),
    bg="#5DF2A7",
    fg="white"
)
title_label.pack(pady=(15,25))

input_frame = tk.Frame(
    root,
    bg="#5DF2A7"
)
input_frame.pack(pady=10)
food_label = tk.Label(
    input_frame,
    text="Food Item:",
    font=("Arial", 14, "bold"),
    bg="#5DF2A7",
    fg="black"
)
food_label.pack(side="left",padx=10)

food_name = tk.Entry(
    input_frame,
    font=("Arial", 14, "italic"),
    bg="#F2AFD4",
    fg="black",
    bd=2,
    relief="groove",
    justify="center"
)
food_name.pack(side="left")

search_button = tk.Button(
    root,
    text="Search",
    font=("Arial", 14, "bold"),
    bg="#63DF10",
    fg="white",
    command=get_metrics
)
search_button.pack(pady=10)

status_label = tk.Label(
    root,
    textvariable=status_text,
    font=("Arial", 14, "bold"),
    bg="#5DF2A7",
    fg="#E9F108"
)
status_label.pack(pady=(20,25))

metrics_frame = tk.Frame(
    root,
    bg="#5DF2A7"
)
metrics_frame.pack(anchor="w", padx=100, pady=10)

calories_label = tk.Label(
    metrics_frame,
    text = "Calories: --",
    font=("Arial", 14),
    bg="#9ABBE9",
    fg="black"
)
calories_label.pack(anchor="w", pady=10)

protein_label = tk.Label(
    metrics_frame,
    text="Protien: --",
    font=("Arial", 14),
    bg="#9ABBE9",
    fg="black"
)
protein_label.pack(anchor="w", pady=10)

carbs_label = tk.Label(
    metrics_frame,
    text="Carbohydrate: --",
    font=("Arial", 14),
    bg="#9ABBE9",
    fg="black"
)
carbs_label.pack(anchor="w", pady=10)

fat_label = tk.Label(
    metrics_frame,
    text="Fat: --",
    font=("Arial", 14),
    bg="#9ABBE9",
    fg="black"
)
fat_label.pack(anchor="w", pady=10)

root.mainloop()