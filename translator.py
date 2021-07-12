import googletrans as gt
gt = gt.Translator()
class tr():
   @staticmethod
   def fr(text):
      res = gt.translate(text, dest='fr')
      return res.text
   @staticmethod
   def ar(text):
      res = gt.translate(text, dest='ar')
      return res.text
   @staticmethod
   def en(text):
      res = gt.translate(text, dest='en')
      return res.text
   @staticmethod
   def es( text):
      res = gt.translate(text, dest='es')
      return res.text
   @staticmethod
   def de(text):
      res = gt.translate(text, dest='de')
      return res.text
   @staticmethod
   def port( text):
      res = gt.translate(text, dest='pt')
      return res.text
