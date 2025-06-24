# 0x02. Shell, I/O Redirections and filters

## Resources:
1. [Shell, I/O Redirection](https://linuxcommand.org/lc3_lts0070.php)
2. [Special Characters](https://mywiki.wooledge.org/BashGuide/SpecialCharacters)

man or help:

echo
cat
head
tail
find
wc
sort
uniq
grep
tr
rev
cut
passwd (5) (i.e. man 5 passwd)

## Learning Objectives
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

Shell, I/O Redirection
What do the commands head, tail, find, wc, sort, uniq, grep, tr do
How to redirect standard output to a file
How to get standard input from a file instead of the keyboard
How to send the output from one program to the input of another program
How to combine commands and filters with redirections
Special Characters
What are special characters
Understand what do the white spaces, single quotes, double quotes, backslash, comment, pipe, command separator, tilde and how and when to use them
Other Man Pages
How to display a line of text
How to concatenate files and print on the standard output
How to reverse a string
How to remove sections from each line of files
What is the /etc/passwd file and what is its format
What is the /etc/shadow file and what is its format
Copyright - Plagiarism
You are tasked to come up with solutions for the tasks below yourself to meet with the above learning objectives.
You will not be able to meet the objectives of this or any following project by copying and pasting someone else’s work.
You are not allowed to publish any content of this project.
Any form of plagiarism is strictly forbidden and will result in removal from the program.
Requirements
General
Allowed editors: vi, vim, emacs
All your scripts will be tested on Ubuntu 20.04 LTS
All your scripts should be exactly two lines long ($ wc -l file should print 2)
All your files should end with a new line (why?)
The first line of all your files should be exactly #!/bin/bash
A README.md file, at the root of the folder of the project, describing what each script is doing
You are not allowed to use backticks, &&, || or ;
All your files must be executable
You are not allowed to use sed or awk
More Info
Read your /etc/passwd and /etc/shadow files.

Note: You do not have to learn about fmt, pr, du, gzip, tar, lpr, sed and awk yet.

0. 0-hello_world
Write a script that prints “Hello, World”, followed by a new line to the standard output.

1. 1-confused_smiley
Write a script that displays a confused smiley "(Ôo)'.

2. 2-hellofile
Display the content of the /etc/passwd file.

3. 3-twofiles
Display the content of /etc/passwd and /etc/hosts

4. 4-lastlines
Display the last 10 lines of /etc/passwd

5. 5-firstlines
Display the first 10 lines of /etc/passwd

6. 6-third_line
Write a script that displays the third line of the file iacta.

The file iacta will be in the working directory

You’re not allowed to use sed

7. 7-file
Write a shell script that creates a file named exactly \*\\'"Best School"\'\\*$\?\*\*\*\*\*:) containing the text Best School ending by a new line.

8. 8-cwd_state
Write a script that writes into the file ls_cwd_content the result of the command ls -la. If the file ls_cwd_content already exists, it should be overwritten. If the file ls_cwd_content does not exist, create it.

9. 9-duplicate_last_line
Write a script that duplicates the last line of the file iacta

The file iacta will be in the working directory

10. 10-no_more_js
Write a script that deletes all the regular files (not the directories) with a .js extension that are present in the current directory and all its subfolders.

11. 11-directories
Write a script that counts the number of directories and sub-directories in the current directory.

The current and parent directories should not be taken into account
Hidden directories should be counted

12-newest_files
Create a script that displays the 10 newest files in the current directory.

Requirements:

One file per line
Sorted from the newest to the oldest

13-unique
Create a script that takes a list of words as input and prints only words that appear exactly once.

Input format: One line, one word
Output format: One line, one word
Words should be sorted

14-findthatword
Display lines containing the pattern “root” from the file /etc/passwd

15-countthatword
Display the number of lines that contain the pattern “bin” in the file /etc/passwd

16-whatsnext
Display lines containing the pattern “root” and 3 lines after them in the file /etc/passwd.

17-hidethisword
Display all the lines in the file /etc/passwd that do not contain the pattern “bin”.

18-letteronly
Display all lines of the file /etc/ssh/sshd_config starting with a letter.

include capital letters as well

19-AZ
Replace all characters A and c from input to Z and e respectively.

20-hiago
Create a script that removes all letters c and C from input.

21-reverse
Write a script that reverse its input.

22-users_and_homes
Write a script that displays all users and their home directories, sorted by users.

Based on the the /etc/passwd file

100-empty_casks
Write a command that finds all empty files and directories in the current directory and all sub-directories.

Only the names of the files and directories should be displayed (not the entire path)
Hidden files should be listed
One file name per line
The listing should end with a new line
You are not allowed to use basename, grep, egrep, fgrep or rgrep

101-gifs
Write a script that lists all the files with a .gif extension in the current directory and all its sub-directories.

Hidden files should be listed
Only regular files (not directories) should be listed
The names of the files should be displayed without their extensions
The files should be sorted by byte values, but case-insensitive (file aaa should be listed before file bbb, file .b should be listed before file a, and file Rona should be listed after file jay)
One file name per line
The listing should end with a new line
You are not allowed to use basename, grep, egrep, fgrep or rgrep

102-acrostic
An acrostic is a poem (or other form of writing) in which the first letter (or syllable, or word) of each line (or paragraph, or other recurring feature in the text) spells out a word, message or the alphabet. The word comes from the French acrostiche from post-classical Latin acrostichis). As a form of constrained writing, an acrostic can be used as a mnemonic device to aid memory retrieval. Read more.

Create a script that decodes acrostics that use the first letter of each line.

The ‘decoded’ message has to end with a new line
You are not allowed to use grep, egrep, fgrep or rgrep

103-the_biggest_fan
Write a script that parses web servers logs in TSV format as input and displays the 11 hosts or IP addresses which did the most requests.

Order by number of requests, most active host or IP at the top
You are not allowed to use grep, egrep, fgrep or rgrep
Format:

host    When possible, the hostname making the request. Uses the IP address if the hostname was unavailable.
logname Unused, always -
time    In seconds, since 1970
method  HTTP method: GET, HEAD, or POST
url Requested path
response    HTTP response code
bytes   Number of bytes in the reply
Here is an example with one day of logs of the NASA website (1995).

julien@ubuntu:/tmp/0x02$ wget https://s3.amazonaws.com/alx-intranet.hbtn.io/public/nasa_19950801.tsv
--2022-03-08 11:08:26--  https://s3.amazonaws.com/alx-intranet.hbtn.io/public/nasa_19950801.tsv
Resolving s3.amazonaws.com (s3.amazonaws.com)... 52.217.171.144
Connecting to s3.amazonaws.com (s3.amazonaws.com)|52.217.171.144|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 782913 (765K) [binary/octet-stream]
Saving to: ‘nasa_19950801.tsv’

nasa_19950801.tsv   100%[===================>] 764.56K  --.-KB/s    in 0.008s

2022-03-08 11:08:26 (98.4 MB/s) - ‘nasa_19950801.tsv’ saved [782913/782913]

julien@ubuntu:/tmp/0x02$ head nasa_19950801.tsv
host    logname time    method  url     response        bytes
in24.inetnebr.com       -       807249601       GET     /shuttle/missions/sts-68/news/sts-68-mcc-05.txt 200     1839
uplherc.upl.com -       807249607       GET     /       304     0
uplherc.upl.com -       807249608       GET     /images/ksclogo-medium.gif      304     0
uplherc.upl.com -       807249608       GET     /images/MOSAIC-logosmall.gif    304     0
uplherc.upl.com -       807249608       GET     /images/USA-logosmall.gif       304     0
ix-esc-ca2-07.ix.netcom.com     -       807249609       GET     /images/launch-logo.gif 200     1713
uplherc.upl.com -       807249610       GET     /images/WORLD-logosmall.gif     304     0
slppp6.intermind.net    -       807249610       GET     /history/skylab/skylab.html     200     1687
piweba4y.prodigy.com    -       807249610       GET     /images/launchmedium.gif        200     11853
julien@ubuntu:/tmp/0x02$ ./103-the_biggest_fan < nasa_19950801.tsv 
www-relay.pa-x.dec.com
piweba3y.prodigy.com
www.thyssen.com
130.110.74.81
ix-min1-02.ix.netcom.com
uplherc.upl.com
reggae.iinet.net.au
seigate.sumiden.co.jp
ircgate1.rcc-irc.si
s150.phxslip4.indirect.com
torben.dou.dk
julien@ubuntu:/tmp/0x02$ 