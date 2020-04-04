#include <iostream>
#include <string>
#include <vector>

class Airplane
{

    public:
        std::string name;
        int id;

};

int main(void)
{
    Airplane plane;
    plane.id = 1;

    std::vector<Airplane> airplanes;
    airplanes.push_back(plane);

    std::cout << plane.id << "\n";

    return 0;
}