#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <math.h>

typedef struct {

  int q;
  int r;
} Result;

Result divide(int x, int y) {
  Result res;
  if (x==0) {
    res.q = 0;
    res.r = 0;
    return res;
  }

  Result prev = divide(x/2, y);
  res.q = 2*prev.q;
  res.r = 2*prev.r;

  if (x%2==1) {
    res.r=res.r + 1;
  }
  if (res.r>=y) {
    res.r = res.r - y;
    res.q = res.q + 1;
  }
  return res;
}

int main() {
  for (int i=25; i<30; i++) {
    int a = (int)pow(2, i);
    int b = rand() % a;
    Result res1 = divide(a, b);
    int q = a / b;
    int r = a % b;
    printf("x=%d, y=%d\n", a, b);
    printf("Divide function result: %d, %d\n", res1.q, res1.r);
    printf("Built-in function result: %d, %d\n\n", q, r);
  }

  clock_t start, end;
  for (int i=1; i<=30; i++) {
    int x = (int)pow(2, i);
    int y = rand() % x;
    start = clock();
    Result res = divide(x, y);
    end = clock();
    printf("%d div %d = %d reminder %d, time usage: %.2f\n", x, y, res.q, res.r, (double)(end-start));
  }

  return 0;
}
