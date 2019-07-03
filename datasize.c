#include<stdlib.h>
#include<stdio.h>

int main()
{
  int a=32;
  long int b = 32;
  float c = 32;
  double d = 32;
  printf("size of int is %ld bytes\n", sizeof(a));
  printf("size of long int is %ld bytes\n", sizeof(b));
  printf("size of float is %ld bytes\n", sizeof(c));
  printf("size of double is %ld bytes\n", sizeof(d));
}
