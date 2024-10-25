pip install pyinstaller psutil PyQt5 requests

echo Y | del dist\main\* 
echo Y | del build\main\*

echo y | python -m PyInstaller src/main.py --windowed --icon asset/program.ico

copy dist\main\main.exe dist\main\FlyffUniverse.exe
del dist\main\main.exe
mkdir dist\main\cache_folder
