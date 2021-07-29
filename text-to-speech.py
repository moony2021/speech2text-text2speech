from ibm_watson import TextToSpeechV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
api = IAMAuthenticator("TDdmsWLc2DOzCNxXAR1IajP3xHovIhd3YURngwRrok9W")
text_to_speech= TextToSpeechV1(authenticator=api)
text_to_speech.set_service_url("https://api.eu-gb.text-to-speech.watson.cloud.ibm.com/instances/967a4f79-853c-4abd-a26e-e48b46cb8c7f")

with open ("welcome.mp3","wb") as audiofile:
    audiofile.write(text_to_speech.synthesize("Hello ",accept="audio/mp3").get_result().content)
