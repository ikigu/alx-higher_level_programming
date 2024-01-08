#include <Python.h>
#include <object.h>
#include <listobject.h>

/**
* print_python_list_info - prints some basic info about a python list
* @p: python object
**/

void print_python_list_info(PyObject *p)
{
	long int list_size =  PyList_Size(p);
	int i = 0;
	PyListObject *object = (PyListObject *)p;

	printf("[*] Size of the Python List = %li\n", list_size);
	printf("[*] Allocated = %li\n", object->allocated);

	while (i < list_size)
	{
		printf("Element %i: %s\n", i, Py_TYPE(object->ob_item[i])->tp_name);
		i++;
	}
}
