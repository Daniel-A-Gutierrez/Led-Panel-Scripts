Creating Modules
======================================

Setup
--------
Move the samples folder into a location which python checks for packages in. One such example is the dist-packages folder. To check for locations that this folder can be moved to, try `python -c 'import sys; print(sys.path)'`.

Usually, the location below exists in the syspath, so run the following command with your version of python replacing X.X (Ex: python3.5).
```
sudo mv samples /usr/local/lib/pythonX.X/dist-packages/
```
**Do not name other folders "samples"** This can cause conflicts with finding the locations of files when importing.

