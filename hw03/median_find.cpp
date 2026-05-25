#include <iostream>
#include <vector>
#include <algorithm>

use namespace std;

int median_find(vector<int> arr) {
  

}

int main() {
  vector<int> array = {1,2,6,3,4,8,20,7,5,16};
  cout << "Array: {";
  for (int x : array) {
    cout << x << ", ";
  }
  cout << "}\n";
  int ans = median_find(array);
  cout << "The median value of the array is: " << ans << "\n";
  return 0;
}
