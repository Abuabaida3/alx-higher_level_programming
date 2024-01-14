/*
 * file: 100-print_python_list_info.c
 * Auth: brennan d baraban
 */

#include <python.h>

/**
 * print_python_list_info - print basic info about python list.
 * @p: A pyobject list.
 */
void print_python_list_info(pyobject *p)
{
	int size, alloc, i;
	    pyobject *obj;

	    size = py_size(p);
	    alloc = ((pylistobject *)p)->allocated;

	    printf("{*} size of the python list = %d\n", size);
	    printf("{*} allocated = %d\n", alloc);

	    for (i = 0; i < size; i++)
		    print("Element %d: ", i);

	    obj = pylist_getItem(p, i)
		    printf("%s\n", py_TYPE(p, i);
				    printf("%s\n", py_TYPE(obj)->tp_name);
}
}
