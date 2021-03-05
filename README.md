# Daily-Git-Commit

Commit to repo every day for the perfect commit streak

## Requirments

`pip install -r requirements.txt`



## Setup

1. 	Download this repository.
2. 	Create your own repository on your GitHub account.
3. 	It's very important to first commit the `update_me.yaml` file first before you begin the daily commit.
4. 	That's really it.. Assuming your logged into git on your system it should work fine.

Now that your repository and git is setup, its time to set up the most important part. DAILY commit. Since the script handles all of the updates and processing, all we need to do is call that script. There are alot of ways to achieve this, depending on what operating system you are on. Below are instructions for both Windows and Linux solutions, you can do this how ever you feel. 

### Possible Issues

1.  If for some reason it doesn't commit, re-clone or merge the repository to your PC again. It's just a funny issue it has.

### Windows

I will be showing you how to set this up using task sceduler on windows.

1.  Open 'Task Scheduler' from search bar.
2.  Press 'Create Task...'.
3.  Name it: "Daily Git Commit" just so you know what it is later on, and not some wierd virus.
4.  I would suggest, to check both of the following: "Run with highest privileges" to insure no issues ever occure when reading and writing to files, and: "Run where user is logged on or not" Just so you never miss a day when your PC is logged out.
5.  Head over to the "Triggers" tab, and create a "New" trigger.
6.  Set the trigger to DAILY (or how ever you want :) ) and set the time how ever you want. Make sure the "Status" is: "Enabled"
7.  Next go to the "Actions" tab. (This is where we specify what program to run.
8.  Press "Browse" and go to the path of the `run.bat` script and double click it. There is no need for additional arguments. Press OK.
9.  There are a few additions settings you can change in the "Settings" tab, such as if the task fails restart it every couple seconds, maybe a network error. Run task ASAP. There is not more to setup, this is pretty much it for windows setup.

**NOTE**
- Make sure you edit the `run.bat` file to the correct paths.
- If for some reason, the directory changed/`run.bat` got renamed or deleted/or you deleted the project and re-downloaded. REPEAT step 8.
- If there are errors that occur, open up an issue and I will get it fixed ASAP.

### Linux

I will be using `crontab`.

1.  Open crontab with: `sudo crontab -e`
2.  Add the following line: `59 23 * * * cd /path/to/script/folder/ ; /usr/bin/env /usr/local/bin/python3.8 /path/to/script/main.py`
3.  Thats it! Make sure you save and exit.

Note. There may be git config issues, I solved them by generating a GitHub token in the developer settings. Using the github token as a login for git, make sure git is logged in your system.

Additional information about [crontab](https://crontab.guru)
## WHY?!

Only because I wanted to. I hate to see my git commit stats have gaps, and so I made this SUPER simple script to create a commit to this repository to bring up my commit streak :P, and to fill in the gaps where I don't commit on one day. Again this is just a silly project and has no purpose besides to 'cure my ocd' for a perfect commit streak :D. I hope if you have the same issue this script will help.

## BAN!?

Short answer: NO!

Detailed answer:
I asked this question on [stackoverflow](https://stackoverflow.com/questions/66496319/is-it-against-github-tos-to-make-commits-daily-with-gitpython), and any other question you have is answered there!

