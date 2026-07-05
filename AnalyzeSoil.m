%% Lab 1 Sample MATLAB Script
%
% This is a sample of a MATLAB script. A script is a computer program, and
% it executes one statement at a time, e.g. line-by-line.
%
% Run this script by typing the name of the script in the Command Window,
% like this:
%
% >> AnalyzeSoil
%
% and then hitting "Enter". See what is displayed in the Command Window!

%% Initialize variables
sodium = 10.90;
potassium = 68.22;
calcium = 25.41;
magnesium = 13.77;

%% Calculate Exchangable Sodium Percentage
ESP = sodium / (potassium + calcium + magnesium + sodium);

%% Display the results to the Command Window

disp('This soil sample''s ESP is:');
disp(ESP);

%% Change the numbers 
%
% You can change the numbers in the "Initialize variables" section, save
% this file, and then re-run the script. You will get a different number
% for the value of ESP. 