#include <stdio.h>
#include <Python.h>

/**
 * print_python_bytes - prints info about python bytes
 * @p: pointer to PyObject
 */
void print_python_bytes(PyObject *p)
{
    Py_ssize_t i, size;
    char *str;

    printf("[.] bytes object info\n");
    if (!PyBytes_Check(p))
    {
        printf("  [ERROR] Invalid Bytes Object\n");
        return;
    }
    size = ((PyVarObject *)p)->ob_size;
    printf("  size: %ld\n", size);
    str = ((PyBytesObject *)p)->ob_sval;
    printf("  trying string: %s\n", str);
    if (size < 10)
        printf("  first %ld bytes:", size + 1);
    else
        printf("  first 10 bytes:");
    for (i = 0; i <= size && i < 10; i++)
        printf(" %02hhx", str[i]);
    printf("\n");
}