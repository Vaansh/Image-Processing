function q1()
    % read
    I = imread("img/Doc.tiff");

    % initialize parameters and
    % call custom function
    [m, c] = deal(9, 5.5);
    O = adaptive_thresholding(I, m, c);

    % initialize parameters and
    % call built-in function
    s = 0.7;
    T = adaptthresh(I, s);
    M = imbinarize(I, T);

    % compare and save
    imshowpair(O, M, "montage")
    imwrite(O, "img/prog/output.tiff");
end

function [O] = adaptive_thresholding(I, m, c)
    % get size
    [row, col, x] = size(I);

    % initialize empty output
    O = zeros(row, col);

    % create a new image with padded boundary
    boundary_len = floor(m / 2);
    K = padarray(I, [boundary_len, boundary_len]);

    % loop through every pixel
    for i = 1 : row
        for j = 1 : col
            % get average of local window 
            win = K(i : i + m - 1, j : j + m - 1);
            avg = mean(win(:));

            % compute threshold
            thr = avg - c;

            % set output pixel accordingly
            if (I(i, j) >= thr)
                O(i, j) = 1;
            end
        end
    end
end
