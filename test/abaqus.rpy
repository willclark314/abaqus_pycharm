# -*- coding: mbcs -*-
#
# Abaqus/CAE Release 6.14-1 replay file
# Internal Version: 2014_06_05-06.11.02 134264
# Run by mymor on Sat Jul 23 10:23:31 2022
#

# from driverUtils import executeOnCaeGraphicsStartup
# executeOnCaeGraphicsStartup()
#: Executing "onCaeGraphicsStartup()" in the site directory ...
from abaqus import *
from abaqusConstants import *
session.Viewport(name='Viewport: 1', origin=(1.23958, 1.24074), width=182.467, 
    height=123.081)
session.viewports['Viewport: 1'].makeCurrent()
from driverUtils import executeOnCaeStartup
executeOnCaeStartup()
execfile('D:/Documents/GitHub/abaqus_pycharm/test/test.py', __main__.__dict__)
#: A new model database has been created.
#: The model "Model-1" has been created.
session.viewports['Viewport: 1'].setValues(displayedObject=None)
#: The model database has been saved to "D:\Documents\GitHub\abaqus_pycharm\test\zigzag.cae".
print 'RT script done'
#: RT script done
