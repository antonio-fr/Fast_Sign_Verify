rd /S /Q build
rd /S /Q dist
c:\python27_32\python.exe setup.py py2exe
cd dist
ren main.exe FSV.exe
cd ..
copy c:\Python27_32\Lib\msvcp90.dll dist
cd dist

