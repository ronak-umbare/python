import time
import speech_recognition as sr
import pyttsx3
import tkinter as tk
from tkinter import ttk, messagebox

# Initialize the speech engine and recognizer
recognizer = sr.Recognizer()
engine = pyttsx3.init()

# Predefined dataset of questions for various domains and positions with 10 keywords per question
interview_data = {
    "AI": {
        "Data Scientist": [
            {"question": "What is supervised learning?", "keywords": ["supervised", "training", "labels", "classification", "regression", "model", "data", "algorithm", "input", "output"]},
            {"question": "Explain a decision tree.", "keywords": ["decision", "tree", "splitting", "node", "branch", "leaf", "classification", "root", "feature", "data"]},
            {"question": "What is a neural network?", "keywords": ["neural", "network", "layers", "input", "output", "hidden", "weights", "activation", "data", "model"]},
        ],
        "AI Engineer": [
            {"question": "What is deep learning?", "keywords": ["deep", "learning", "neural networks", "layers", "data", "model", "training", "algorithm", "input", "output"]},
            {"question": "Explain reinforcement learning.", "keywords": ["reinforcement", "reward", "action", "environment", "agent", "policy", "learning", "feedback", "state", "decision"]},
            {"question": "What is the role of AI in healthcare?", "keywords": ["AI", "healthcare", "data", "diagnosis", "treatment", "prediction", "algorithm", "disease", "patients", "technology"]},
        ]
    },
    "Web Development": {
        "Frontend Developer": [
            {"question": "What is React?", "keywords": ["React", "JavaScript", "library", "components", "UI", "frontend", "state", "props", "virtual DOM", "framework"]},
            {"question": "Explain the box model in CSS.", "keywords": ["box model", "padding", "border", "margin", "content", "CSS", "width", "height", "layout", "element"]},
            {"question": "What are web components?", "keywords": ["web components", "custom elements", "shadow DOM", "HTML", "JavaScript", "reusable", "CSS", "encapsulation", "frontend", "UI"]},
        ],
        "Backend Developer": [
            {"question": "What is Node.js?", "keywords": ["Node.js", "JavaScript", "backend", "server", "event-driven", "non-blocking", "runtime", "API", "asynchronous", "framework"]},
            {"question": "Explain RESTful APIs.", "keywords": ["REST", "API", "stateless", "client", "server", "HTTP", "resource", "method", "GET", "POST"]},
            {"question": "What is a database index?", "keywords": ["index", "database", "performance", "query", "search", "optimization", "table", "column", "speed", "storage"]},
        ]
    },
    # Add more domains and positions here
    "Data Analytics": {
        "Analyst": [
            {"question": "What is data cleaning?", "keywords": ["data", "cleaning", "missing", "outliers", "errors", "dataset", "inconsistencies", "accuracy", "quality", "preprocessing"]},
            {"question": "Explain regression analysis.", "keywords": ["regression", "analysis", "predictive", "statistics", "model", "relationship", "variables", "trend", "data", "linear"]},
            {"question": "What is a pivot table?", "keywords": ["pivot", "table", "summary", "data", "group", "columns", "rows", "statistics", "filter", "spreadsheet"]},
        ]
    }
}

# Function to speak out text
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to listen to user's speech and convert to text
def listen():
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
        try:
            response = recognizer.recognize_google(audio)
            print(f"You said: {response}")
            return response
        except sr.UnknownValueError:
            speak("Sorry, I didn't catch that. Please try again.")
            return listen()
        except sr.RequestError:
            speak("Sorry, there was an issue with the recognition service. Please try again.")
            return listen()

# Function to verify if the user's answer contains the expected keywords and return results
def verify_answer(answer, keywords):
    matched_keywords = [keyword for keyword in keywords if keyword.lower() in answer.lower()]
    return matched_keywords, len(matched_keywords)

# Main interview function with UI integration
def start_interview():
    domain = domain_combobox.get()
    position = position_combobox.get()

    if domain not in interview_data:
        messagebox.showerror("Error", f"No data available for the domain '{domain}'")
        return
    if position not in interview_data[domain]:
        messagebox.showerror("Error", f"No data available for the position '{position}'")
        return
    
    speak(f"Starting your interview for {position} in {domain}.")
    
    questions = interview_data[domain][position]
    
    total_keywords = 0
    matched_keywords = 0

    for i, q in enumerate(questions):
        speak(f"Question {i+1}: {q['question']}. You have 60 seconds to answer.")
        question_label.config(text=q['question'])
        
        # Listen to the user's response
        answer = listen()
        answer_entry.delete(0, tk.END)  # Clear the answer entry box for next question
        answer_entry.insert(0, answer)  # Display recognized speech as text

        # Verify answer
        matched, count = verify_answer(answer, q['keywords'])
        matched_keywords += count
        total_keywords += len(q['keywords'])

        # Display matched keywords
        matched_label.config(text=f"Matched Keywords: {', '.join(matched)}")
        root.update()

        time.sleep(1)  # Pause between questions

    # Adjusted logic for passing the interview
    if matched_keywords >= 4:
        speak("Congratulations! You passed the interview , You Are Promoted To Next Round ")
        result_label.config(text="Result: You Passed!")
    else:
        speak("You didn't meet the keyword requirements. You have failed the interview.")
        result_label.config(text="Result: You Failed.")

# Setting up the Tkinter UI with custom styles
root = tk.Tk()
root.title("AI Interviewer")
root.geometry("600x500")
root.configure(bg="#D2B48C")

style = ttk.Style()
style.configure("TButton", font=("Arial", 14), padding=10, )
style.configure("TLabel", background="#D2B48C", font=("Times New Roman", 14))
style.configure("TEntry", padding=5)
style.configure("TCombobox", padding=5)

# Create UI Elements
ttk.Label(root, text="AI Interviewer", font=("Times New Roman", 24, "bold")).pack(pady=10)

ttk.Label(root, text="Domain:").pack(pady=5)
domain_combobox = ttk.Combobox(root, values=list(interview_data.keys()), state="readonly", width=47)
domain_combobox.pack()

ttk.Label(root, text="Position:").pack(pady=5)
position_combobox = ttk.Combobox(root, values=[], state="readonly", width=47)
position_combobox.pack()

# Function to update position options based on domain selection
def update_positions(event):
    selected_domain = domain_combobox.get()
    if selected_domain:
        position_combobox["values"] = list(interview_data[selected_domain].keys())
        position_combobox.set('')

domain_combobox.bind("<<ComboboxSelected>>", update_positions)



# Start Interview Button
ttk.Button(root, text="Start Interview", command=start_interview).pack(pady=20)

# Display question
question_label = ttk.Label(root, text="Question will appear here", font=("Arial", 16))
question_label.pack(pady=10)

# User's Answer Entry
ttk.Label(root, text="Your Answer:").pack()
answer_entry = ttk.Entry(root, width=50)
answer_entry.pack(pady=5)

# Matched Keywords Display
matched_label = ttk.Label(root, text="Matched Keywords will appear here", font=("Times New Roman", 12))
matched_label.pack(pady=10)

# Result Display
result_label = ttk.Label(root, text="Result will appear here", font=("Times New Roman", 16, "bold"))
result_label.pack(pady=10)

# Run the Tkinter loop
root.mainloop()