Setup
========
Download this repository as a zip and extract it onto your computer
Login to the led panel with winscp
Clear out any existing extraneous folders in the home/pi directory, which other children have made in their classes.
    do not remove the led-matrix directory
Any which cannot be removed can be removed later.
Create a directory here called "projects".
From the repository, drop in examples and ledpanel. 
Run the command "sudo mv ledpanel /usr/local/lib/python3.5/dist-packages"
Any extraneous folders left by other students can be removed with "sudo rm -r folder_name". Be careful doing this.
Run the sanity check to ensure the setup has been done correctly. It is located in examples. Run it like so:
"sudo python3 SanityCheck.py"


Examples
========
Extra examples for fun/curriculum.

Run with `sudo python3 (filename)`


