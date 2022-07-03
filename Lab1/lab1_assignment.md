## Lab 1: 
#### Basic "Knowledge Toolbox" to get started in the Cloud

In this Lab you will be asked to put in practice the basic knowledge required for Labs of this course.

#  Pre-lab homework
Have a look at provided tutorials to come up to speed with the basics for this course.

* Tutorial 0: [Run Linux OS in a Virtual Machine](https://github.com/jorditorresBCN/Quick-Start/blob/master/LinuxOS-VirtualMachine.md) (Only for Windoze users)

* Tutorial 1: [Git Quick Start](https://github.com/jorditorresBCN/Quick-Start/blob/master/Git-Github-Quick-Start.md)

* Tutorial 2: [Markdown syntax](https://github.com/jorditorresBCN/Quick-Start/blob/master/Quick-Start-Markdown.md)

* Tutorial 3: [Python Quick Start](https://github.com/jorditorresBCN/Quick-Start/blob/master/Python-Quick-Start.md) 

* Tutorial 4: [Getting Started in the Cloud with AWS](https://github.com/jorditorresBCN/Quick-Start/blob/master/Quick-Start-AWS.md)


### Lab Tasks

#### Task 1:
Install Python on your local host.

#### Task 2:
Using Python create a program that exploits the ‘random’ library. 
Creativity will be valued positively. The minimum example accepted will be a code that generates a random number between 1 and 20, then let the player guess the number introduced. At each guess, the code displays if the number is to low or too high. The game ends either when the number is guessed correctly or when the USER decides to end it. The suggested program name is `guess_nbr.py`.

#### Task 3:
Create a private repo ‘CLC_cloud-computing_2017’ in your GitHub account. Use your student email for creating your github account in order to benefit from students privilege on the GitHub platform.

#### Task 4:
Update your remote Git repo from your local host repo.
```
echo "# CLC - Cloud-Computing - 2017" >> Readme.md
git init
git add Readme.md
git add guess_nbr.py
git commit -m "Lab 1 – task 1"
git remote add origin https://github.com/<USER>/CLC_cloud-computing_2017.git
git push -u origin master
```

#### Task 5:
Update the ‘Readme.md’ file including all the information of your group (members’ names and emails).

#### Task 6:
Invite GitHub user ‘JordiTorresBCN’ to your remote private repository as a collaborator using ‘Settings’ (for evaluation purpose).

#### Task 7:
Create an AWS account using your student ID.<BR>
Create an EC2 instance on your AWS account.<BR>
Pull down the contents of your remote Git repo making an exact clone, issuing `git clone`.

#### Task 8:
Execute the program `guess_nbr.py` in your AWS EC2 instance.<BR>
Take an screenshot of the xterm as a proof of a successful execution on the cloud host.<BR>
Include this screenshot in your local host’s repo under the name `aws_terminal.png`.

#### Task 9:
Update your remote Git repo with the updated `Readme.md`and the new file `aws_terminal.png` using `git add`, `commit` and `push`.
