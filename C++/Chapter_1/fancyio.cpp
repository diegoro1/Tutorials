#include <iostream>
#include <fstream>
#include <vector>

int main(void)
{
    int i, j, len;
    std::vector<std::string> input;
    std::string buffer;

    std::ifstream ifp ("fancy_input.txt");
    std::ofstream ofp ("fancy_output.txt");

    if (!ifp.is_open() || !ofp.is_open())
    {
        std::cerr << "failed to open file\n";
        exit(0);
    }

    while ()


    ofp.close();
    ifp.close();
    return 0;
}   