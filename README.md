# Intern Recruit Test for GMRIT

**Prerequisites**

Before you begin the task, ensure you have the following available with you.

1. You need an PC running Ubuntu operating system to complete this task within the timeframe. We recommend Ubuntu 14.04 or higher.
2. Good & uninterrupted Internet Connectivity. Access to Google.com, Stack Overflow, w3schools.com etc.
3. Individual Github account.

**Also, note these points before you begin the test:**

1. Perform this task as an individual only. Though you will work with a team during your internship, this particular task doesn't require any team activity to solve. 
2. Do not ask any external person, friend or a relative for a solution or advice during the test period. You should find the solution to the given task by yourself **only**. The task is simple and basic for the kind of person we are looking for. If you are unable to finish the task, even though you complete this particular task by gathering solution made up by someone else, you are likely to be terminated from the internship as you will have to do similar task on a daily basis and it is not practical for you to ask the same source for the solutions each day.
3. Complete this task within 120 minutes from when you begin the test.

**Steps to complete the tasks:**

Clone this repository on to your github account.

- Fork the repository to your own github account.
- Use "git clone repo_name" to clone on to your PC using Terminal or clone using the Github desktop app.
- Create a new branch with the name in the format: rollnumber_yourfullname. (Example: "13341A0586_ramharsha")

**Task 01:** Write a python program to extract only links from the .html page included in this repo into a new .txt file.

Note: 
- Every link should be appended by \n so that links are posted in a new line.

Tip: 
- All the links can be found in one tag format.

This is the end of Task 01.

**Task 02:** Create a database and populate with data.

1. In the same python file you used earlier in the previous task, write commands to 

- Create a database with any name you wish
- Create a table in the database with the name "user".

The table must contain three columns named as userid, interestid, interestname.

| interestid                           | interestname | userid                               |
|:---     |:---: |---:|
| fde29dc7-0d46-4949-954a-46c60de411a5 | Projects     | 40b0f97a-5e21-4250-b016              |

2. Populate the table randomly with 100,000 rows.

Note: 
- Consider interestnames to be: Projects, Startups, Travel, Food, Music, Pets, Relationships.
- Column userids should have different uuid4 for each row.
- Column interestid must fill a hashed data of the userid that is generated. Use md5 as the hashing technique.

Tip: 
- Google uuid4 to understand what it means.
- Google how to import md5 implementation.

This is the end of Task 02.

Commit all the files and create a pull request to submit your work.
