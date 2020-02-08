function out = Untitled(x)
    img = imread(x);
    imwrite(img, 'img.tiff');
    img = imread('img.tiff');
    I = imresize(img, [128 128]);
    a = size(I);
    new = reshape(I, [a(1)*a(2) a(3)]);
    zero = zeros(128*128,1);
    q2 = [zero new];
    I2 = zeros(128 ,128);
    for i = 1:128
        for j = 1:128
            I2(i,j) = (I(i,j,1).^2 + I(i,j,2).^2 + I(i,j,3).^2);
        end
    end

    I_temp = I2;


    for i = 1:128
        for j = 1:128
           I_temp(i,j) = I_temp(i,j)/(128*128);
        end
    end
    avg_g = mean(I_temp, 'all');

    avg = zeros(16,16);

    m = 1;
    n = 1;

    for i = 1:16
        m = 1 + 8*(i-1);
        for j = 1:16
            n = 1 +8*(j-1);
            if mean(I_temp(m:m+7 ,n:n+7), 'all') > avg_g
                avg(i,j) = 1;
            else
                avg(i,j) = 0;
            end
        end
    end
    out = reshape(avg, [1 16*16]);
end
  
 
        
