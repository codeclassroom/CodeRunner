#include <iostream>

using namespace std;
// calculate factorial of a number
long Fact(long);

int main () {
long x = 9, fact;
fact = Fact (x);
cout << "Factorial = " << fact;

return 0;
}

long Fact (long a) {
if (a == 0) return 1;
else return a * Fact (a - 1);
}