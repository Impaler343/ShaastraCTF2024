## Q1 - Laplace, Fourier and CNN
Convolutional encoding of order 1 needs to be done to decrypt the string. I.e we need to shift the string by 1 unit and then sum it up with the original string to generate an encoding with 1 more letter than the original. 
<br />
ShaastraCTF{cRyPtOgRaPhYisAmAzInG}
<br />

## Q2 - Everest Base Camp
The image consists of the flag code written such that its representation in base 36 is the solution.
<br />
ShaastraCTF{C0m3_W3st1n}
<br />

## Q3 - Binary Dumpland
This question involves finding the hidden .zip file using binwalk, and then unzip this file 1000 times using a bash script to discover the .txt file that has the flag.
<br />
ShaastraCTF{Th3_4n5w3r_15_4n_1nt3g3r}
<br />

## Q4 - Name(Recursion, get it?)
We need to find the iterative solution to this recursive code which is a little complicated. After that, you will be able to find the value of fibbmod(250)
<br />
ShaastraCTF{4611686018427387904}
<br />

## Q5 - The Flip Side of Binary
We need to convert all the numbers to binary, flip all the bits, convert back to decimal and finally back to ASCII, to give the flag.
<br />
ShaastraCTF{Bit_0f_0bfusc4t10n_4nd_0bstruc710n}
<br />

## Q6 - Corporate Trails
We need to Google Search the image to find the author of the article whose page has the image, after which you need to go to the FaceBook page of the current Workplace of the author, where the flag can be found in one of the comments.
<br />
ShaastraCTF{W3lc0m3_t0_7h3_w0rld_0f_CTFs}
<br />

## Q7 - Acropolis
We need to scramble the letters of the word Athens to form hasten, we then need to hash it using sha-224 and submit the flag.
<br />
ShaastraCTF{dc021713e546210aa2f97ffe025fbf9c2ef5812c97735314dba280f8}
<br />

## Q8 - Decoding Digits
We need to observe that each correct letter of the 6-digit letter password makes the program run slower, hence they will try all the possibilities to find the one that takes the most time to run.
<br />
ShaastraCTF{835789}
<br />

## Q9 - SSL Buster
Go to the file comments to retrieve the SSL Key.
Add the SSL key to a text file on the system.
Use this file in the Wireshark SSL preferences, to decrypt TSL traffic.
Go to the packet which contains the SSL handshake.
Right-click on the packet select "Decode As" --> "base64" and view it as "raw".
<br />
ShaastraCTF{f9ae830816482b79a8}
<br />

## Q10 - Gottfried and Bob Bemer
Replace uppercase letters by 1, lowercase letters by 0. Split at every 7th letter. Convert every 7 bits to decimal and replace these from ASCII values to characters
<br />
ShaastraCTF{Y35_7h15_I5_7h3_FL4G}
<br />

## Q11 - Going Low
Smart solution:- You will see that wrong solutions end up inside an infinite loop of op2. Modify the code to redirect itself to the main function instead of entering the infinite loop and try to parse through the program again , adfter increasing the trial value by 1 . Now the code will cycle until it reaches the end function , and we can see the latest value there.

Long Solution:- Take lite
<br />
ShaastraCTF{132}
<br />

## Q12 - Cold & Hot
Opposite to the Hot and Cold game , if burning is returned you are very far from the right answer , and freezing means you are close. Keep in mind Negative numbers are also integers.  
<br />
ShaastraCTF{dLkDF@^HgsGRus63EsT&}
<br />

## Q13 - Event
use a hex editor to open it. In the character area, the first part of the flag is given at the end. Compare the magic bytes in the hexadecimal area with that of a jpg and correct it. Now the image can be opened directly and the 2nd part is displayed. The third part can be found by running an executable file by typing the event name, i.e "CTF" (case insensitive).

<br />

## Q14 - RSA
Since the RSA encoding is only 24 bits , we can compute the 2 prime factors of the public key with some simple python code , which will turn out to be 3623 and 3631 in this case. Using this we can compute the private key which will turn out to be 7513063. Now , decrypt the message recieved using the private key , and then convert the numbers to their respective ASCII values to obtain the flag. 

<br />

## Q15 - About Time
