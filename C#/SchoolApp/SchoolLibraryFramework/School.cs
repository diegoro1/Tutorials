using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace SchoolLibrary
{
    public class School
    {
        private string SchoolName;
        private string SchoolAddress;
        private string SchoolCity;
        private string SchoolState;
        private string SchoolZip;
        private string PhoneNumber;

        private string _twitterAddress;
        public string TwitterAddress
        {
            get { return _twitterAddress; }
            set
            {
                if (value.StartsWith("@"))
                    _twitterAddress = value;
                else
                    throw new Exception("Wrong twitter address.");
            }
        }

        public School(string _schoolName, string _phoneNumber)
        {
            SchoolName = _schoolName;
            PhoneNumber = _phoneNumber;
        }

        public override string ToString()
        {
            StringBuilder sb = new StringBuilder();
            sb.Append(SchoolName);
            sb.Append(", ");
            sb.Append(PhoneNumber);

            return sb.ToString();
        }
    }
}