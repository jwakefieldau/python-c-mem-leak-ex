#define PY_SSIZE_T_CLEAN
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <stdlib.h>

#include "Python.h"

static PyObject *sum_urandom(PyObject *self, PyObject *args);

static PyMethodDef sum_urandom_methods[] = {
  {"sum_urandom", sum_urandom, METH_VARARGS, "Sum ASCII values from /dev/urandom"},
  {NULL, NULL, 0, NULL}
};

static struct PyModuleDef sum_urandom_module = {
  PyModuleDef_HEAD_INIT,
  "sum_urandom",
  NULL,
  -1,
  sum_urandom_methods
};

PyMODINIT_FUNC PyInit_sum_urandom(void) {
  return PyModule_Create(&sum_urandom_module);
}

static PyObject *sum_urandom(PyObject *self, PyObject *args) {

  short len;
  ssize_t len_read;
  int fd;
  char *buf = NULL;
  unsigned long sum = 0;
  short sum_i;

  if (!PyArg_ParseTuple(args, "h", &len)) {
    return NULL;
  }
  if ((len > 10000) || (len < 0)) {
    len = 10000;
  }
  buf = (char *)malloc(sizeof(char) * len);
  fd = open("/dev/urandom", O_RDONLY);
  if (fd < 0) {
    return NULL;
  }
  len_read = read(fd, buf, len);
  for (sum_i = 0; sum_i < len_read; sum_i++) {
    sum += buf[sum_i];
  }
  return PyLong_FromUnsignedLong(sum);
}