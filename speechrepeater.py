import os
import pypdf
import gtts
import playsound

print("Current working directory:", os.getcwd())

file_path = "Do Epic Shit.pdf"  

if not os.path.isfile(file_path):
    print(f"File not found: {file_path}")
else:
    print(f"File found: {file_path}")

    # Open the PDF file
    with open(file_path, "rb") as file:
        reader = pypdf.PdfReader(file)
        
        # Get the number of pages in the PDF
        num_pages = len(reader.pages)
        print(f"The PDF has {num_pages} pages.")
        
        # Extract text from each page
        full_text = ""
        for i in range(num_pages):
            page = reader.pages[i]
            text = page.extract_text()
            if text:  # Ensure text is not None
                full_text += text + "\n"
    
    # Convert the extracted text to speech
    if full_text:
        sound = gtts.gTTS(full_text, lang="en")
        sound.save("tts.mp3")
        
        # Play the resulting audio file
        playsound.playsound("tts.mp3")
    else:
        print("No text could be extracted from the PDF.")
