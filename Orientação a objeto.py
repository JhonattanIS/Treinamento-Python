class Televisao:
    def __init__(self):
        self.marca = "LG"
        self.volume = 0

    def aumentar_volume (self):
            if self.Volume < 10:
                self.Volume = self.Volume+1

    def reduzir_Volume (self):
            if self.Volume > 0:
                self.Volume = self.volume-1
    
tv = Televisao()
print (tv)
             