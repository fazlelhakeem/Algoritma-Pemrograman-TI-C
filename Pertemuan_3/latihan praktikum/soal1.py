class Vehicle:
   def __init__(self, jenis, merk, tahun_rilis):
      self.jenis = jenis
      self.merk = merk
      self.tahun_rilis = tahun_rilis

   def sound(self):
      return "suara"

class Mobil(Vehicle):
   def __init__(self, jenis, merk, tahun_rilis):
      super().__init__(jenis, merk, tahun_rilis)
      self.__warna = 'merah'

   def get_warna(self):
      return self.__warna

class Motor(Vehicle):
   def __init__(self, jenis, merk, tahun_rilis):
      super().__init__(jenis, merk, tahun_rilis)
      self.__warna = 'putih'

   def get_warna(self):
      return self.__warna

kapal = Vehicle('kapal', 'titanic', 1876)
mobil1 = Mobil('Civic', 'Honda', 2015)
motor1 = Motor('Vario', 'Honda', 2020)

print(kapal.merk)
print(mobil1.get_warna())
print(motor1.get_warna())