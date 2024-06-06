# A tool let your Repo daily auto commit.
----------------------------------------------------------------------------

## How to use?

Follow the step：

1. clone this Repo：
    ```sh
    https://github.com/codingYuYu/dailyAutoCommit.git
    ```
2. install gitpython
   ```sh
   pipenv install
   ```
   or if you don't have pipenv you could install pipenv
   ```
   pip install pipenv
   ```
   or install it directly on the local system.
   ```sh
   pip install gitpython
   ```
3. Replace /path/to/your/repository with the path to your Git project.

4. Linux:
   ```sh
   crontab -e
   ```
   ```sh
   0 0 * * * /usr/bin/python3 /path/to/your/script.py
   ```
   ※ min(0-59) / hour(0-24) / day / month / weekday(1-7) and * mean every

   Windows:
   1. Open the Task Scheduler.
   2. Create a new Basic Task.
   3. For the Trigger, set it to run the task Daily.
   4. For the Action, select "Start a program".
   5. 
   ```sh
   C:\Path\To\python.exe C:\Path\To\your\script.py

   ```
---------------------------------------------------------------------------
## How to stop?
Linux:
1. add #
```sh
crontab -e
```
```sh
# 0 0 * * * /usr/bin/python3 /path/to/your/script.py
```
2. check
```sh
crontab -l
```

Windows:
1. Open the Task Scheduler.
2. In the left pane, locate the "Task Scheduler Library" and find the task you created.
3. Right-click on the task, then choose either "Disable" or "Delete".
4. Selecting "Disable" will temporarily stop the task, but keep it available to be re-enabled later.
5. Choosing "Delete" will permanently remove the task.

-------------------------------------------------------------------------

Note:

1. Ensure that the remote URL of your Git repository is set to the SSH format, and that your computer has been properly configured with an SSH key, so that the script can automatically push changes.

2. If necessary, you can add error handling and logging functionalities to the script, to better track the execution status of the script.