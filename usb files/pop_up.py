import tkinter as tk
import tkinter.font as tkFont

# Create the main window (root) and hide it
root = tk.Tk()
root.withdraw()  # Hide the main window

def show_custom_popup(message):
    # Create a new top-level window for the custom popup
    popup = tk.Toplevel()

    # Set the size of the window and position it in the center of the screen
    popup.geometry("800x500+{}+{}".format(int(popup.winfo_screenwidth()/2 - 400), int(popup.winfo_screenheight()/2 - 250)))
    popup.title("WARNING!!!")  # Title of the pop-up
    
    # Change the background color to black
    popup.config(bg="black")
    
    # Define a scary font (Rockwell or Impact for a scary, bold font)
    scary_font = tkFont.Font(family="Rockwell", size=18, weight="bold")

    # Add the message text in red to the center of the pop-up
    label = tk.Label(popup, text=message, font=scary_font, fg="red", bg="black", padx=20, pady=20, justify="center")
    label.pack(expand=True, anchor="center")

    # Function to handle closing the pop-up
    def on_close():
        popup.quit()  # Quit the popup event loop
        popup.destroy()  # Destroy the popup window to release resources
        root.quit()  # Close the root Tkinter window

    # Bind the close event to the on_close function
    popup.protocol("WM_DELETE_WINDOW", on_close)

    # Focus the popup window to grab attention
    popup.focus_set()
    
    # Start the popup event loop
    popup.mainloop()

def get_multiline_input():
    print("Enter your message (type 'DONE' to finish):")
    lines = []
    while True:
        line = input()  # Get user input for each line
        if line.strip().upper() == 'DONE':  # Exit condition when the user types 'DONE'
            break
        lines.append(line)
    # Join the lines with a newline character
    return "\n".join(lines)

# Ask the user for a multi-line input message
user_message = get_multiline_input()

# Show the custom pop-up with the multi-line message
show_custom_popup(user_message)

# After closing the pop-up, the program will properly exit and return control to the terminal
root.quit()