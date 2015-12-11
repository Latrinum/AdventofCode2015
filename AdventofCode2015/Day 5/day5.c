#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>
#include <math.h>

bool isVowel(char v) {
  if(v == 'a' || v == 'e' || v == 'i' || v == 'o' || v == 'u') {
    return true;
  }
  return false;
}

bool hasThreeVowels(char name[]) {
  int i = 0;
  int vowelCount = 0;

  while(name[i] != '\0') {
    if (isVowel(name[i])) {
      vowelCount++;
      if(vowelCount == 3) {
        return true;
      }
    }
    i++;
  }

  return false;
}

int hasTwoInARow(char name[]) {
  int i = 0;

  while(name[i+1] != '\0') {
    if(name[i] == name[i+1]) {
      return true;
    }
    i++;
  }

  return false;
}

bool hasForbiddenStrings(char name[]) {
  int i = 0;

  while(name[i+1] != '\0') {
    if(name[i] == 'a' && name[i+1] == 'b') {
      return true;
    }
    if(name[i] == 'c' && name[i+1] == 'd') {
      return true;
    }
    if(name[i] == 'p' && name[i+1] == 'q') {
      return true;
    }
    if(name[i] == 'x' && name[i+1] == 'y') {
      return true;
    }
    i++;
  }

  return false;
}

bool hasRepeatSkipLetter(char name[]) {
  int i = 0;

  while(name[i+2] != '\0') {
    if(name[i] == name[i+2]) {
      return true;
    }
    i++;
  }

  return false;
}

bool hasPairs(char name[], int nameLength) {
  int i = 0;

  for(i = 0; i < nameLength; i++) {

    for(int j = i+2; j < nameLength; j++) {
      if(name[i] == name[j] && name[i+1] == name[j+1]) {
        return true;
      }
    }
  }

  return false;
}

bool nice(char name[], int part, int nameLength) {

  if(part == 1) {
    if(hasThreeVowels(name) && hasTwoInARow(name) && !hasForbiddenStrings(name)) {
      return true;
    }
  } else if(part == 2){
    printf("hasRepeatSkipLetter(name) %s\n", hasRepeatSkipLetter(name) ? "true" : "false");
    printf("hasPairs(name, nameLength) %s\n", hasPairs(name, nameLength) ? "true" : "false");
    if(hasRepeatSkipLetter(name) && hasPairs(name, nameLength)) {
      return true;
    }
  }

  return false;

}

void run() {
  FILE *inputFileP;
  char name[17];
  int niceCountPart1 = 0;
  int niceCountPart2 = 0;
  int part = 2;

  inputFileP = fopen("input.txt", "r");

  if (inputFileP == NULL) {
    fprintf(stderr, "Can't open input file input.txt!\n");
    exit(1);
  }

  while(fscanf(inputFileP, "%s", name) != EOF) {
    if(nice(name, part, 17)) {
      if(part == 1) {
        niceCountPart1++;
      } else if(part == 2) {
        niceCountPart2++;
      }
    };
  }

  printf("Nice count part 1: %d\n", niceCountPart1);
  printf("Nice count part 2: %d\n", niceCountPart2);
}

int main() {
  printf("%s\n", nice("ieodomkazucvgmuy", 2, 17) ? "true" : "false");
  run();

  return 0;
}
