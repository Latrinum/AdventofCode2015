#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>
#include <math.h>

int getEncoded(char str[]) {
  int i = 0;
  int count = 4;

  while(str[i] != '\0') {
    if((int) str[i] == 92 && (int) str[i+1] == 92) {
      count += 4;
      i += 2;
    } else if((int) str[i] == 92 && (int) str[i+1] == 34) {
      count += 4;
      i += 2;
    } else if((int) str[i] == 92 && str[i+1] == 'x') {
      count += 5;
      i += 4;
    } else {
      count++;
      i++;
    }
  }

  return count;
}

int getLiteral(char str[]) {
  int i = 0;
  int count = 0;

  while(str[i] != '\0') {
    count++;
    i++;
  }

  return count;
}

int getValue(char str[]) {
  int i = 1;
  int count = 0;

  while(str[i+1] != '\0') {
    if((int) str[i] == 92 && (int) str[i+1] == 92) {
      count++;
      i += 2;
    } else if((int) str[i] == 92 && (int) str[i+1] == 34) {
      count++;
      i += 2;
    } else if((int) str[i] == 92 && str[i+1] == 'x') {
      count++;
      i += 4;
    } else {
      count++;
      i++;
    }
  }

  return count;
}

void run() {
  FILE *inputFileP;
  char str[100];
  int strLiteral = 0;
  int strValue = 0;
  int strEncoded = 0;

  inputFileP = fopen("input.txt", "r");

  if (inputFileP == NULL) {
    fprintf(stderr, "Can't open input file input.txt!\n");
    exit(1);
  }

  while(fscanf(inputFileP, "%s", str) != EOF) {
    printf("%s\n", str);
    strLiteral += getLiteral(str);
    strValue += getValue(str);
    strEncoded += getEncoded(str);
    printf("%d %d %d\n", getLiteral(str), getValue(str), getEncoded(str));
  }
  printf("strEncoded - strLiteral: %d\n", strEncoded - strLiteral);
  printf("strLiteral - strValue: %d\n", strLiteral - strValue);

}

int main() {
  run();

  //printf("double quotes: %d %d\n", getLiteral("aaa\"aaa"), getValue("aaa\"aaa"));
  return 0;
}
