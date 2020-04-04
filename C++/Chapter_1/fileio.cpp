#include <iostream>
#include <fstream>
#include <vector>
# include <string>

int  main(void)
{   
    int i, j, len;
    // instantiating an ofstring object and passes file name to it
    std::ifstream ifp ("input.txt");
    std::ofstream ofp ("output.txt");
    if (!ifp.is_open() || !ofp.is_open())
    {
        std::cerr << "Could not open input.txt \n";
        exit(0);
    }

    // where string will be stored
    std::vector<std::string> input;

    // creating a string to be used as a buffer
    std::string buffer;

    while (ifp >> buffer)
    {
        input.push_back(buffer);
    } 

    // something cool I found in stackoverflow (auto) :)
    // kind of makes me wanna cry of OCD but I'll let it fly in the for loops
    // this changes all the strings in the vector to uppercase and places it in output.txt
    for (auto &i : input)
    {   
        len = i.length();
        for (j = 0; j < len; j++)
            i[j] = toupper(i[j]);
        
        ofp << i << "\n";     
    }

    ofp.close();
    ifp.close();
    return 0;
}