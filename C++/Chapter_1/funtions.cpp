#include <iostream>
#include <cmath>
#include <ctime>
#include <vector>
#include <stdlib.h>
#include <array>

using namespace std; // this makes names from namespace std visible w/out std::

double square(double x)
{
    return x * x;
}

// all the qt stuff from CS1
double power(int base, int exponent)
{
    if (exponent == 1)
        return base;
    return base * power(base, exponent - 1);
}

// all the cude stuff I remeber from CS1 ^ 2
double factorial(int a)
{
    if (a < 2)
        return 1;
    return a * factorial(a - 1);
}

vector<int> fill(vector<int> data)
{   
    int i;
    for (i = 0; i < 10; i++)
    {
        data.push_back(i * 10);
    }

    return data;
}

void super_fill(vector<int> &data)
{
    int i;
    for (i = 0; i < 10; i++)
    {
        data.push_back(i * (rand()%10 + 1));
    }
}

void printSTL(array<int, 4> array)
{
    int i, len = array.size();

    for (i = 0; i < len; i++)
        printf("Array[%d] = %d\n", i, array[i]);

    cout << "\n";
}

// dont trust shitty devs!
void nastyPrint(array<int, 4> &array)
{
    int i, len = array.size();

    for (i = 0; i < len; i++)
        printf("Array[%d] = %d\n", i, array[i]);
    
    // oh no...
    array[0] = 400000;
    cout << "\n";
}

void compareWithPrint(vector<int> a, vector<int> b)
{
    int i, len = a.size();
    for (i = 0; i < len; i++)
    {
        printf("a[%d] = %d | b[%d] = %d\n", i, a[i], i, b[i]);
    }
}

int main(void)
{
    int i, x;

    srand(time(NULL));

    /*  
    cout << "Insert number to be squared: ";
    cin >> x;
    cout << "The square of " << x << " is " << square(x) << "\n";
    */

    // using math funtion
    cout << "2^3 = " << pow(2,3) << "\n";
    cout << "fancy 2^3 = " << power(2,3) << "\n";
    cout << "5! = " << factorial(5) << endl;
    cout << "Random Number " << (rand() % 10) << endl;

    std::vector<int> data;

    // pops 10 ints to stack
    for (i = 0; i < 10; i++)
    {
        data.push_back(i * (rand()%10 + 1));
        printf("Vector data[%d] = %d\n", i, data[i]);
    }

    // size() is constant runtime!
    // delets all elements
    int len = data.size();
    for (i = 0; i < len; i++)
    {
        printf("Vector data[%d] = %d is getting popped!\n", i, data[i]);
        data.pop_back();
    } 

    cout << "fancy stuff happening ------------------------------------------------\n";

    // unlike arrays, vectors are passed by value (& needed to pass by ref)
    // by value! returning a vector! how fancy!
    data = fill(data);
    
    // delets all elements
    len = data.size();
    for (i = 0; i < len; i++)
    {
        printf("Vector data[%d] = %d is getting popped!\n", i, data[i]);
        data.pop_back();
    } 

    // by ref, super fancy
    super_fill(data);

    // delets all elements
    len = data.size();
    for (i = 0; i < len; i++)
    {
        printf("Vector data[%d] = %d is getting popped!\n", i, data[i]);
        data.pop_back();
    }

    cout << "\n\n";

    // the STL array
    // this is interesting, an array wrapped around an object
    // how to I fell about this? 5/10
    // will google why
    // the C in me is hurting
    // It would probably been a better idea to learn C++ first
    // but with time, we will C... 
    // passed by value btwe

    // STL array
    std::array<int, 4> randomAF = {3, 4, 3, 1};

    printSTL(randomAF);
    nastyPrint(randomAF);
    printSTL(randomAF);


    // this is gonna make you cridge, but it's ok to be afraid
    std::vector<int> things;
    things.push_back(10); things.push_back(11); things.push_back(12);

    // hold on cause this shit actually works
    std::vector<int> stuff = things;

    compareWithPrint(things, stuff);

    // this is that shitty thing that python/java does, this should have been left in the trash.
    // range for-loops...

    for (int i : things)
        cout << "things -> " << i << "\n";
    return 0;
}