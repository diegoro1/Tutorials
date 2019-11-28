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
            str.AppendLine("oh look!"); // like adding a new line character after 
            str.Append("I am down here!");

            realStr = str.ToString();
            Console.WriteLine(realStr);

            // string formatter
            // this is a bit like java but cooler

            string city = "Orlando";
            DateTime dateNow = DateTime.Now;
            float temperature = 15.4f;

            Console.WriteLine(string.Format("\nlocation: {0} \ndate: {1}\ntemperature: {2:0.00}\n", city, dateNow, temperature));

            // a cute way of writing numbers
            int population = 100000;
            Console.WriteLine("Population {0:0,0}", population);


            // lets say someone wrote a database with commas in it! OH NO!
            // how will we get the numerical values with all the numbers are strings
            // with commas all of the place! like 1300 is 1,300!
            // that's an easy fix!
            String problems = "12,400,433";
            int yourSmart = int.Parse(problems.Replace(",", ""));
            Console.WriteLine(yourSmart + " WOW YOU'R SMART! but i like the commas!");
            // that's easy!
            Console.WriteLine(string.Format("Here are the commas back!: {0:0,0}", yourSmart));

            // lets be a bit more careful with parse
            int moreNumbers;
            int.TryParse("3333", out moreNumbers);
            Console.WriteLine(moreNumbers);


        }
    }
}