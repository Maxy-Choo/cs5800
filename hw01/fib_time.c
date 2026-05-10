#include <stdio.h>
#include <time.h>
#include <stdlib.h>

#define LIMIT 100

int fib_recursive(int n) {
  if (n <= 1) {
    return n;
  }
  return fib_recursive(n-1)+fib_recursive(n-2);
}

int fib_array(int n) {

  if (n <= 1) {

    return n;
  }
  int* arr = (int*)malloc(LIMIT*sizeof(int));
  if (arr == NULL) {
    return -1;
  }
  arr[0] = 0;
  arr[1] = 1;
  for (int i=2; i<=n; i++) {

    arr[i] = arr[i-1]+arr[i-2];
  }
  int res = arr[n];
  free(arr);
  return res;
}

int fib_compressed(int n) {

  if (n <= 1) {

    return n;
  }
  int s0 = 0;
  int s1 = 1;
  for (int i=2; i<=n; i++) {

    int temp = s0+s1;
    s0 = s1;
    s1 = temp;
  }
  return s1;
}

int main() {
  clock_t start, end;
  for (int i=1; i<=20; i++) {

    printf("fib(%d):\n", i*5);
    start = clock();
    fib_recursive(i*5);
    end = clock();
    printf("Recursive Time cost: %.2f seconds\n", (double)(end-start)/CLOCKS_PER_SEC);
    
    start = clock();
    fib_array(i*5);
    end = clock();
    printf("Array Time cost: %.2f seconds\n", (double)(end-start)/CLOCKS_PER_SEC);

    start = clock();
    fib_compressed(i*5);
    end = clock();
    printf("Compressed Time cost: %.2f seconds\n\n", (double)(end-start)/CLOCKS_PER_SEC);
  }
  return 0;
}
