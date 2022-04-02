---
---
<style>
    a[href="#spoiler"] {
    text-decoration: none !important;
    cursor: default;
    margin-bottom: 10px;
    padding: 10px;
    background-color: #FFF8DC;
    border-left: 2px solid #ffeb8e;
    display: inline-block;
  }
  a[href="#spoiler"]::after {
    content: attr(title);
    color: #FFF8DC;
    padding: 0 0.5em;
  }
  a[href="#spoiler"]:hover::after,
  a[href="#spoiler"]:active::after {
    cursor: auto;
    color: black;
    transition: color .5s ease-in-out;
  }
</style>

Taught by Drshika Asher, Justin Hu, and Joanna Huang

------------------------------------------

# Getting Ready

### Local Machine Instructions

1. Download a **text editor** (VSCode: https://code.visualstudio.com/download) and make sure you have a version of **python** greater than 3.0 and https://pip.pypa.io/en/stable/installation/ installed. To check your Python version, run the following command:
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
3. Open the folder in VSCode
```bash
    $ code .
```
or open VSCode, File >> Open Folder >> choose the gjournal directory

![open in vscode](https://github.com/drshika/gjournal/blob/gh-pages/assets/images/vscodeimport.png)
4. Install requirements
Run the following in your terminal
```bash
    $ pip install -r requirements.txt
```
5. Install pytest globally so that you can test your code:

```bash
    $ pip install -u pytest
```

### Repl.it Instructions
Just in case your local machine does not work for some reason.
1. Log onto your [https://replit.com/~](https://replit.com/~)
2. Create Repl 
![create repl](https://github.com/drshika/gjournal/blob/gh-pages/assets/images/createrepl.png)
![create repl pt 2](https://github.com/drshika/gjournal/blob/gh-pages/assets/images/createrepl2.png)
3. Install requirements
Run the following in your console
```bash
    $ pip install -r requirements.txt
```
4. Install pytest globally so that you can test your code:

```bash
    $ pip install -u pytest
```

### Extras:

2. Learn a bit of git on the command line. You can use any intro tutorial, but [this web browser one](https://learngitbranching.js.org/) looks good.

3. Learn some basics of how a command line works. [Here is a quick crash course](https://www.vikingcodeschool.com/web-development-basics/a-command-line-crash-course) with links to resources to learn even more. The command line is intimidating, but you'll wonder how you lived without it once you get used to it. It's part of almost every programmer's toolbox.

# Workshop

Justin, Drshika, and Joanna were too busy with their algorithms class and procrastinated creating this workshop! Oh no! We need **YOUR** help to fix some bugs, write some functions and create a wholesome gratitude journal for your command line. 

You will learn to work with different Python Libraries, read test outputs and documentation, read existing code and integrate your work into the codebase.

Prior Knowledge: Intermediate/Advanced Programming

*Note:* I've done this on MacOs Monterey 12.1, but you should be able to do this on any computer. Your progress shouldn't be drastically different, but you may need to adjust depending on your OS. I used `python 3.9.9`.

# Background
## Files
We have provided you with some starter files for the project in the directory. Here is a short explainer of what each of them is:

- sail directory
    - contains the API that has some helpers for this workshop
- sail_journal
    - contains journal entries
- .gitignore
    - tells git what files to ignore
- LICENSE
    - allows other people to modify and extend our code!
    - learn more about oopen-source licenses! [https://opensource.org/licenses](https://opensource.org/licenses)
- functions.py
    - helper functions for our code
- journal.py
    - main file with all the functions that run the journal cli
- requirements.txt 
    - libraries that our program requires to run

### Libraries
In the file called `requirements.txt`, we have provided the names of libraries needed to run the cli. Creating a requirements file is a standard convention in Python projects.

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
* [pyfiglet](https://github.com/pwaller/pyfiglet) provides ASCII art displays. See fonts [here](http://www.figlet.org/examples.html)
* [plumbum](https://plumbum.readthedocs.io/en/latest/) gives us a way of accepting input, displaying help information, and calling existing system commands.
* [pyyaml](https://pyyaml.org/wiki/PyYAMLDocumentation) allows us to set a filepath and your name
* [datetime](https://pypi.org/project/DateTime/) gives us the date and time
* [ruaeml.yaml](https://pypi.org/project/ruamel.yaml/) extends the capabilities of pyyaml and allows us to format strings properly
* [pytest](https://docs.pytest.org/en/6.2.x/) allows us to test our code and make sure everything is running

## What the code does

### Logical Level
Let's imagine this gratitude journal in real life. Here are some steps you may take:

1. Get a Journal
2. Open the Journal to the right page (for today)
3. Journal
4. Close the Journal
5. View past Journals

We tried imitating these steps in our code, but some of them are incomplete/buggy. Can you help us fix them? 

Yes, you can! You're a U of I CS student, and you're super bright and can solve these problems hehe

### Implementation
Now, here is the translation of those basic journal functionalities into code.

**Main Journal functions:**
1. `pick_journal`
    - Help the user get a journal with their name and store it in their location
2. `write_journal`
    - Open the right entry and allow the user to write what they are grateful for
3. `add_content`
    - Give the user a prompt to journal and collect their thoughts
4. `read_entries`
    - Let the user "flip" through their digital journal entries

## Fixing the code
Your task, if you choose to accept it, will be to fix some bugs, implement some functions and add some aesthetic improvements and your creative touches :sparkles:

### 1. Squash the Bugs!

**Test Case #1: Making Folders**

Try the following:

1. Pick a journal with the name `"Student A"` and the path `"student"`.
2. Pick a journal with the name `"Student B"` and the path `"student"`.

We get a `FileExistsErrors`! Can you guess what is causing the error? 

In professional programming, we like to handle errors nicely and not rely on the compiler to catch our mistakes. So how do we make the error message more helpful?

[Hint 1](#spoiler How do we handle errors in Python?)

[Hint 2](#spoiler What kind of error is this?)

[Hint 3](#spoiler If you have no clue how to do something, google! StackOverflow is a really valuable resource. Here's a link to get you started:   
[https://stackoverflow.com/questions/4592162/python-exception-handling](https://stackoverflow.com/questions/4592162/python-exception-handling))

**Test Case #2: Writing Entries**

Try the following:
1. Pick a journal with any name and path you'd like!
2. Write a journal entry.

What??? I'm getting a `io.UnsupportedOperation: not writable` error?

[Hint 1](#spoiler What flags can you specify in the open function?)

[Hint 2](#spoiler In our example code, we specified the flag `r`. What does this mean?)

[Hint 3](#spoiler What flag could we use to represent write?)

[Hint 4](#spoiler Time to go back to google. Geeks4Geeks sometimes has good information:   
[https://www.geeksforgeeks.org/python-open-function/](https://www.geeksforgeeks.org/python-open-function/))

*To test your code, run:*
```
$ pytest --tb=no
```
### 2. Write the Functions!

**Impl #1: Reading entries**

Let's allow our users to read what they have written in the past. We've been able to write to a file or open a file, but we don't yet have a way to read the contents of a file. Let's fix that. 

*Hint 1: Your function should return the contents of the file.*

*Hint 2: How do you open a file?*

*Hint 3: What flag should you use for this?*

**Impl #2: Writing in journal**

Copy your implementation of `write_file()` to `add_to_file()`. What modifications do you need to make so that the function behaves properly?

*Hint 1: Your function should not overwrite the old contents in the file*

*Hint 2: How do you open a file?*

*Hint 3: What flag should you use for this?*

**Impl #3: Fancy Print**

Now, let's jazz up our CLI by adding a fancy greeting for our users! We'll use `Figlet` from the `pyfiglet` library to select a font and `plumbum` to choose a color. Currently, our app prints out plain text and then asks the user for their choice of what to do. 

*Hint 1: When you don't know how to use a strange library, googling the documentation is your best friend*

*Hint 2: See the [Libraries](#libraries) section for the links to the documentation for each library we use here*

*To test your code, run:*
```
$ pytest --tb=no
```
### 3. Extra Credit!

Using your newfound knowledge, let's implement the "I'm Feeling Lucky" option!

Pick a random journal entry, and show a snippet of it to the user!

We're not going to provide hints for this one. So instead, try to google around yourself and see what you can create. Good luck, have fun!

## Acknowledgements

Thank you so much for joining us for this workshop. Thanks to Harsh Deep & Monica Para (cofounder of 125 Summer of Side Projects: [https://125summer.tech/](https://125summer.tech/)) and [Candace Williams](https://medium.com/thebit/intro-to-file-i-o-and-terminal-usage-how-to-create-a-journal-using-python-7bf1ccf1549a) for a lot of language, explanations, and packages used to create this workshop. ILL!