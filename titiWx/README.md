titi is a satelitall image viewer
====



### Features

* Support a huge kind of satellital/radar image formats (via pyraster which uses GDAL Raster Formats: http://www.gdal.org/formats_list.html).
* You can extract the stored value clicking over the image.
* Extract from georederenced images the stored value giving the coordinates (latitude and longitude).
* Use different kinds of color maps tu visualize the image.

### How to use titi

titi has two files to be used:

* titi : the main satelital image viewer
* tit-k: a useful tool to make massive calcs over a set of images

You can run anyone from the command line:

    python titi.py

or

    python titi-k.py

From the main viewer, titi, you can invoke titi-k using the graphical user interface over the menues.

### Dependencies
* python-numpy
* python-matplotlib
* python-gdal
* python-wxgtk2.8

### To do List
* About the code/GUI design
    * GUI re-design: to use notebook/tabs			[OK]
    * Zoom to be fixed
    * Prueba desde titi original

* About functionality
    * Number of bands automatically detected		[OK]
    * Math operation between bands (NDVI, NWDI, etc..)	[..]
    * Massive extraction: extract values (from a given lat & long) from selected images... [..]


