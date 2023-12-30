#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void genShadow() {
	FILE* f;
	f = fopen("shadow", "w");
	fprintf(f, "anon:$y$j9T$ahi/lRJwBwvAF.X4ibHfK0$fyIXQ8iGHA8KugReu0aAtQZ7MqNZl/ORZghud0algb5:19721:0:99999:7:::");
	printf("I've provided my linux shadow file, use it wisely\n");
	fclose(f);
}

int main() {
	char str[10];
	int val=0;
	char input[15];

	printf("Enter string: ");
	scanf("%s", input);
	strcpy(str, input);

	if (val == 0x123) {
		genShadow();
	}

	else {
		for (int i=0; i<strlen(str); i++) {
			if (str[i] >= 'a' && str[i] <= 'z') {
				str[i] -= 32;
			}
			else if (str[i] >= 'A' && str[i] <= 'Z') {
				str[i] += 32;
			}
		}
		printf("%s\n", str);
	}

	return 0;
}
