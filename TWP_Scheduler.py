import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib.dates import DateFormatter
import tkinter as tk
from tkinter import filedialog
import textwrap


def generate_plot():
    # Prompt user to select a file using a file dialog
    file_path = filedialog.askopenfilename(title="Select CSV file", filetypes=[("CSV files", "*.csv")])

    # Check if a file was selected
    if not file_path:
        print("No file selected. Exiting.")
        return

    # Define columns containing date information
    date_columns = ["Start", "Finish"]

    # Read the CSV file into a pandas DataFrame and sort by the 'Start' column in descending order
    df = pd.read_csv(file_path)

    # Convert columns with date information to datetime format
    for col in date_columns:
        df[col] = pd.to_datetime(df[col], dayfirst=True)

    # Calculate the duration of each task
    df["Diff"] = df.Finish - df.Start

    # Create a 'Modified Item' column for plotting (using suffix for Item Position = 1)
    df['Modified Item'] = df.apply(
        lambda row: f"{row['Item']}_{row.name}" if df['Item Position'].nunique() > 1 and row['Item Position'] == 1
        else row['Item'], axis=1)

    # Create a figure and axis object for the plot
    fig, ax = plt.subplots(figsize=(14, 10))

    # Initialize an empty list to store item labels
    labels = []

    # Initialize a list to keep track of valid indices (i.e., items that are plotted)
    valid_indices = []

    # Get unique modified items (to handle plotting) in reverse chronological order
    unique_items = df['Modified Item'].unique()[::-1]

    # Iterate over each modified item for plotting
    for i, mod_item in enumerate(unique_items):
        # Filter the DataFrame for the current modified item
        filtered_df = df[df['Modified Item'] == mod_item]

        # Check if the filtered DataFrame is empty
        if filtered_df.empty:
            print(f"No data found for Modified Item: {mod_item}. Skipping...")
            continue  # Skip this iteration if no data is found

        # Add the index of valid items
        valid_indices.append(len(valid_indices))  # Append the current valid index

        # Get the original item name (without suffix) to display on the chart
        original_item = filtered_df['Item'].values[0]

        # Add the original item to the list of labels (multiple positions for the same item will still only show one label)
        labels.append(original_item)

        # Iterate over each color group within the modified item
        for r in filtered_df.groupby("Color"):
            # Extract data for plotting from the color group
            data = r[1][["Start", "Diff"]]

            # Plot the data as broken bar plot with black boundaries and 2pt thickness
            ax.broken_barh(data.values, (len(valid_indices) - 1 - 0.4, 0.8), color=r[0], label=r[0], edgecolor='black',
                           linewidth=2)

            # Add item labels to the bars
            for index, row in r[1].iterrows():
                item_label = row['Item Name']  # Get the 'Item Name' label
                bar_end = row['Start'] + row['Diff']  # Calculate the end of the bar

                # Rotate the label 90 degrees only if the color is NOT black or blue
                rotation_angle = 90 if r[0] not in ['black', 'blue'] else 0

                # Wrap the text for vertical labels (when rotated)
                wrapped_label = "\n".join(textwrap.wrap(item_label, width=7)) if rotation_angle == 90 else item_label

                # Set text color as black for 'Item Position = 1' regardless of bar color
                text_color = 'black' if row['Item Position'] == 1 else 'white'

                # Position the label just outside the right edge of the bar for 'Item Position = 1'
                x_position = bar_end + pd.Timedelta(days=5) if row['Item Position'] == 1 else bar_end - row['Diff'] / 2

                # Add the label to the plot
                ax.text(x_position, len(valid_indices) - 1, wrapped_label,
                        ha='left' if row['Item Position'] == 1 else 'center',
                        va='center', color=text_color, fontweight='bold', fontsize='large', rotation=rotation_angle)

    # Set y-axis ticks and labels (using only valid items that were plotted)
    ax.set_yticks(valid_indices)
    ax.set_yticklabels(labels, fontweight='bold')  # Making item labels bold
    ax.set_ylabel("Activity", fontsize=18, fontweight='bold')

    # Set x-axis label and format
    ax.set_xlabel("Timeline", fontsize=18, fontweight='bold')
    date_form = DateFormatter("%m-%Y")
    locator = mdates.MonthLocator()
    ax.xaxis.set_major_formatter(date_form)
    ax.xaxis.set_major_locator(locator)

    # Rotate x-axis labels for better readability
    plt.setp(ax.get_xticklabels(), rotation=60, fontsize=14, fontweight='bold')

    # Increase font size of y-axis labels
    plt.setp(ax.get_yticklabels(), fontsize=14, fontweight='bold')

    # Add gridlines to the x-axis
    ax.xaxis.grid()

    # Set plot title
    plt.title('TWP Scheduler', fontsize=18, fontweight='bold')

    # Adjust layout for better appearance
    plt.tight_layout()

    # Adjust layout to make room for the legend outside the plot
    plt.subplots_adjust(left=0.2, bottom=0.25)  # Increased left padding to fit y-axis labels

    # Add legend with custom labels and colors
    legend_elements = [
        plt.Line2D([0], [0], color='orange', lw=4, label='Exploration'),
        plt.Line2D([0], [0], color='brown', lw=4, label='Appraisal'),
        plt.Line2D([0], [0], color='red', lw=4, label='Oil Development'),
        plt.Line2D([0], [0], color='green', lw=4, label='Gas Development'),
        plt.Line2D([0], [0], color='gray', lw=4, label='Rig Move'),
        plt.Line2D([0], [0], color='black', lw=4, label='Facilities'),
        plt.Line2D([0], [0], color='blue', lw=4, label='Project Maturation')
    ]
    # Place the legend outside the plot area
    ax.legend(handles=legend_elements, loc='lower left', fontsize=10, frameon=False, bbox_to_anchor=(0, -0.3),
              borderaxespad=0, ncols=2)

    # Save the plot as an image file
    fig.savefig('TWP.png', facecolor='white', transparent=False, dpi=600)

    # Open and display the generated plot
    img = Image.open('TWP.png')
    img.show()






# Create a Tkinter root window
root = tk.Tk()
root.title("TWP Generator")
root.geometry("400x400")

# Set the default theme to black
root.configure(bg="black")

# Create a frame to hold the button
frame = tk.Frame(root, bg="black")
frame.place(relx=0.5, rely=0.6, anchor="center")  # Adjusted to keep it central below the image

# Create a button to execute the code
generate_button = tk.Button(frame, text="TWP Generator", command=generate_plot, bg="black", fg="white")
generate_button.pack()

# Run the Tkinter event loop
root.mainloop()
