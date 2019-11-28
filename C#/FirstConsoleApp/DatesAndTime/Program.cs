using System;
using System.Text;

namespace DatesAndTime
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine(DateTime.Now + ", This will always change!");
            DateTime birthday = new DateTime(1996, 9, 21);
            Console.WriteLine("My birday!: " + birthday);

            // lets find out how many days I am!
            TimeSpan difference = DateTime.Now - birthday;
            Console.WriteLine(string.Format("I am {0} days old", difference.Days));
        }
    }
}
