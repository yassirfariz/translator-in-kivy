from gtts import gTTS
from playsound import playsound
import datetime

def get_date():
   x = datetime.datetime.now()
   year = x.year
   month = x.month
   day = x.day
   hour = x.hour
   minute = x.minute
   
   return year, month,day,hour,minute                        
class sp():
   @staticmethod
   def p_en(Text):
      sound = gTTS(text=Text, lang='en', slow=False)
      try:
         sound.save(
             f"C:/Users/beck/Desktop/google trans/records/speech/{Text}_eng.mp3")
         playsound(f"C:/Users/beck/Desktop/google trans/records/speech/{Text}_eng.mp3")
      except:
         playsound(
             f"C:/Users/beck/Desktop/google trans/records/speech/{Text}_eng.mp3")
   @staticmethod
   def p_fr(Text):
      sound = gTTS(text=Text, lang='fr', slow=False)
      try:
         sound.save(
          f"C:/Users/beck/Desktop/google trans/records/speech/{Text}_fr.mp3")
         playsound(
          f"C:/Users/beck/Desktop/google trans/records/speech/{Text}_fr.mp3")
      except:
         playsound(
              f"C:/Users/beck/Desktop/google trans/records/speech/{Text}_fr.mp3")

   @staticmethod
   def p_ar(Text):
      sound = gTTS(text=Text, lang='ar', slow=False)
      name = get_date()
      try:
        sound.save(
          f"C:/Users/beck/Desktop/google trans/records/speech/{name}_ar.mp3")
        playsound(
          f"C:/Users/beck/Desktop/google trans/records/speech/{name}_ar.mp3")
      except: 
          playsound(
              f"C:/Users/beck/Desktop/google trans/records/speech/{name}_ar.mp3")
   @staticmethod
   def p_es(Text):
      sound = gTTS(text=Text, lang='es', slow=False)
      try:
          sound.save(
          f"C:/Users/beck/Desktop/google trans/records/speech/{Text}_es.mp3")
          playsound(
          f"C:/Users/beck/Desktop/google trans/records/speech/{Text}_es.mp3")
      except:
          playsound(
              f"C:/Users/beck/Desktop/google trans/records/speech/{Text}_es.mp3")

   @staticmethod
   def p_de(Text):
      sound = gTTS(text=Text, lang='de', slow=False)
      try:
        sound.save(
          f"C:/Users/beck/Desktop/google trans/records/speech/{Text}_de.mp3")
        playsound(
          f"C:/Users/beck/Desktop/google trans/records/speech/{Text}_de.mp3")
      except:
        playsound(
            f"C:/Users/beck/Desktop/google trans/records/speech/{Text}_de.mp3")

   @staticmethod
   def p_pt(Text):
      sound = gTTS(text=Text, lang='pt', slow=False)
      try:
        sound.save(
          f"C:/Users/beck/Desktop/google trans/records/speech/{Text}_pt.mp3")
        playsound(
          f"C:/Users/beck/Desktop/google trans/records/speech/{Text}_pt.mp3")
      except:
          playsound(
              f"C:/Users/beck/Desktop/google trans/records/speech/{Text}_pt.mp3")


