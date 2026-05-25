#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

// given two sorted arrays, return the value of kth element of their sorted union function unionkth(array1, array2, k)

// Part 1: design an algorithm using recursion.

int unionkth(int* p1, int size1, int* p2, int size2, int k) {
  // base case
  if (size1==0) {return p2[k-1];}
  if (size2==0) {return p1[k-1];}
  
  // recursion
  // calculate mid idxes
  int mid1 = size1/2;
  int mid2 = size2/2;
  // compare sum of mid idxes and k
  if (mid1+mid2 >= k) { // when sum of mid idxes >= k
    if (p1[mid1] >= p2[mid2]){ // when mid value of array1 >= mid value of array2
      return unionkth(p1, mid1, p2, size2, k); // cut latter half of array1, don't cut mid value itself
    } 
    else { // when mid value of array2 > mid value of array1
      return unionkth(p1, size1, p2, mid2, k); // cut latter half of array2, don't cut mid value itself
    }
    // k stays the same because we didn't cut the former part of an array.
  }
  else { // when sum of mid idxes < k
    if (p1[mid1] >= p2[mid2]){ // when mid value of array1 >= mid value of array2
      return unionkth(p1, size1, p2+mid2+1, size2-mid2-1, k-mid2-1); // cut former part of array2
      // cut mid value itself because it is guaranteed to be smaller than the kth element
    }
    else { // when mid value of array2 > mid value of array1
      return unionkth(p1+mid1+1, size1-mid1-1, p2, size2, k-mid1-1); // cut former part of array1
    }
    // k changes because we cutted the former part of anarray.
  }
}

// The join and sortalgorithm to proof the result of the recursion algorithm is correct.
int join_sort(int*p1, int size1, int*p2, int size2, int k) {
  vector<int> comb;
  while (size1 > 0 && size2 > 0) {
    if (p1[0] > p2[0]) {
      comb.push_back(p2[0]);
      p2++;
      size2--;
    } 
    else {
      comb.push_back(p1[0]);
      p1++;
      size1--;
    }
  }
  if (size1!=0){
    for (int i=0; i<size1; i++) {
      comb.push_back(p1[i]);
    }
  }
  else {
    for (int i=0; i<size2; i++){
      comb.push_back(p2[i]);
    }
  }
  return comb[k-1];
}


// Part 2: writing the iterating version to find the kth element of both arrays.

int iterate(int* p1, int size1, int*p2, int size2, int k) {
  // initialize binary search boundaries.
  int right1=size1;
  int right2=size2;
  int left1=0;
  int left2=0;

  // execute binary search
  // terminate when any pair of two boundaries meet,
  // representing the size of the array becomes 0.
  while (left1<right1 && left2<right2) {
    //mid points
    int mid1=(left1+right1)/2;
    int mid2=(left2+right2)/2;
    // logic similar to recursion algorithm
    if (mid1+mid2>=k) {
      if (p1[mid1]>p2[mid2]) {
        right1=mid1;
      }
      else {
        right2=mid2;
      }
    }
    else{
      if (p1[mid1]>p2[mid2]) {
        k=k-(mid2-left2+1);
        left2=mid2+1;
      }
      else {
        k=k-(mid1-left1+1);
        left1=mid1+1;
      }
    }
  }

  // if one pair of boundaries meet, return the kth element in the other array
  if (left1>=right1) {
    return p2[k-1];
  }
  else {
    return p1[k-1];
  }
}

// Part 3:
// Because both recursion and iterating algorithms doing binary search on both arrays.
// They do one binary search at each array at a time.
// The worst case is that they need to finish the whole binary search on both arrays.
// Therefore, T(n) = O(logm + logn).

int main() {
  vector<int> array1 = {1,4,5,7,8,10,11,15,16,20};
  vector<int> array2 = {2,3,4,6,7,8,10,12,15,17,18};
  cout << "Array1: {";
  for (int x : array1){
    cout << x << ", ";
  }
  cout << "}\n";
  cout << "Array2: {";
  for (int x : array2) {
    cout << x << ", ";
  }
  cout << "}\n";

  int k = 5;
  int ans = unionkth(array1.data(), array1.size(), array2.data(), array2.size(), k);
  int compare = join_sort(array1.data(), array1.size(), array2.data(), array2.size(), k);
  cout << "Part 1" << "\n";
  cout << "the kth element of two sorted arrays is: " << ans << "\n";
  cout << "the answer of the join and sort algorithm is: " << compare << "\n";
  int iter = iterate(array1.data(), array1.size(), array2.data(), array2.size(), k);
  cout << "Part 2" << "\n";
  cout << "the answer of the iterating algorithm is: " << iter << "\n";
  return 0;
}
