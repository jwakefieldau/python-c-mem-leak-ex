from distutils.core import setup, Extension

sum_urandom_module = Extension(
  'sum_urandom',
  sources=['sum_urandom.c']
)

setup(
  name='sum_urandom',
  version='0.1',
  description='Sum char values read from /dev/urandom.  An example of'
              'a malloc()-based memory leak in a module written in C',
  ext_modules=[sum_urandom_module]
)
