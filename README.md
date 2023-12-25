# ShaastraCTF2024
CTF Questions for Shaastra 2024

## Q1
Name: Simply Encoded  
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
Logic: A recursive algorithm is written which does not function like normal recursive functions. Long story short, an equivalent iterative loop must be figured out and used to generate fibbmod(250) <br />
Difficulty : 9 <br />
Clue: Every recursive function has an equivalent iterative form <br />


## Q5
Name: Maze Runner
Logic: You are thrown inside a labyrinth of recursively linked directories , users need to navigate through it to find the text file with the flag. Each file will contain folders names a , c , f , h , r, s, t , and right answer will come from going to the file by following the order s-> h -> a -> a -> s -> t -> r -> a . We will let them know that shortest path is 7 directories 
Difficulty: 5
Clue: We will tell them to use rm -r on some files at the highest level which will simplify the challenge


## Q6
Name: Corporate Trails <br />
Logic: We provide an image and tell the person to find the flag hinting at the author's workplace <br />
Difficulty : 5 <br />
Clue: Where does this person work? <br />


## Q7
Name : Acropolis <br />
Logic: We provide an image of the Acropolis and say - "Shattering the location of this image gives you the answer, Quickly. Submit it like this - 6f79e83ebf4321cad0f70cf9664e4540dbb89e33bce5abc70574589a". We need to scramble the letters in the word "Athens" and submit it in SHA224 hashed format<br />
Difficulty : 6 <br />
Clue: Unscramble and Hash <br />


## Q8
Name: Decoding Digits <br />
Logic: We provide the executable of the file and ask them to crack the 10 digit code and submit it as ShaastraCTF{...}. It does not give out a correct answer output even for the correct answer, we must find the answer by observing which input takes the longest to run. <br />
Difficulty : 7 <br />
Clue: Is Runtime proportional to the Correct solution? <br />


## Q9
Name: SSL Buster <br />
Logic: We provide a .pcapng file of a MySQL Server-Client interaction, and we ask them to print out the base64 encoded raw dump of the TLS-decrypted SSL certificate, in the format ShaastraCTF{...}. SSL key is in the file comments. <br />
Difficulty : 9 <br />
Clue: Use the SSL key to decrypt packets through the TSL protocol. <br />

