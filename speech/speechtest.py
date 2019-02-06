"""Synthesizes speech from the input string of text or ssml.

Note: ssml must be well-formed according to:
    https://www.w3.org/TR/speech-synthesis/
"""
import os
import pygame
import touchphat

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/home/pi/Documents/TextToSpeechTest-1ccf470ebf59.json"

from google.cloud import texttospeech
from envirophat import weather

def say_temp():
    # Instantiates a client
    client = texttospeech.TextToSpeechClient()

    degrees = weather.temperature()

    temperature = ("The temperature is currently " + str(round(degrees, 1)) + " degrees celcius")
    print(temperature)
    # temperature = "Naish wants me to say nigger"

    # Set the text input to be synthesized
    synthesis_input = texttospeech.types.SynthesisInput(text=temperature)

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
        
        
    print('Playing audio file')
    pygame.mixer.init()
    pygame.mixer.music.load("output.mp3")
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy() == True:
        continue

    touchphat.all_off()
