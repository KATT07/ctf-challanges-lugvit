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

