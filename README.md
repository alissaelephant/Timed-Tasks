    # Task Time Tracker
    #### Video Demo:  https://youtu.be/2VQcgD0QVro

   ## Description -

   If you or someone you know tends to procrastinate on repetitive tasks like chores, adminstrative duties at work, or even hygiene-related tasks this program might help.

   A common reason behind a lack of motiation to complete tasks is the perception of how much time and energy it will take. By timing yourself working through tasks, this helps your brain to stay focused on completing the task without distractions. By keeping a log of on average how long the task takes to complete, it simplifies the decision-making process to perform the task by framing the action as only X minutes with low effort, depending on how simplified the task is.

   ## Installations -

   There are necessary libraries in order to successfully run the Task TIme Tracker program. All required libraries are part of Python's standard libraries that will not require any pip installs.

   ### CSV

   Because task data is stored and updated within a CSV file, the CSV Python library will allow your program to add the desired task to the log while also keeping track of changing time averages and total amount of time spent on any given task.

   Additionally, the Writer functions from the CSV library are also needed to be imported by simply adding "from CSV import Writer." This allows the program to add new tasks the user wants to track time for in addition to adding time spent to the total time spent on a specific tasks, the number of times the program has timed this task, and the average time spent performing the task.

   ### Time

   To track the user's time stamps of when a task is started and when it is finished the Time library is essential for logging time stamps in order to capture the duration of the task being timed through this program.

   ### Sys

   The final library needed to run this program is the Sys library. The user will not specifically use the sys library tools when initally running the Python Program. The sys library essentially allows for clean error-related alerts and exit the program instead of staying stuck in the program under error-related circumstances. The sys.exit() function is activated when implementing Cmd+C to exit a program when the program prompts the user to either start or start the timer.

   ## Usage -

   ### Step One

   The first step to using the Task Time Tracker is executing the program by typing "python project.py" on the command line. This will initiate the program. The user will be immediately prompted to enter a name for the desired task. If you choose a task that already exists in the list of previously timed tasks, please be aware that you must use the exact wording previously used. For example, if the previously timed task is "wash dishes", the exact same verbiage is required to update the average time for that task. If the user instead enters "washing dishes" the program will treat that entry as a brand new task.

   ### Step Two

   Once the user has submitted the task he or she wants timed, the system will prompt the user to hit the "Enter" key on the keyboard to start the clock. The clock will not track any time data until the "Enter" key is hit. If any other key is entered, the system will reprompt the user to hit the correct key for the program to operate as intended.

   ### Step Three

   Once the "Enter" key is hit and the clock has started, the user is immediately prompted to hit the "Enter" key again to stop the clock. The user can then work towards completing the task, taking as much time as needed. The clock will continue to count seconds until the "Enter" key is hit for the second time. If the user hits any other keys or commands on the keyboard, the clock will continue to run and reprompt the user to hit the "Enter" key and nothing else.

   ### Step Four
   Once both the start time and end time for the task is captured, the program calculates the duration of how long it took to complete the task in total amount of seconds.

   If the task name does not currently exist in the list of timed tasks, it will be added into the csv file.

   If the task name already exists in the csv file, the amount of times the program has timed the task will be increased by 1. The total amount of seconds captured will be updated by the new timed session, and finally the average amount of time will be updated.

   ### Step Five

   The last step of this program will be providing the average amount of time it typically takes the user to complete a specific task in minutes.

   ## Contributing -

   The biggest current need for contirubtation is constructive critiscim on code effenciency and handling errors not yet accounted for in this program. Additionally, any graphic interface contributations will be accepted as well. Please reach out via Twitter by sending a DM to @alissamiche