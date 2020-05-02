# Matching Numbers GUI


This simple GUI is a learning game that after pressing start it will call out a number and the user has to select that number. This GUI program was written using **Python 3.7** on a **Windows 10** OS.

-----------------------
Install before running
-----------------------

Python libraries needed

    pip install pygame
    pip install pyglet
    pip install random
    pip install tkinter
    pip install gtts

Run Programm
------------

After clonning this project, it can be started with the following commands:
```
$py -m matchingGui
```
A pop up window will appear. Press start to start and click on the number that is spoken until a pop up window pops up. **Make sure the speaker is on and the volume is up.**

Changes To Original Project Idea
--------------------------------

There were 2 changes made from the original project idea. Originally I wanted to be able to get a kids youtube video to pop up and play after a person completes the challenge as a reward. However, I found it very difficult to get a youtube video to get it connected and playing and after some search I couldnt really find any helpful libraries so I opted to just change it to a pop up messagebox that completes the challenge. The second change I made was that instead of listening to a person speak when a number pops up, my GUI speaks and the user has to select the number spoken. The main reason I changed that was because autistic kids have a hard time pronouncing words so the speaker will have a lot of trouble understanding and matching with the right number.
