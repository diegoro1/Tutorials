// supper basic stuff, like looking at variables to make sure everything is C/java
// like which looks like so!

using System;

namespace FirstConsoleApp
{
    class Program
    {
        static void Main(string[] args)
        {
            // cw tab gets Console.WriteLine("");
            Console.WriteLine("Hey! I am alive!!");
            Console.WriteLine("Press enter to continue!");

            // lets look at strings!
            string str = "This is great!";
            Console.WriteLine(str + "but is it really?"); //same as java!


            // lets look at something even more interesting
            // the byte variable!
            // an 8 bit variable
            // pretty much an unsign int that ranges from 0 -255
            byte coolByte= 10; //can be from anywhere from 0 - 255 (256#s)


            // lets look at something more familiar
            // char variable
            char coolChar = 'C'; //16 bit

            // it is aslo possible to get a straight ASCI number as a char
            char fancy = (char)65;
            Console.WriteLine("wow this is a fancy: "+ fancy); // facy is a 'A' :)


            // lets look at a short
            // pretty c like stuff
            short shawty = 65; //16 bit signed int


            // the daddy of all varibles
            int fatherHimself = -1000000000; // 32 bit of course
            uint crazy = 999999999;          // 32 bit but more to work with


            // floats and doubles
            float pie = 3.14f; // end with f to tell VS it is not a double :( 32bit
            double realPie = 3.141592653589793; // 64 bit
            decimal preciss = (decimal)3.141592653589793908080809898099; // 128bit wow!


            // more on strings
            string name = "none of your busniness";
            Console.WriteLine(name.ToUpper());

            // bool
            bool tru = false;
            bool fal = true;

            // a nice trick to get a max value
            int max = int.MaxValue;
            Console.WriteLine(max); // should be 2147483647 :)
            int min = int.MinValue;
            Console.WriteLine(min); // should be -2147483648

            // lets convert using parse
            int cool = int.Parse("100");
            Console.WriteLine(cool);

           
        }
    }
}
