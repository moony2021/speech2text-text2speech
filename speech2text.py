# Import the Gtts module for text  
# to speech conversion 
from gtts import gTTS 
  
# import Os module to start the audio file
import os 
  
mytext = 'hello, how can I help you'
  
# Language we want to use 
language = 'en'
  

text = gTTS(text=mytext, lang=language, slow=False) 
  

text.save("output.mp3") 
  
# Play the converted file 
os.system("start output.mp3") 