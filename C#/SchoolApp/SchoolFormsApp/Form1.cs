using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using SchoolLibrary; // to use the code we have been making

namespace SchoolFormsApp
{
    public partial class Form1 : Form
    {
        private void label9_Click(object sender, EventArgs e)
        {

        }

        private void label10_Click(object sender, EventArgs e)
        {

        }

        private void label12_Click(object sender, EventArgs e)
        {

        }

        private void btnPush_to_test_Click(object sender, EventArgs e)
        {
            School testSchool = new School(txtSchool_name.Text, txtNumber.Text); // gets values from text boxes
            MessageBox.Show(testSchool.ToString());
        }
    }
}
