import os

print(os.path.abspath(os.path.join(os.path.sep)))
# или
print("Корень диска:", os.path.abspath('.').split("\\")[0])
