namespace SchoolFormsApp
{
    partial class Form1
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            this.txtSchool_name = new System.Windows.Forms.Label();
            this.txtAddress = new System.Windows.Forms.Label();
            this.txtCity = new System.Windows.Forms.Label();
            this.txtState = new System.Windows.Forms.Label();
            this.txtZip = new System.Windows.Forms.Label();
            this.txtNumber = new System.Windows.Forms.Label();
            this.textBox7 = new System.Windows.Forms.TextBox();
            this.textBox8 = new System.Windows.Forms.TextBox();
            this.textBox9 = new System.Windows.Forms.TextBox();
            this.textBox10 = new System.Windows.Forms.TextBox();
            this.textBox11 = new System.Windows.Forms.TextBox();
            this.textBox12 = new System.Windows.Forms.TextBox();
            this.btnPush_to_test = new System.Windows.Forms.Button();
            this.SuspendLayout();
            // 
            // txtSchool_name
            // 
            this.txtSchool_name.AutoSize = true;
            this.txtSchool_name.Location = new System.Drawing.Point(14, 52);
            this.txtSchool_name.Name = "txtSchool_name";
            this.txtSchool_name.Size = new System.Drawing.Size(71, 13);
            this.txtSchool_name.TabIndex = 0;
            this.txtSchool_name.Text = "School Name";
            // 
            // txtAddress
            // 
            this.txtAddress.AutoSize = true;
            this.txtAddress.Location = new System.Drawing.Point(12, 77);
            this.txtAddress.Name = "txtAddress";
            this.txtAddress.Size = new System.Drawing.Size(45, 13);
            this.txtAddress.TabIndex = 1;
            this.txtAddress.Text = "Address";
            // 
            // txtCity
            // 
            this.txtCity.AutoSize = true;
            this.txtCity.Location = new System.Drawing.Point(12, 99);
            this.txtCity.Name = "txtCity";
            this.txtCity.Size = new System.Drawing.Size(24, 13);
            this.txtCity.TabIndex = 2;
            this.txtCity.Text = "City";
            this.txtCity.Click += new System.EventHandler(this.label9_Click);
            // 
            // txtState
            // 
            this.txtState.AutoSize = true;
            this.txtState.Location = new System.Drawing.Point(12, 121);
            this.txtState.Name = "txtState";
            this.txtState.Size = new System.Drawing.Size(32, 13);
            this.txtState.TabIndex = 3;
            this.txtState.Text = "State";
            this.txtState.Click += new System.EventHandler(this.label10_Click);
            // 
            // txtZip
            // 
            this.txtZip.AutoSize = true;
            this.txtZip.Location = new System.Drawing.Point(13, 143);
            this.txtZip.Name = "txtZip";
            this.txtZip.Size = new System.Drawing.Size(22, 13);
            this.txtZip.TabIndex = 4;
            this.txtZip.Text = "Zip";
            // 
            // txtNumber
            // 
            this.txtNumber.AutoSize = true;
            this.txtNumber.Location = new System.Drawing.Point(12, 165);
            this.txtNumber.Name = "txtNumber";
            this.txtNumber.Size = new System.Drawing.Size(44, 13);
            this.txtNumber.TabIndex = 5;
            this.txtNumber.Text = "Number";
            this.txtNumber.Click += new System.EventHandler(this.label12_Click);
            // 
            // textBox7
            // 
            this.textBox7.Location = new System.Drawing.Point(94, 49);
            this.textBox7.Name = "textBox7";
            this.textBox7.Size = new System.Drawing.Size(100, 20);
            this.textBox7.TabIndex = 6;
            // 
            // textBox8
            // 
            this.textBox8.Location = new System.Drawing.Point(94, 74);
            this.textBox8.Name = "textBox8";
            this.textBox8.Size = new System.Drawing.Size(100, 20);
            this.textBox8.TabIndex = 7;
            // 
            // textBox9
            // 
            this.textBox9.Location = new System.Drawing.Point(94, 96);
            this.textBox9.Name = "textBox9";
            this.textBox9.Size = new System.Drawing.Size(100, 20);
            this.textBox9.TabIndex = 8;
            // 
            // textBox10
            // 
            this.textBox10.Location = new System.Drawing.Point(94, 118);
            this.textBox10.Name = "textBox10";
            this.textBox10.Size = new System.Drawing.Size(100, 20);
            this.textBox10.TabIndex = 9;
            // 
            // textBox11
            // 
            this.textBox11.Location = new System.Drawing.Point(94, 140);
            this.textBox11.Name = "textBox11";
            this.textBox11.Size = new System.Drawing.Size(100, 20);
            this.textBox11.TabIndex = 10;
            // 
            // textBox12
            // 
            this.textBox12.Location = new System.Drawing.Point(94, 162);
            this.textBox12.Name = "textBox12";
            this.textBox12.Size = new System.Drawing.Size(100, 20);
            this.textBox12.TabIndex = 11;
            // 
            // btnPush_to_test
            // 
            this.btnPush_to_test.Location = new System.Drawing.Point(94, 209);
            this.btnPush_to_test.Name = "btnPush_to_test";
            this.btnPush_to_test.Size = new System.Drawing.Size(100, 24);
            this.btnPush_to_test.TabIndex = 12;
            this.btnPush_to_test.Text = "Push to Test";
            this.btnPush_to_test.UseVisualStyleBackColor = true;
            this.btnPush_to_test.Click += new System.EventHandler(this.btnPush_to_test_Click);
            // 
            // Form1
            // 
            this.ClientSize = new System.Drawing.Size(284, 261);
            this.Controls.Add(this.btnPush_to_test);
            this.Controls.Add(this.textBox12);
            this.Controls.Add(this.textBox11);
            this.Controls.Add(this.textBox10);
            this.Controls.Add(this.textBox9);
            this.Controls.Add(this.textBox8);
            this.Controls.Add(this.textBox7);
            this.Controls.Add(this.txtNumber);
            this.Controls.Add(this.txtZip);
            this.Controls.Add(this.txtState);
            this.Controls.Add(this.txtCity);
            this.Controls.Add(this.txtAddress);
            this.Controls.Add(this.txtSchool_name);
            this.Name = "Form1";
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.TextBox textBox3;
        private System.Windows.Forms.TextBox textBox1;
        private System.Windows.Forms.TextBox textBox2;
        private System.Windows.Forms.TextBox textBox4;
        private System.Windows.Forms.TextBox textBox5;
        private System.Windows.Forms.TextBox textBox6;
        private System.Windows.Forms.Label label2;
        private System.Windows.Forms.Label label3;
        private System.Windows.Forms.Label label4;
        private System.Windows.Forms.Label label5;
        private System.Windows.Forms.Label label6;
        private System.Windows.Forms.Label txtSchool_name;
        private System.Windows.Forms.Label txtAddress;
        private System.Windows.Forms.Label txtCity;
        private System.Windows.Forms.Label txtState;
        private System.Windows.Forms.Label txtZip;
        private System.Windows.Forms.Label txtNumber;
        private System.Windows.Forms.TextBox textBox7;
        private System.Windows.Forms.TextBox textBox8;
        private System.Windows.Forms.TextBox textBox9;
        private System.Windows.Forms.TextBox textBox10;
        private System.Windows.Forms.TextBox textBox11;
        private System.Windows.Forms.TextBox textBox12;
        private System.Windows.Forms.Button btnPush_to_test;
    }
}

