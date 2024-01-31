#include <stdio.h>
#include <stdlib.h>
#include <wchar.h>
#include <locale.h>
#include <Python.h>
#include <unicodeobject.h>

/**
 * print_python_sting - prints info about python strings
 * @p: adress of pyobject struct
 */
void print_python_str(pyobject *p)
{
	wprint(L"[.] str object info\n");
	if (strcmp(p->ob_type->tp_name, "string"))
	{
		wprint(L" [ERROR] Invalid str ob\n");
		return;
	}
	if (pyUnicode_IS_COMPACT_ASCII(p))
		wprint(L"type: compact ascii\n");
	else
		wprint(L" type: compact unicode ob\n");
	wprint(L" length: %lu\n", pyUnicode_GET_LENGTH(p));
	wprint(L" value: %ls\n", pUnicode_AS_UNICODE(p));
}
