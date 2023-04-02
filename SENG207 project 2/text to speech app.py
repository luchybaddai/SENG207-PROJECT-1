import pyttsx3
import PySimpleGUI as sg

# Initialize the pyttsx3 engine
engine = pyttsx3.init()

# Define a list of available voices and their IDs
voices = engine.getProperty('voices')
voices_list = [voice.name for voice in voices]

# Define the PySimpleGUI layout
layout = [
    [sg.Text("Enter text to speak:")],
    [sg.InputText()],
    [sg.Text("Select a voice:")],
    [sg.Listbox(values=voices_list, size=(30, 6), key="-VOICE-")],
    [sg.Text("Adjust speech rate (words per minute):")],
    [sg.Slider(range=(100, 300), default_value=150, orientation="h", size=(20, 15), key="-RATE-")],
    [sg.Button("Speak"), sg.Button("Exit")]
]

# Create the PySimpleGUI window
window = sg.Window("Text to Speech App", layout)

# Start the PySimpleGUI event loop
while True:
    event, values = window.read()
    if event == "Exit" or event == sg.WIN_CLOSED:
        break
    elif event == "Speak":
        # Get the selected voice ID
        voice_id = None
        for voice in voices:
            if values["-VOICE-"][0] in voice.name:
                voice_id = voice.id
                break
        # Set the voice and speech rate
        engine.setProperty("voice", voice_id)
        engine.setProperty("rate", values["-RATE-"])
        # Speak the text
        engine.say(values[0])
        engine.runAndWait()

# Close the PySimpleGUI window and pyttsx3 engine
window.close()
engine.stop()
