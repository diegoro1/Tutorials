#include <iostream>
#include <string>

void print(int a)
{
    // this is for exp purpose only! (cout is a lot better)
    printf("%d\n", a);
}

void print(std::string a)
{
    std::cout << a << "\n";
}

void print(double a)
{
    printf("%lf\n", a);
}

int main(void)
{
    print(1);
    print(100.1);
    print("One");
    return 0;
}