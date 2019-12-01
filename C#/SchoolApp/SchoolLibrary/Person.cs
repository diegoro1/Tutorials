using System;
using System.Text

namespace SchoolLibrary
{
    public abstract class Person
    {
        private string FirstName;
        private string LastName;


        // Getter and Setter methods
        public void SetFirstName(string _firstName)
        {
            FirstName = _firstName;
        }
        public string GetFirstname()
        {
            return FirstName;
        }

        public void SetLastName(string _lastName)
        {
            LastName = _lastName;
        }
        public string GetLastName()
        {
            return LastName;
        }

        public abstract float ComputeGradeAverage();

        public virtual string SendMessage(string message)
        {
            return "Hey!";
        }
    }
}
