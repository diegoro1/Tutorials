using System;
namespace SchoolLibrary
{
    public class Teacher : Person
    {
        private string Subject;


        // Getter and Setter methods
        public void SetSubject(string _subject)
        {
            Subject = _subject;
        }
        public string GetSubject()
        {
            return Subject;
        }

        public override float ComputeGradeAverage()
        {
            return 4.0f;
        }
    }    
}
