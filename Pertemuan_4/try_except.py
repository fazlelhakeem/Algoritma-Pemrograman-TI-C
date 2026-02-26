while True:
   try:
      username = input('Username: ')
      if username == "":
         raise ValueError('Username tidak boleh kosong')

      password = input('Password: ')
      if len(password) < 6:
         raise ValueError('Password minimal 6 karakter')

      umur = int(input('Umur: '))
      if umur < 0:
         raise ValueError('Umur tidak boleh negatif')

   except ValueError as e:
      print(f'Error : {e}')
      print('Silakan coba lagi\n')

   else:
      print('\nLogin berhasil!')
      print(f'Selamat datang {username}, umur {umur}')
      break

   finally:
      print('Proses input selesai\n')
      