#include<stdio.h>
#include<stdlib.h>

/*function definition*/
void test0(int *a, int *b){
  *b = *a + *b;
}

void test1(int &a, int &b){
  b = a + b;
}

int main()
{

  int a = 10;
  int b = 10;
  test0(&a,&b);
  printf("b = %d\n", b);

  test1(&a,&b);
  printf("b = %d\n", b);
  
}
