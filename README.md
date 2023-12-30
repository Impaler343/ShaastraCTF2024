# ShaastraCTF2024
CTF Questions for Shaastra 2024

## Q1
Name: Simply Encoded  <br />
Logic: convolutional encoding, of order 1 . I.e we shift the string by 1 unit and then sum it up with the original string to generate an encoding with 1 more letter than the original. <br />
Difficulty : 6 <br />
Clue: Have you heard of convolution? <br />


## Q2
Name: Base Jumping <br />
Logic: A random noisy image, wherein the base 36 encodings will contain the password <br />
Difficulty : 6 <br />
Clue: You have heard of bases 2, 8,10, and 16... how far do you think we jumped? <br />


## Q3
Name: Deep Dive Discovery <br />
Logic: A .jpg file will have a .zip file when extracted will have another .zip file, and this will go on 1000 times, and the last folder will have the flag.txt file <br />
Difficulty: 8 <br />
Clue: Images have X and Y axes. Does this file have a Z-axis too? <br />


## Q4
Name : Name(A Recursion Reference) <br />
Logic: A recursive algorithm that does not function like normal recursive functions is written. Long story short, an equivalent iterative loop must be figured out and used to generate fibbmod(250) <br />
Difficulty : 8 <br />
Clue: Every recursive function has an equivalent iterative form <br />


## Q5
Name: The Flip Side of Binary <br />
Logic: The flag is converted to ASCII numbers in binary form. This binary form is 1's complemented and converted back to numbers and placed in a TXT file. This is the same as the 127-ASCII value <br />
Difficulty: 2  <br />
Clue: No clue <br />


## Q6
Name: Corporate Trails <br />
Logic: We provide an image and tell the person to find the flag hinting at the author's workplace <br />
Difficulty : 6 <br />
Clue: Where does this person work? <br />


## Q7
Name : Acropolis <br />
Logic: We provide an image of the Acropolis and say - "Shattering the location of this image gives you the answer, Quickly. Submit it like this - 6f79e83ebf4321cad0f70cf9664e4540dbb89e33bce5abc70574589a". We need to scramble the letters in the word "Athens" and submit it in SHA224 hashed format<br />
Difficulty : 5 <br />
Clue: Unscramble and Hash <br />


## Q8
Name: Decoding Digits <br />
Logic: We provide the file executable and ask them to crack the 6-digit code and submit it as ShaastraCTF{...}. It does not give out a correct answer output even for the correct answer, we must find the answer by observing which input takes the longest to run. <br />
Difficulty : 6 <br />
Clue: Is Runtime proportional to the Correct solution? <br />


## Q9
Name: SSL Buster <br />
Logic: We provide a .pcapng file of a MySQL Server-Client interaction, and we ask them to print out the base64 encoded raw dump of the TLS-decrypted SSL certificate, in the format ShaastraCTF{...}. The SSL key is in the file comments. <br />
Difficulty : 10 <br />
Clue: Use the SSL key to decrypt packets through the TSL protocol. <br />


## Q10
Name: Gottfried and Bob Bemer <br />
Logic: Gottfried discovered binary. In the question, the repeated use of two instead of to and too also suggests usage of binary format. Replace uppercase letters by 1, lowercase letters by 0. Split at every 8th letter. Convert every 8 bits to decimal and replace these from ASCII values to characters. The flag is obtained from "iAmTWobOreDOffINdiNGfLaGsIwANTTWodOSoMEThINgMoreinTEresTinGWaItDiDyOUSEEtHatTwoNoyOUdIdNoTiJUSTFouNDtHEFlAGnOwiamgOIngTWoThENEXTqUestIOnyOucANalsoGOiFyouWishTWO"
 <br />
Difficulty : 6 <br />
Clue: There are Two Types of leTTers in This senTence. <br />

## Q11
Q11: 
Name: Going low <br />
There is an assembly file that participants must download. Inside there is a line to give a particular number as input. And there is another target line, i.e. if the code reaches the target line, the input number given is the solution. Op1 calculates (a+b)%256, where a is n^n and b is n!; Without any prime factors of 2. Op2 is a complex way to check if the result of op1 is 1. Can be solved mathematically.
The ideal solution is to modify the code to cycle through all possible inputs and find the answer on its own. <br />
Difficulty : 8 <br />
Clue: Who knows what op1 does<br />

## Q12
Name: Cold & Hot
Logic: Interactive a.exe is given. Players have to guess the number to get the password. The program returns hot and cold opposite to the normal conventions, i.e cold means you are close and hot means you are far from the right answer.<br />
Difficulty : 4 <br />
Clue: The convention has been flipped, just like the name! <br />

##Q13
Name: RSA<br />
While sleuthing around your network , you see that there is a transmission with RSA encryption. Knowing that its not possible to hack the RSA codes due to the extensive amount of computing power that you would require , something catches your eye , the public key , is only 64 bits long ! You quickly collect the encrypted message and get to work..... What is the decoded message:<br />

Difficulty : 6<br />
Clue: Not needed<br />


Difficulty chart:
1: 0 <br />
2: 1 <br />
3: 0 <br />
4: 1 <br />
5: 1 <br />
6: 5 <br />
7: 0 <br />
8: 3 <br />
9: 0 <br />
10: 1 <br />
