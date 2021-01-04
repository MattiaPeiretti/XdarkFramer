# Xdarkframer

Xdarkframer is a (for now) command line tool to acquire dark frames of local capturing devices
The script is intended to work with python 3.8 and is likely not going to work with python2.X.


### Use

You can launch the script this way:

```
python xdarkframer.py [argument1] [argument2] [argument3] [argument4]
```

- The first argument is an integer of the device you want to use (0 is default)
- The second argument is the number of dark frames you want to capture (from 1 to infinite!)
- The third argument is the file extention of the images when saved (0 for .bmp, 1 for .tiff)
- The fourth argument is the folder to save the images to (you can leave is empty if you are capturing just one image)

### Example:
```
python xdarkframer.py 0 32 1 mydarkframe01/
```

The previous command will create a new folder named "mydarkframe01" and populate it with 32 .tiff images.

Remeber to cover your device's sensor before running!
