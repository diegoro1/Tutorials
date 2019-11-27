// using string manipulation methods

using System;
namespace Strings
{
    public class Strings
    {
        public Strings()
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

            }
        }
    }
}
