About this fork
====
This fork presents changes in titi,  referred to a different languaje of user interfaces and functionalities.
Firstly, the languaje of user interfaces was changed from WxPython to PyQt.
Secontly, new functions were aggregated in titi. This allow see satellital images from SAC-D/Aquarius mision. Using tar.gz files the user can graph orbits of different band and product for the levels of processing L1B and L2. 
In conclusion, titi keeps all its funcionalities and adds the capacity of visualization images from SAC-D/Aquarius mision.


### About new functionality

User has to:

* Select orbits option 
* Select folder where are tar.gz files from SAC-D mision
* Select level of processing from images
* Select type of map and colour scale
* Select graph

With these steps, you can see a world map with orbits from the satellite 

You can run from the command line:

    python titi.py


### Dependencies
* python-numpy
* python-matplotlib
* python-osgeo
* python-wxgtk2.8
* python-tarfile
* python-shutil
* python pyqt4
* python mpl_toolkits.basemap



