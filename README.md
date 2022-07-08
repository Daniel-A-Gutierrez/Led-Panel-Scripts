Setup
========
<br>Download this repository as a zip and extract it onto your computer
<br>Login to the led panel with winscp. 
<br>Clear out any existing extraneous folders in the home/pi directory, which other children have made in their classes.
<br>Any which cannot be removed can be removed later. (do not remove the led-matrix directory )
<br>Create a directory here called "projects".
<br>From the repository, drop in examples and ledpanel. 
<br>Login to the led panel with ssh. Wifipw : 123456789, username : pi , pw :raspberry"
<br>Run the command "sudo mv ledpanel /usr/local/lib/python3.5/dist-packages"
<br>Any extraneous folders left by other students can be removed with "sudo rm -r folder_name". Be careful doing this.
<br>Run the sanity check to ensure the setup has been done correctly. It is located in examples. Run it like so:
<br>"sudo python3 SanityCheck.py"


Examples
========
Extra examples for fun/curriculum.

Run with `sudo python3 (filename)`


