<center> <h1>HBNB - The Console</h1> </center>

This repository contains the initial stage of a student project to build a clone of the AirBnB website. This stage implements a backend interface, or console, to manage program data. Console commands allow the user to create, update, and destroy objects, as well as manage file storage. Using a system of JSON serialization/deserialization, storage is persistent between sessions.

---

<center><h3>Repository Contents by Project Task</h3> </center>

| Tasks | Files | Description |
| ----- | ----- | ------ |
| 0: Authors/README File |
| 1: Pep8 | N/A | All code is pep8 compliant|
| 2: Unit Testing | [/tests]| All class-defining modules are unittested |
| 3. Make BaseModel | [/models/base_model.py] | Defines a parent class to be inherited by all model classes|
| 4. Update BaseModel | Add functionality to recreate an instance of a class from a dictionary representation|
| 5. Create FileStorage class | [/models/_ _init_ _.py]| Defines a class to manage persistent file storage system|
| 6. Console 0.0.1 | Add basic functionality to console program, allowing it to quit, handle empty lines and ^D |
| 7. Console 0.1 | | Update the console with methods allowing the user to create, destroy, show, and update stored data |
| 8. Create User class || Dynamically implements more classes |
| 10. Console 1.0 | | Update the console and file storage system to work dynamically with all  classes update file storage |
<br>
<br>
<center> <h2>General Use</h2> </center>

1. First clone this repository.

3. Once the repository is cloned locate the "console.py" file and run it as follows:
```
/AirBnB_clone$ ./console.py
```
4. When this command is run the following prompt should appear:
```
(hbnb)
```
5. This prompt designates you are in the "HBnB" console. There are a variety of commands available within the console program.

##### Commands
    * create - Creates an instance based on given class

    * destroy - Destroys an object based on class and UUID

    * show - Shows an object based on class and UUID

    * all - Shows all objects the program has access to, or all objects of a given class

    * update - Updates existing attributes an object based on class name and UUID

    * quit - Exits the program (EOF will as well)


##### Alternative Syntax
Users are able to issue a number of console command using an alternative syntax:

	Usage: <class_name>.<command>([<id>[name_arg value_arg]|[kwargs]])
Advanced syntax is implemented for the following commands: 

    * all - Shows all objects the program has access to, or all objects of a given class

	* count - Return number of object instances by class

    * show - Shows an object based on class and UUID

	* destroy - Destroys an object based on class and UUID

    * update - Updates existing attributes an object based on class name and UUID


