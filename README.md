This demonstrates a memory leak in a Python module that will be invisible
to memory profiling and tracing tools that operate at the level of Python code,
but will be visible to tools that measure process memory metrics or trace
into C libraries, system calls, etc.

Build with:

````
python ./setup.py build
````

Install with:

````
python ./setup.py install
````

For obvious reasons you will want this in an isolated, disposable virtual environment.

Usage:

````
% python                   
Python 3.8.10 (default, Sep 28 2021, 16:10:42) 
[GCC 9.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> from sum_urandom import sum_urandom
>>> sum_urandom(10000)
18446744073709536210
>>> 
````