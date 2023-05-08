#include <stdio.h>
#include <stdlib.h>

int main(void) {
	puts("Enter your name");
	char *s = (char*) malloc(30 * sizeof(char));
	fgets(s, 30, stdin);
	printf("Hello, %s\n", s);
	free(s);
	s[40] = 'a';		
}
