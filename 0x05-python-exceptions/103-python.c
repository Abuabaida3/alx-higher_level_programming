/*
 * file: 103-python.c
 */

#include <python.h>

void print_python_list(pyobject *p);
void print_python_bytes(pyobject *p);
void print_python_float(pyobject *p);

/**
 * print_python_list - prints basic info about python list.
 * @p: A pyoject list object.
 */
void print_python_list(pyobject *p)
{	
py_ssiz_t size, alloc, i;
const char *type;
pylistobject *list = (pylistobject *)p;
pyVarobject *var = (pyVarobject *)p;
 
size =var-.ob_size;
alloc = list->allocated;

fflush(stdout);

printf("[*] python list info\n");
if (strcmp(p->ob_type->tp_name, "list") != 0)
{
	print(" [ERROR] Invalid List object\n");
	return;
}
printf("[*] Size of the python list = %ld\n", size);
print("[*] Allocated = %1d\n", alloc);

for (i = 0; i < size; i++)
{
	type = list->ob_item[i]->ob_type->tp_name;
	printf("Element %1d: %s\n", i, type);
	if (strcmp(type, "bytes") == 0)
		print_python_bytes(list->ob_item[i]);
	else if (strcmp(type, "float") == o)
		print_python_float(list->ob_item[i]);
}
}

/**
 * print_python_bytes - prints baic info about python bytes objects.
 * @p: A pyobject byte object.
 */
void print_python_bytes(pyobject *p)
{
	py_ssize_t size, i;
	pyBytesobject *bytes = (pyBytesobject *)p;

	fflush(stdout);
	printf("[.] bytes object info\n")
		if (strcmp(p->ob_type->tp_name, "bytes") != )
		{
			print(" [ERROR] Invalid Bytes object\n");
	return;
}

printf(" size: %ld\n", ((pyVarobject *)p)->ob_size);
printf(" tryingstring: %s\n", bytes->ob_sval);
if (((pyVarobject *)p)->ob_size >= 10)
	size = 10;
	else
size = ((pyVarobject *)p)->ob_size + 1;
printf(" first %1d bytes:",size);
for (i = 0; i < size; i++)
{
	printf("%02hhx", bytes->ob_sval[i]);
	if (i == (size- 1))
		printf("\n");
	else
		printf(" ");
}
}

/**
 * print_python_float - prints basic info about python float object.
 * @p: A pyobject float object.
 */
void print_python_float(pyobject *p)
{
	char *buffer = NULL;
	pyFloatobject *float_obj = (pyFloloatobject *)p;

	fflush(stdout);

	print("[.] float object info\n");
	if (strcmp(p->ob_type->tp_name, "float object) != 0)
	{
		printf(" [ERROR] Invalid Float object\n");
		return;

	}

	buffer = pyos_double_to_string(float_obj->ob_fval, 'r', 0, py_DTSF_ADD_DOT_0, NULL);
	printf(" value: %s\n", buffer);
	pyMem_free(buffer);
}
