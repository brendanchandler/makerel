# Makerel


## Introduction
If you have a c/c++ project using recursive make, the build system will change into various directories and print any error messages relative to the current directory.  This can cause problems for visual studio code.

First, if you use the remote ssh plugin, it gets confused if you give it both absolute and relative paths to the same file, thinking they are different files.

Second, compiler errors point to relative paths based on whichever directory your recursive make is currently in.  This confuses VS code and you're unable to control+click links, or use the problem matcher (F8) to jump to the files correctly.

This script works around these problems by translating the output from 'make' to display paths relative to the directory it was invoked from.  To use it, 

Before
```
$ make
...
make[1]: Entering directory 'src/module'
./foo.cpp:50 some error occured here
```

After
```
$ python3 makerel.py
...
make[1]: Enering directory 'src/module'
src/module/foo.cpp:50 some error occured here
```

## HOWTO
### Is there a shorter way to invoke this?
I like to link the