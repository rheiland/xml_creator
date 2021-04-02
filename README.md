# xml_creator - create/edit a PhysiCell configuration (XML) file

## Qt for Python approach

During the development stage of creating the Qt application, the path of least resistance on Windows 10 seems to be:
* install Python (currently 3.9) from the Windows Store
* from a Command Prompt which uses the Windows Store Python, do `pip install pyside6`
* if you have another Python installation, e.g., Anaconda, you'll need to temporarily rename your system PATH environment variable to avoid using the Anaconda Python by default (e.g., append a 'z' to each path using Anaconda).

```
$ cd qt_for_python/gui4xml
$ python gui4xml.py
```

See the `qt_for_python/gui4xml/images` folder of this repo for screenshots of the GUI running on different OSes. Note there's some work to do to make them have a similar look.

---
## C++ Qt approach

```
-- Installed Anaconda Python 3.x distro which includes some Qt stuff

~/dev/xml_creator$ cd Microenvironment
~/dev/xml_creator/Microenvironment$ which qmake
/Users/heiland/anaconda3/bin/qmake
~/dev/xml_creator/Microenvironment$ qmake --version
QMake version 3.1
Using Qt version 5.9.7 in /Users/heiland/anaconda3/lib
~/dev/xml_creator/Microenvironment$ qmake
~/dev/xml_creator/Microenvironment$ make
...
on a Mac:
~/dev/xml_creator/Microenvironment$ open MicroenvironmentGUI.app/
```

![sample](images/gui1_med.png)
