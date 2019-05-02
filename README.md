 #  Logs Analysis Project
This project is the third project in the Full Stack Web Development Nanodegree.  In this project, we explore a large database  with over a million rows.  We build an internal reporting tool that will use information from the database to discover what kind of articles the newspaper site's readers prefer.  The database contains newspaper articles, as well as the web server log for the site.  The log has a database row for each time a reader loaded a web page.  Using that information, my code answers questions about the site's user activitiy.

The program I write in this project runs from the command line and doesn't take any input from the user.  Instead, it connects to that database, uses SQL queries to analyze the log data, and prints out the answers to three questions.  I build and refine complex queries and use them to draw business conclusions from the data.

The database includes three tables: 
- Authors
- Articles
- Log

Enjoy running the program!

 ##  Installation:

   Download or clone the LogsAnal folder, including all files.  You will need the newsdata.sql database file, which you can download from the Udacity website.  

 ##  You need these installed to run the program:
  - Vagrant 
  - Python 3
  - Virtual Box

 ##  Usage:
* Download the newsdata.sql file from the Udacity website.  You will need to unzip the file after downloadLaunch Vagrant with 'vagrant up' ing it.  
* Move newsdata.sql into the Vagrant directory, which is shared with your virtual machine (VM).  
* Launch Vagrant with 'vagrant up' 
* Log into Vagrant with 'vagrant ssh'
* Load the data from the newsdata.sql file with this command on your command line: 'psql -d news -f newsdata.sql'
* After you log into Vagrant, navigate to the folder that contains the newsdata.sql file and the LogsAnal.py file and run 'python3 LogsAnal.py'
* Enjoy!

 ##  Issues/Known Bugs:
_None._
_If you find any, please let me know :)_

 ##  Frequently Asked Questions:

1.   How can I see the output from your questions?
*Run the program as described above and the output will appear automatically below where you typed in the command to open and run the LogsAnal.py file *

 2.  What will happen after the results show?
 *The command line prompt will return.*

 ##  Contributing:
 *Thanks to Udacity Full Stack Web Development Nanodegree course for helping me learn skills to code this project.*

 ##  Licensing Information:
   MIT License - open source! *Please see the License.txt file for details.*
