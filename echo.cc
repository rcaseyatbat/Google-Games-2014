
#include <iostream>
#include <cstdio>
#include <algorithm>
using namespace std;
int main() {
  // Set up the input and output files
  freopen("sample.in", "r", stdin);
  freopen("sample.out", "w", stdout);
  // Read in T
  int total_cases;
  cin >> total_cases;
  for (int case_number = 1; case_number <= total_cases; case_number++) {
    // Read in C and W
    int copies;
    string word;
    cin >> copies >> word;
    // Output the result
    printf("Case #%d:", case_number);
    for (int i = 0; i < copies; i++) {
      printf(" %s", word.c_str());
    }
    printf("\n");   // Move to the next line
  }
}