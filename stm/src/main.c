#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// Function prototypes
int add(int a, int b);
void print_array(int arr[], int size);
char *create_greeting(const char *name);

int main(int argc, char *argv[]) {
  printf("Hello, World!\n");

  // Basic arithmetic
  int x = 5;
  int y = 10;
  int sum = add(x, y);
  printf("Sum of %d and %d is %d\n", x, y, sum);

  // Array example
  int numbers[] = {1, 2, 3, 4, 5};
  int size = sizeof(numbers) / sizeof(numbers[0]);
  print_array(numbers, size);

  // String example
  const char *name = "Alice";
  char *greeting = create_greeting(name);
  if (greeting != NULL) {
    printf("%s\n", greeting);
    free(greeting);
  }

  return 0;
}

int add(int a, int b) { return a + b; }

void print_array(int arr[], int size) {
  printf("Array elements: ");
  for (int i = 0; i < size; i++) {
    printf("%d ", arr[i]);
  }
  printf("\n");
}

char *create_greeting(const char *name) {
  if (name == NULL) {
    return NULL;
  }

  size_t greeting_len = strlen("Hello, ") + strlen(name) + 2;
  char *greeting = (char *)malloc(greeting_len);

  if (greeting == NULL) {
    return NULL;
  }

  snprintf(greeting, greeting_len, "Hello, %s!", name);
  return greeting;
}
