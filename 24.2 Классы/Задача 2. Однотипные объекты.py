class Monitor:
    name = 'Samsung'
    matrix = 'VA'
    res = 'WQHD'
    freq = 0

monitir_1 = Monitor
monitir_1.freq = 60

monitir_2 = Monitor
monitir_2.freq = 144

monitir_3 = Monitor
monitir_3.freq = 70

monitir_4 = Monitor
monitir_4.freq = 60

print('monitir_1 freq -', monitir_1.freq,
      '\nmonitir_2 freq -', monitir_2.freq,
      '\nmonitir_3 freq -', monitir_3.freq,
      '\nmonitir_4 freq -', monitir_4.freq)

class Headphones:
    name = 'Sony'
    sensitivity = 108
    micro = False

headphones_1 = Headphones
headphones_1.micro = False

headphones_2 = Headphones
headphones_2.micro = True

headphones_3 = Headphones
headphones_3.micro = True

print('headphones_1 -', headphones_1.micro)
print('headphones_2 -', headphones_2.micro)
print('headphones_3 -', headphones_3.micro)