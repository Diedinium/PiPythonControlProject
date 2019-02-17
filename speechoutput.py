# Synthesizes speech from the input string of text or ssml.
# Using Google Cloud Platform Text to Speech API service
# Made by Jake Hall

# Note: ssml must be well-formed according to:
#   https://www.w3.org/TR/speech-synthesis/

# When called function generates audio output from provided string

def say_value(x):
    # Imports
    import os
    import pygame
    import touchphat
    from envirophat import weather
    
    # Setting the environment API credentials for use with GCP Text to speech
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/home/pi/Documents/TextToSpeechTest-1ccf470ebf59.json"

    # Import text to speech once API key is loaded into environment
    from google.cloud import texttospeech
    
    # Instantiates a client
    client = texttospeech.TextToSpeechClient()

    # Set the text input to be synthesized
    synthesis_input = texttospeech.types.SynthesisInput(text=x)

    # Build the voice request, select the language code ("en-US") and the ssml
    # voice gender ("neutral")
    voice = texttospeech.types.VoiceSelectionParams(
        language_code='en-US',
        ssml_gender=texttospeech.enums.SsmlVoiceGender.NEUTRAL)

    # Select the type of audio file you want returned
    audio_config = texttospeech.types.AudioConfig(
        audio_encoding=texttospeech.enums.AudioEncoding.MP3)

    # Perform the text-to-speech request on the text input with the selected
    # voice parameters and audio file type
    response = client.synthesize_speech(synthesis_input, voice, audio_config)

    # The response's audio_content is binary.
    with open('output.mp3', 'wb') as out:
        # Write the response to the output file.
        out.write(response.audio_content)
        print('Audio content written to file "output.mp3"')
        
    # Play the output.mp3 audio file    
    print('Playing audio file')
    pygame.mixer.init()
    pygame.mixer.music.load("output.mp3")
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy() == True:
        continue


