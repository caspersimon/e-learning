# Resetting FCP trial period
You can easily reset the trial period:
1. Open the Terminal application
2. Copy and paste this command: 
   `mv -v ~/Library/Application\ Support/.ffuserdata ~/.Trash`
3. Now open FCP again and see that the trial period is 90 days. If this is not the case, you can try the instructions below.

*Manual reset*:
1. Open Finder
2. On the menu bar, click *Go > Library*
3. Find and open the folder named 'Application Support'
4. Press the key combination **⌘ + ⇧ + .**  (*Command + Shift + dot* ). This will reveal hidden files.
5. Find the file named _.ffuserdata_ and delete it.

*Why does this work?*

FCP stores the date that you first opened the trial period in the file named _.ffuserdata_. If you delete that file, FCP seems to assume you have never opened FCP and thus grants you 90 days acces. Running the command or manually deleting the file accomplishes the same thing :)
