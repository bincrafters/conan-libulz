#include <stdlib.h>

#include "strlib.h"
#include "format.h"

int main(void) {
	char out[32] = {0};

	raw2hex(out, "bincrafters", 11);
	ulz_printf("bincrafters: 0x%s\n", out);

	return EXIT_SUCCESS;
}
