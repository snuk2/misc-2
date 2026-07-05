function [numPallets] = additionalPallets(roofHeight, pallets, palletHeight)
    numPallets = (roofHeight - (pallets.*palletHeight)) ./ palletHeight;
    numPallets = fix(numPallets);
    numPallets = sum(sum(numPallets));
end

% count rocks greater than 0.65 me

