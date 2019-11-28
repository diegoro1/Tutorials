using System;
using System.Text;

namespace MathFuncs
{
    class Program
    {
        enum days { Monday, Tuesday, Wednesday, Friday }; // notice no equals!

        static void Main(string[] args)
        {
            Console.WriteLine(string.Format("Assolute value of -2: {0}", Math.Abs(-2)));
            Console.WriteLine(string.Format("2^3: {0}", Math.Pow(2, 3)));
            Console.WriteLine(string.Format("Floor 3.9: {0}", Math.Floor(3.9)));
            Console.WriteLine(string.Format("Ceiling 3.9: {0}", Math.Ceiling(3.9)));
            Console.WriteLine(string.Format("Round 3.9: {0}", Math.Round(3.9)));

            // that's fancy and all but what about constants?
            const float pi = 3.14f;
            //pi = 3; this is BAD! :(

            // how about the cool enums?
            string today = days.Monday.ToString();
            Console.WriteLine("Topday is: " + today);

        } 
    }
}
