% Inputs for total burn time of fuel
days = 20;
hours = 6;
minutes = 43;

% Input for rate of fuel burn
fuelRate = 5; % grams/second

% calculation
totalHours = days * 24 + hours;
totalMinutes = totalHours * 60 + minutes;
totalTimeInSeconds = 60 * totalMinutes;

% Output
totalFuelUsed = totalTimeInSeconds * fuelrate; % grams
disp('The total fuel used in grams is:');
disp(totalFuelUsed);
