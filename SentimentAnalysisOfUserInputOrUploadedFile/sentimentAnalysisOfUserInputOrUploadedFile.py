import tkinter as tk  # Import the tkinter library for creating GUI
from tkinter import filedialog  # Import the filedialog submodule to open a file dialog
from vaderSentiment.vaderSentiment import \
    SentimentIntensityAnalyzer  # Import the SentimentIntensityAnalyzer from VADER library


# Function to analyze the sentiment of the input text when the "Analyze Text" button is clicked
def analyze_sentiment():
    text = input_text.get("1.0", tk.END).strip()  # Get the input text from the text input field
    if text:
        perform_sentiment_analysis(text)  # Call the function to perform sentiment analysis if the text is not empty
    else:
        result_label.config(
            text="Please enter text or upload a file.")  # Display an error message if no text is entered


# Function to perform sentiment analysis on the given text
def perform_sentiment_analysis(text):
    analyzer = SentimentIntensityAnalyzer()  # Create a SentimentIntensityAnalyzer object from VADER
    sentiment_scores = analyzer.polarity_scores(text)  # Perform sentiment analysis on the input text
    compound_score = sentiment_scores["compound"]  # Extract the overall sentiment score (compound score)
    positive_score = sentiment_scores["pos"]  # Extract the positive sentiment score
    negative_score = sentiment_scores["neg"]  # Extract the negative sentiment score
    neutral_score = sentiment_scores["neu"]  # Extract the neutral sentiment score

    # Update the result_label with the sentiment analysis results
    result_label.config(text=f"Sentiment Analysis:\n\n"
                             f"Compound Score: {compound_score:.2f}\n"
                             f"Positive Score: {positive_score:.2f}\n"
                             f"Negative Score: {negative_score:.2f}\n"
                             f"Neutral Score: {neutral_score:.2f}")


# Function to browse and select a file for sentiment analysis when the "Upload File" button is clicked
def browse_file():
    file_path = filedialog.askopenfilename()  # Open a file dialog to choose a file
    if file_path: # if file path instance exists
        with open(file_path, "r") as file:  # opening the file in the read mode
            text = file.read()  # Read the content of the selected file
            input_text.delete("1.0", tk.END)  # Clear existing text in the input field
            input_text.insert(tk.END, text)  # Insert the content of the file into the input field


app = tk.Tk()  # Create the main application window
app.title("Sentiment Analysis App")  # Set the title of the window
app.geometry("500x500")  # Set the size of the window

input_text = tk.Text(app, wrap="word")  # Create a text input field for user input
input_text.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)  # Place the text input field in the window with a y padding of 10px an x padding of 10px.

analyze_button = tk.Button(app, text="Analyze Text", command=analyze_sentiment)  # Create a button to analyze the text
analyze_button.pack(pady=5)  # Place the "Analyze Text" button in the window with a y padding of 5 px.

browse_button = tk.Button(app, text="Upload File", command=browse_file)  # Create a button to upload a file
browse_button.pack(pady=5)  # Place the "Upload File" button in the window

result_label = tk.Label(app, text="", font=("Helvetica", 14))  # Create a label to display the sentiment analysis result
result_label.pack(pady=15)  # Place the result label in the window with a y padding of 15 px.

app.mainloop()  # Start the main event loop to run the application
