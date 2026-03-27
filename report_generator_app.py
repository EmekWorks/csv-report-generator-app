import csv
import os
import tkinter as tk
from tkinter import filedialog, messagebox

def choose_file():
    file_path = filedialog.askopenfilename(
        filetypes=[("CSV files", "*.csv")]
    )
    selected_file.set(file_path)

def generate_report():
    file_path = selected_file.get()

    if not file_path:
        messagebox.showerror("Error", "Choose a CSV file first.")
        return

    if not os.path.exists(file_path):
        messagebox.showerror("Error", "Selected file does not exist.")
        return

    total_rows = 0
    total_revenue = 0
    total_price = 0

    try:
        with open(file_path, "r", encoding="utf-8-sig") as file:
            reader = csv.DictReader(file)

            for row in reader:
                price = float(row["price"])
                quantity = int(row["quantity"])

                total_rows += 1
                total_revenue += price * quantity
                total_price += price

        average_price = total_price / total_rows if total_rows > 0 else 0

        report_text = (
            f"CSV REPORT\n"
            f"----------------------\n"
            f"Number of rows: {total_rows}\n"
            f"Total revenue: {total_revenue}\n"
            f"Average price: {average_price:.2f}\n"
        )

        with open("report.txt", "w", encoding="utf-8") as report_file:
            report_file.write(report_text)

        messagebox.showinfo("Done", "Report saved to report.txt")

    except Exception as e:
        messagebox.showerror("Error", f"Something went wrong:\n{e}")

root = tk.Tk()
root.title("CSV Report Generator App")
root.geometry("450x220")

selected_file = tk.StringVar()

title_label = tk.Label(root, text="CSV Report Generator App", font=("Arial", 16, "bold"))
title_label.pack(pady=15)

file_label = tk.Label(root, text="Choose CSV file")
file_label.pack()

file_entry = tk.Entry(root, textvariable=selected_file, width=48)
file_entry.pack(pady=5)

choose_button = tk.Button(root, text="Choose file", command=choose_file)
choose_button.pack(pady=5)

generate_button = tk.Button(root, text="Generate report", command=generate_report)
generate_button.pack(pady=20)

root.mainloop()