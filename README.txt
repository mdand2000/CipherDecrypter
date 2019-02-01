This is a Python 2.7.15 program and needs that to run.

Have base.py, cipherCracker.py, ngram_score.py, ngrams.txt, substitution.py, and the file you want decrypted
in the same directory. I called mine nsacoded.txt as I used NSA's 2014 tweet for this example.

To run type "cipherCracker.py" at the command prompt in the directory where these files are located.

The prgram will ask for the file name (please include the file extension (I am working on exception handling)).

Once you enter the file name, the program starts to print on screen the decypted text from the file. When complete/use is happy with the output, the user types ctrl+c to exit.  The program writes the decrypted text to a file in that directory called
decrypted.txt.

Since I am still learning, this is a very simple program and I plan to work on it as a project for myself as I learning
Python's methods moving forward.  Any input from you would be greatly appreciated!

I want to add some error handling, checking for the file name before writing, not having to enter the file extension when entering the file name, and to incorporate argparse to make it more interactive and user friendly.

Additionally, it would be nice to be able to parse PATH and run this from anywhere and except paths to find/decrypt files anywhere.
