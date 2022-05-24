# Django_HW3


### Task#1: Virtual Environment

You learned how to create a new Django project using PyCharm IDE which provides you with a ready virtual environment, however, VS Code doesn't provide that, so you have to search for:

- What is the main purpose behind using the virtual environment?
#The answer:

#Python has various modules and packages for different applications. During our project, it may require a third-party library, which we install. Another project also uses the same directory for retrieval and storage but doesn't require any other third-party packages. So, the virtual environment can come into play and make a separate isolated environment for both projects, and each project can store and retrieve packages from their specific environment.


- How to create a virtual environment?

#The answer:

*pip install virtualenv --> To install the virtual environment.

*virtualenv --version --> To test and check the version of installation.

*virtualenv <name of directory> --> To create a virtualenv
  
*virtualenv -p /usr/bin/python2.7 < name of directory> --> To create a more specific virtualenv
  
*source <name of directory>/bin/activate --> To activate the virtualenv





#Task#2: Apply CRUD on ToDoList Project
