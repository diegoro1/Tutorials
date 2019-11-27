// using string manipulation methods

using System;
using System.Text;

namespace Strings
{
    class Strings
    {
        static void Main(String[] args)
        {
            string random1 = "WoooWOWOWOWooString";
            String random2 = "yeahhh!11123";
            string spaceEnd = "extra space here->   ";
            string spaceStart = "  <-space here";
            string nospace = " s p a c e ";

            Console.WriteLine("before: " + spaceEnd + "After: " + spaceEnd.TrimEnd());
            Console.WriteLine("before: " + spaceStart + "After: " + spaceStart.TrimStart());
            Console.WriteLine("before: " + nospace + "After: " + nospace.Trim());

            // this method breaks down strings
            Console.WriteLine(random1.Substring(4,3) + "!");

            // lets take a look at string builder
            StringBuilder str = new StringBuilder();
            String realStr;

            str.Append("Hello,");
            str.Append("world!");
            realStr = str.ToString();   // gotta covert SB to string                                    
            Console.WriteLine(realStr);

            // changing up the game with appendLine
            str = new StringBuilder();
            str.AppendLine("oh look!");
            str.Append("I am down here!");

            realStr = str.ToString();
            Console.WriteLine(realStr);





        }
    }
}