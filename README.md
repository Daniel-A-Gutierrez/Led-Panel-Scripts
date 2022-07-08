Setup
========
<p>Download this repository as a zip and extract it onto your computer</p>
<p>Login to the led panel with winscp. </p>
<p>Clear out any existing extraneous folders in the home/pi directory, which other children have made in their classes.</p>
<p>Any which cannot be removed can be removed later. (do not remove the led-matrix directory )</p>
<p>Create a directory here called "projects".</p>
<p>From the repository, drop in examples and ledpanel. </p>
<p>Login to the led panel with ssh. Wifipw : 123456789, username : pi , pw :raspberry"
<p>Run the command "sudo mv ledpanel /usr/local/lib/python3.5/dist-packages"</p>
<p>Any extraneous folders left by other students can be removed with "sudo rm -r folder_name". Be careful doing this.</p>
<p>Run the sanity check to ensure the setup has been done correctly. It is located in examples. Run it like so:</p>
<p>"sudo python3 SanityCheck.py"</p>


Examples
========
Extra examples for fun/curriculum.

Run with `sudo python3 (filename)`


