using System;
namespace SchoolLibrary
{
    public class Student : Person
    {
        public enum GradeLevels { Freshman, Sophomore, Junior, Senior}
        private GradeLevels GradeLevel;

        // getter, setter
        public void SetGradeLevel(GradeLevels _gradeLevel)
        {
            GradeLevel = _gradeLevel;
        }
        public GradeLevels GetGradeLevel()
        {
            return GradeLevel;
        }

        public override float ComputeGradeAverage()
        {
            return 4.0f;
        }

        public override string SendMessage(string message)
        {
            String original = base.SendMessage(message);
            return original.ToUpper();
        }
    }
}
