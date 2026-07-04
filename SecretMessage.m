
clear 
close all


% reveal a secret message

img1 = imread('cat1.png');
figure(1)
imshow(img1);

img2 = imread('cat2.png');
[newImg] = reveal(img1, img2);
figure(2);
imshow(newImg);

% provide alt text for the message
% TODO: Change <NUMBER> to be the number that is revealed once you get
% the function debugged, and change <WORD> to be the word that is
% revealed.
alt_text = strcat("There are two pieces of information: " , ...
        "In white text (brightness = 255) is the number <NUMBER>. ", ...
        "In black text (brightness = 0) is the word '<WORD>'.");

disp(alt_text);
