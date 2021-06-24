#ifndef _Utilities
#define _Utilities

#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <math.h>




int INFINIT();
int PERIOD();
int MIN(int d1, int d2, int d3, int d4);
int chooseFollowUpDelay(); 

const  char* getfield(char* line, int num);

const float getfield1(char* filecsv, int ln, int cl);


float minDIST(float n1, float n2, float n3);
float minDISTT(float n1, float n2);

float readWH(int item);

float readWV(int item);

float readWP(int item);

float readDIST0(int item);

float readDIST1(int item);

float readDIST2(int item);

float readDIST3(int item);

float readDIST4(int item);

float readDIST5(int item);

   
#endif
