# AWS Mini Project

## Introduction
This project involves creating a simple webpage to check a timetable. The webpage will utilize resources provided by **Amazon Web Services (AWS)** to ensure scalability and reliability.

---

## Steps:

### Step 1: Launch an EC2 Instance

1. **Instance Name:**
   - Use your name as the instance name for easy identification.

2. **Choose AMI:**
   - Select **Ubuntu** as the Amazon Machine Image (AMI).

3. **Create a Key Pair:**
   - Create a new key pair during the instance setup to securely connect to the instance.
   - Download the `.pem` file and keep it safe as it will be required for SSH access.


### Step 2: Set Up an EC2 Instance

   - While launching the instance, create or modify a **security group** to allow the necessary traffic:
     - **Port 80:** For HTTP traffic (webpage access).
     - **Port 22:** For SSH access.
     - **Port 443:** For HTTPS traffic (secure connections).
     - **Port 5432:** For PostgreSQL.
     - **Port 8000:** For custom application access.
     - **All Traffic:** (Use only for testing; restrict in production environments).

### Step 3: Set Up RDS PostgreSQL

1. **Choose Database Engine:**
   - In the **RDS Console**, select **PostgreSQL** as the database engine.

2. **Select DB Instance Type:**
   - Choose a **Single DB Instance** for simplicity and cost-effectiveness.

3. **DB Instance Identifier:**
   - Use your name as the **DB Instance Identifier** for easy identification.

4. **Credentials Management:**
   - Select **Self Managed** for credentials management.
   - Create a strong password for the database administrator (master user).

5. **Connectivity:**
   - Configure the database to connect with an EC2 compute resource:
     - Choose the EC2 instance you set up earlier for connectivity.

### Step 4: Connect to EC2 Instance Using MobaXterm

1. **Open MobaXterm:**
   - Launch MobaXterm on your system.

2. **Create a New SSH Session:**
   - Click on `Sessions` and select `New Session`.
   - Choose `SSH` as the session type.

3. **Remote Host:**
   - Enter your **Public IPv4 address** in the **Remote host** field.
     - You can copy the Public IPv4 address from your EC2 instance in the AWS Console.

4. **Advanced SSH Settings:**
   - Tick the box for **Use private key**.
   - Browse and select your `.pem` key file created earlier.

5. **Start the Session:**
   - Click **OK** to initiate the connection.
   - Once connected, you will be prompted to **login as**:
     - Enter `ubuntu` as the username (since you are using an Ubuntu instance).

### Step 5: Update EC2 and Install Dependencies

1. **Update EC2 Instance:**
   - Run the following command to update the package list:
     ```bash
     sudo apt update
     ```

2. **Install Necessary Packages:**
   - Run the following command to install Python 3, pip, and PostgreSQL client:
     ```bash
     sudo apt install python3 python3-pip postgresql-client -y
     ```

### Step 6: Connect to RDS PostgreSQL

1. **Connect to the RDS Instance:**
   - Use the following command to connect to your RDS PostgreSQL instance:
     ```bash
     psql -h <RDS_End_Point> -U postgres -d postgres
     ```
   - Replace `<RDS_End_Point>`, `<RDS_User>`, and `<RDS_Database_Name>` with your actual RDS endpoint, username, and database name.
   - In this case, the **RDC_User** and **RDS_Database_Name** will both be `postgres`.
   - You can find the **RDS endpoint** in the **RDS Console** under the **Connectivity & Security** section. Copy the **Endpoint** (not the port), which is used in the connection command.

2. **Enter the Database Password:**
   - When prompted, enter the **database password** that you created during the RDS setup.

3. **Create Your Database:**
   - If the connection is successful, you will see the prompt: `postgres=>`.
   - Now, create a new database with your name using the following query:
     ```sql
     CREATE DATABASE hamidulla;
     ```
   - After creating the database, switch to it with the following command:
     ```sql
     \c hamidulla;
     ```
4. **Success Message:**
   - If the operation is successful, you will see the prompt: `your_name=>`.

5. **Create a Table:**
   - Now, create a table using `Timetable` as the table name with the following query:
     ```sql
     CREATE TABLE Timetable ( 
         course_name VARCHAR(100),
         room INTEGER,
         day VARCHAR(20),
         time VARCHAR(20)
     );
     ```

6. **Insert Data into the Table:**
   - Insert the following sample data into your table:
     ```sql
     INSERT INTO Timetable (course_name, room, day, time) VALUES 
         ('Mathematics for Computer Science', 103, 'Monday', '9:30 AM'),
         ('Operating Systems', 112, 'Monday', '11:30 AM'),
         ('Python Programming', 205, 'Tuesday', '9:30 AM'),
         ('Java Programming', 213, 'Tuesday', '11:30 AM'),
         ('IT Project Management', 308, 'Wednesday', '2:00 PM'),
         ('Network Principles', 312, 'Wednesday', '4:30 PM'),
         ('Systems Analysis and Design', 415, 'Thursday', '9:30 AM'),
         ('Computer Languages', 325, 'Thursday', '11:30 AM'),
         ('Social Engineering', 256, 'Friday', '2:00 PM'),
         ('Computer and Information', 309, 'Friday', '4:30 PM');
     ```

7. **Check the Data:**
   - Use the following command to check if the data was successfully inserted into the table:
     ```sql
     SELECT * FROM Timetable;
     ```

8. **Exit SQL:**
   - To exit the SQL session, use the following command:
     ```sql
     \q
     ```

### Step 7: Create Project Directory

1. **Create Project Directory:**
   - Run the following command to create a project directory and navigate into it:
     ```bash
     mkdir my_project
     cd my_project
     ```

2. **Create Python File:**
   - Create a Python file called `app.py` in the `my_project` directory using the following command:
     ```bash
     nano app.py
     ```

3. **Create Templates Directory:**
   - Now, create a directory named `templates` to hold your HTML files:
     ```bash
     mkdir templates
     cd templates
     ```

4. **Create HTML Files:**
   - Create the `index.html` file inside the `templates` directory:
     ```bash
     nano index.html
     ```
   - Similarly, create the `timetable.html` file:
     ```bash
     nano timetable.html
     ```

5. **Return to the Project Directory:**
   - Once you've created the necessary files, return to the main project directory:
     ```bash
     cd ..
     ```

### Step 8: Set Up Python Virtual Environment

1. **Install `python3.12-venv`:**
   - First, install the `python3.12-venv` package to ensure that you can create a virtual environment. Run the following command:
     ```bash
     sudo apt install python3.12-venv
     ```

2. **Create and Activate Virtual Environment:**
   - After installing the package, create a Python virtual environment by running:
     ```bash
     python3 -m venv venv
     ```
   - Activate the virtual environment with the following command:
     ```bash
     source venv/bin/activate
     ```

3. **Install Python Dependencies:**
   - Upgrade `pip` to the latest version:
     ```bash
     pip3 install --upgrade pip
     ```
   - Install the necessary Python dependencies:
     ```bash
     pip3 install flask psycopg2-binary
     ```

4. **Install `pg8000`:**
   - To use an alternative PostgreSQL database adapter, install `pg8000`:
     ```bash
     pip install pg8000
     ```

5. **Disable Firewall (Optional):**
   - If you need to disable the firewall for testing purposes, you can run the following command:
     ```bash
     sudo ufw disable
     ```

6. **Run Flask Application:**
   - Finally, to run the Flask application, use this command:
     ```bash
     python app.py
     ```
    - The Flask development server will start, and you can access your application by opening your web browser and navigating to `http://<Public IPv4 address of your instance>:8000/`.