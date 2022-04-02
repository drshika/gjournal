Taught by Drshika Asher, Justin Hu, and Joanna Huang

------------------------------------------

# Getting Ready

### Local Machine Instructions

1. Download a **text editor** (VSCode: https://code.visualstudio.com/download) and make sure you have a version of **python** greater than 3.0 and https://pip.pypa.io/en/stable/installation/ installed. To check your python version, run the following command:
```bash
   $  python --version
```
- Tutorial for Windows: https://feaforall.com/how-to-install-python-3-on-windows-and-set-the-path/
- Tutorial for Mac: https://www.educative.io/edpresso/how-to-add-python-to-the-path-variable-in-mac
- Install Pip: https://pip.pypa.io/en/stable/installation/
2. Clone starter code
```bash
    $ git clone https://github.com/drshika/gjournal.git
```
3. Open folder in VSCode
```bash
    $ code .
```
or open VSCode, File >> Open Folder >> choose the gjournal directory

![open in vscode](_images/vscodeimport.png)
4. Install requirements
Run the following in your terminal
```bash
    $ pip install -r requirements.txt
```

### Repl.it Instructions
Just in case your local machine does not work for some reason.
1. Log onto your [https://replit.com/~](https://replit.com/~)
2. Create Repl 
![create repl](_images/createrepl.png)
![create repl pt 2](_images/createrepl2.png)
3. Install requirements
Run the following in your console
```bash
    $ pip install -r requirements.txt
```


### Extras:

2. Learn a bit of git on the commmand line. You can use any intro tutorial, but [this web browser one](https://learngitbranching.js.org/) looks good.

3. Learn some basics of how a command line works. [Here is a quick crash course](https://www.vikingcodeschool.com/web-development-basics/a-command-line-crash-course) with links to resources to learn even more. The command line is intimidating, but once you get used to it, you'll wonder how you lived without it. It's part of almost every programmer's toolbox.

# Workshop

Justin, Drshika, and Joanna were too busy with their algorithms class and procrastinated creating this workshop! Oh no! Now, we need **YOUR** help to fix some bugs, write some functions and create a wholesome gratitude journal for your command line. 

You will learn how to work with different Python Libraries, read test outputs and documentation, read existing code and integrate your work into the code base.

Prior Knowledge: Intermediate/Advanced Programming

Note: I've done this on MacOs Monterey 12.1 but you should be able to do this on any computer. Your progress shouldn't be drastically different, but you may need to adjust depending on how your OS does things. I used `python 3.9.9`.

# Background
## Files
In the directory, we have provided you with some starter files for the project. Here is a short explainer of what each of them are:

- sail directory
    - contains the api that has some helpers for this workshop
- sail_journal
    - contains journal entries
- .gitignore
    - tells git what files to ignore
- LICENSE
    - allows other people to modify and extend our code!
    - learn more about open source licenses! [https://opensource.org/licenses](https://opensource.org/licenses)
- functions.py
    - helper functions for our code
- journal.py
    - main file with all the functions that runs the journal cli
- requirements.txt 
    - libraries that our program requires to run

### Libraries
In the file called `requirements.txt`, we have provided the names of libraries needed to run the cli. This is a common convention in Python projects.

```js
questionary
datetime
pyyaml
pyfiglet
plumbum
ruamel.yaml
pytest
```

Running the command we did earlier installs these packages all at once (if you use `python3` to execute commands, then use `pip3`):

```bash
$ pip install -r requirements.txt
[install output]
```  

The `-r` flag tells `pip` to look at `requirements.txt` and install everything in it.

Let me explain how we're using each library.

* [questionary](https://github.com/tmbo/questionary) give us fancy interactive menu interfaces.
* [pyfiglet](https://github.com/pwaller/pyfiglet) provides ASCII art displays.
* [plumbum](https://plumbum.readthedocs.io/en/latest/) gives us a way of accepting input, displaying help information and calling existing system commands.
* [pyyaml](https://pyyaml.org/wiki/PyYAMLDocumentation) allows us to set a filepath and your name
* [datetime](https://pypi.org/project/DateTime/) gives us the date and time
* [ruaeml.yaml](https://pypi.org/project/ruamel.yaml/) extends capabilities of pyyaml and allows us to format strings properly
* [pytest](https://docs.pytest.org/en/6.2.x/) allows us to test our code and make sure everything is running

```bash
    $ pytest --tb=no
```

## What the code does

### Logical Level
Let's imagine this gratitude journal in real life. Here are some steps you may take:

1. Get a Journal
2. Open the Journal to the right page (for today)
3. Journal
4. Close the Journal
5. View past Journals

We tried imitating these steps in our code, but some of them are incomplete/buggy. Can you help us fix them? 

Yes you can! You're a UIUC CS student and you're super smart and can solve these problems hehe

### Implementation
Now, here is the translation of those basic journal functionalities into code.

**Main Journal functions:**
1. `pick_journal`
    - Help the user get a journal with their name and store it in their location
2. `write_journal`
    - Open the right entry and allow the user to write what they are grateful for
3. `add_content`
    - Give the user a prompt to journal on and collect their thoughts
4. `read_entries`
    - Let the user "flip" through their digital journal entries