#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>
#include <math.h>

void run() {
  FILE *inputFileP;
  int totalPaperNeeded = 0;
  int totalRibbonNeeded = 0;
  int length1 = 0;
  int length2 = 0;
  int length3 = 0;

  inputFileP = fopen("input.txt", "r");

  if (inputFileP == NULL) {
    fprintf(stderr, "Can't open input file input.txt!\n");
    exit(1);
  }

  while(fscanf(inputFileP, "%dx%dx%d", &length1, &length2, &length3) != EOF) {

    if (length2 < length1) {
      int temp = length2;
      length2 = length1;
      length1 = temp;
    }
    if (length3 < length1) {
      int temp = length1;
      length1 = length3;
      length3 = temp;
    }
    if (length3 < length2) {
      int temp = length2;
      length2 = length3;
      length3 = temp;
    }
    totalRibbonNeeded += (2 * length1) + (2 * length2) + (length1 * length2 * length3);
    totalPaperNeeded += (length1 * length2 * 3) + (length1 * length3 * 2) + (length2 * length3 * 2);
  }

  printf("Total paper needed = %d. Total ribbon needed = %d\n", totalPaperNeeded, totalRibbonNeeded);
}

int main() {
  run();
}
