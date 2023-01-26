# Абсолютный путь до файла: C:\Users\Roman\PycharmProjects\Skillbox\access\admin.bat
#
# Относительный путь до файла: Skillbox\access\admin.bat
import os
abs_path = os.path.abspath('14593424.pdf')
print(abs_path)
rel_path = os.path.join('Practical_work', '22.1 Модуль os генерация путей и метод listdir', '14593424.pdf')
print(rel_path)

print()
# или

rel_path = os.path.join("access", "admin.bat")
abs_path = os.path.abspath(rel_path)
print("Абсолютный путь до файла:", abs_path)
print("Относительный путь до файла:", rel_path)