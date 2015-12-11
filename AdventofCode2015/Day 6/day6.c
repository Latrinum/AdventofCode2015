#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>
#include <math.h>

unsigned char house[1000][1000];

void toggle(int x1, int y1, int x2, int y2) {
  printf("In toggle.\n");
  for(int i = x1; i <= x2; i++) {
    for(int j = y1; j <= y2; j++) {
        house[i][j] += 2;
    }
  }
}

void turnOn(int x1, int y1, int x2, int y2) {
  printf("In turnOn.\n");
  for(int i = x1; i <= x2; i++) {
    for(int j = y1; j <= y2; j++) {
        house[i][j] += 1;
    }
  }
}

void turnOff(int x1, int y1, int x2, int y2) {
  printf("In turnOff.\n");
  for(int i = x1; i <= x2; i++) {
    for(int j = y1; j <= y2; j++) {
      if(house[i][j] == 0) {
        house[i][j] = 0;
      } else {
        house[i][j] -= 1;
      }
    }
  }
}

int countOn() {
  int numLightsOn = 0;

  for(int i = 0; i < 1000; i++) {
    for(int j = 0; j < 1000; j++) {
        numLightsOn += house[i][j];
    }
  }

  return numLightsOn;
}

void run() {
  FILE *inputFileP;
  char cmd[9];
  int x1, y1, x2, y2;

  inputFileP = fopen("input.txt", "r");

  if (inputFileP == NULL) {
    fprintf(stderr, "Can't open input file input.txt!\n");
    exit(1);
  }

  while(fscanf(inputFileP, "%s%d,%d through %d,%d", cmd, &x1, &y1, &x2, &y2) != EOF) {

    if(strcmp(cmd, "toggle") == 0) {
      toggle(x1, y1, x2, y2);
    } else if(strcmp(cmd, "on") == 0) {
      turnOn(x1, y1, x2, y2);
    } else if(strcmp(cmd, "off") == 0) {
      turnOff(x1, y1, x2, y2);
    }

    printf("cmd1: %s, x1: %d, y1: %d, x2: %d, y2: %d\n", cmd, x1, y1, x2, y2);
  }

  printf("Total brightness of lights: %d\n", countOn());
}

int main() {
  run();
  //toggle 0,0 through 999,999 would increase the total brightness by 2000000
  //turnOff(0, 0, 0, 0);
  //printf("countOn: %d\n", countOn());
  return 0;
}
