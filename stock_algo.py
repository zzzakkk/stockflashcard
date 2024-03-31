
import pandas as pd
import requests
import json
import tkinter as tk  
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Create a Tkinter window
root = tk.Tk()
root.title("Zak's Stock Portfolio")

# UI layout
frame = tk.Frame(root)
frame.pack()

# Input widgets
label_symbol = tk.Label(frame, text="Enter stock symbols (comma-separated):")
label_symbol.pack()

entry_symbol = tk.Entry(frame)
entry_symbol.pack()

label_period = tk.Label(frame, text="Select a time period:")
label_period.pack()

period_options = ['1 month', '3 months', '6 months', '12 months', 'YTD']
var_period = tk.StringVar(value='12 months')

for period in period_options:
    radio_period = tk.Radiobutton(frame, text=period, variable=var_period, value=period)
    radio_period.pack()

# Plotting function
def update_plot():
    stock_symbol = entry_symbol.get()
    period = var_period.get()

    # Placeholder data for demonstration
    dates = pd.date_range(start='1/1/2023', periods=30)
    prices = [i ** 2 for i in range(30)]

    # Create and display plot
    plt.figure(figsize=(8, 4))
    plt.plot(dates, prices)
    plt.xlabel("Date")
    plt.ylabel("Price")
    plt.title("Stock Price Trends")
    plt.xticks(rotation=45)
    plt.tight_layout()

    # Show plot in Tkinter window
    canvas = FigureCanvasTkAgg(plt.gcf(), master=root)
    canvas.get_tk_widget().pack()

# Button to update plot
button_plot = tk.Button(frame, text="Update Plot", command=update_plot)
button_plot.pack()

# Label for news
label_news = tk.Label(frame, text="Related News:")
label_news.pack()

# Placeholder news text
news_text = "No news articles found."
label_news_text = tk.Label(frame, text=news_text)
label_news_text.pack()

# Run the Tkinter main loop
root.mainloop()

