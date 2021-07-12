from kivy.uix.boxlayout import BoxLayout
from kivy.app import App
from translator import tr
import arabic_reshaper
import bidi.algorithm
from speech import sp

class Widgt(BoxLayout):
   def translate(self, text, lang):
      if lang == "frensh":
         self.translated = tr.fr(text)
         self.ids.output.text = self.translated
      if lang == "arabic":
         self.translated = tr.ar(text)
         self.rech = arabic_reshaper.reshape(self.translated)
         self.res = bidi.algorithm.get_display(self.rech)
         self.ids.output.text = self.res
      if lang == "english":
         self.translated = tr.en(text)
         self.ids.output.text = self.translated
      if lang == "spanish":
         self.translated = tr.es(text)
         self.ids.output.text = self.translated
      if lang == "deutsch":
         self.translated = tr.de(text)
         self.ids.output.text = self.translated
      if lang == "portugese":
         self.translated = tr.port(text)
         self.ids.output.text = self.translated
   def play(self, text, lang):
      if lang == "frensh":
         self.translated = tr.fr(text)
         sp.p_fr(self.translated)
      if lang == "arabic":
         self.translated = tr.ar(text)
         sp.p_ar(self.translated)
      if lang == "english":
         self.translated = tr.en(text)
         sp.p_en(self.translated)
      if lang == "spanish":
         self.translated = tr.es(text)
         sp.p_es(self.translated)
      if lang == "deutsch":
         self.translated = tr.de(text)
         sp.p_de(self.translated)
      if lang == "portugese":
         self.translated = tr.port(text)
         sp.p_pt(self.translated)

class MainApp(App):
   pass
if __name__ == '__main__':
    MainApp().run()
