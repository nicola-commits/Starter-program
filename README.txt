First of all, you have to have python >3.7, tkinter and pygame.
Then, execut the file. You'll have a little screen with a couple options: 
calculator opens a simple calculator.
password ganerator opens a password generator. It works by using the random module to create random password sequences. You have a 'username' and a 'webpage' entries, they're not important, put whatever you like. They'll be used later. When you press 'calculate' it'll create a password.txt file in which you'll have written the username and webpage you put in, other than the password. This file will be in the same repository as the main one.
The web browser opens a window, put in whatever you like and it'll open a google search with whatever you've put in in your default browser.
The stress test button.. does not work for now, but I'm working on it.
The game button opens a little game I created, more for knowing how pygame works than anything else. You move with wasd, if you go near the x you'll be teleported to the start coordinates. It's by default set for 75fps, if you want you can change it by modifying the 'fps' variable. Gravity is a thing and it works as it does IRL, with an acceleration rather than a costant velocity.
