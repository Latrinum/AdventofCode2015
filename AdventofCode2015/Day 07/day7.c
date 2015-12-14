#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>
#include <math.h>

void interpret(char cmd[]) {

}

void run() {
  FILE *inputFileP;
  char cmd[18];
  int x1, y1, x2, y2;

  inputFileP = fopen("input.txt", "r");

  if (inputFileP == NULL) {
    fprintf(stderr, "Can't open input file input.txt!\n");
    exit(1);
  }

  while(fgets(cmd, 18, inputFileP) != NULL) {
    interpret(cmd);
  }
}

int main() {
  run();

  return 0;
}
