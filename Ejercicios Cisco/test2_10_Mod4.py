import os
os.mkdir('pictures')
os.chdir('pictures')
os.mkdir('thumbnails')
os.chdir('thumbnails')
os.mkdir('temp')
os.chdir('../')

print(os.getcwd())