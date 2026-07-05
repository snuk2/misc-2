rockData = csvread('rocks.csv', 1);
samples = rockData(:,1);
mass = rockData(:,2);
density = rockData(:,3);
metallicity = rockData(:,4);