function hashd = imp(x)
    img = imread(x);
    img_resize = imresize(img, [512 512]); %set to 512 to be devisable to 8

    img_lab = rgb2lab(img_resize);
    L = img_lab(:,:,1);

    %convert to non-overlaping blocs of 8x8
    [size_x, size_y] = size(L);
    Kx = 8; Ky = 8;

    new_matrix = uint8(zeros(size_x,size_y));
    new_matrix(1:size_x, 1:size_y) = L;
    blocks_of_img = mat2cell(new_matrix, repmat(Kx,[1 size(new_matrix,1)/Kx]), repmat(Ky,[1 size(new_matrix,2)/Ky]));

    dct_of_blocks = cell (64,64);

    for i=1:64
      for j=1:64
        dct_of_blocks {i,j} = dct2(blocks_of_img{i,j});
      end
    end

    new_dct_image = cell (512, 512);

    for i = 0:63
        for j=0:63
            a = reshape(dct_of_blocks{i+1,j+1}, 8,8)';
            for m = 1:8
                for n = 1:8
                    new_dct_image{i*8+m, j*8+n} = a(m, n);
                end
            end
        end
    end

    mat_of_dct_image = cell2mat(new_dct_image);
    [LL, LH, HL, HH] = dwt2(mat_of_dct_image, 'db1');
    LL_blocks = cell(32);
    for i = 1:32
        for j = 1:32
            LL_blocks{i,j} = LL((i-1)*8+1:i*8, (j-1)*8+1:j*8);
        end
    end
    LL_mean_of_blocks = zeros(32);
    for i = 1:32
        for j = 1:32
            LL_mean_of_blocks(i,j) = mean(LL_blocks{i,j},'all');
        end
    end

    LL_mean = mean(LL_mean_of_blocks, 'all');

    for i = 1:32
        for j = 1:32
            if(LL_mean_of_blocks(i,j) < LL_mean)
                LL_mean_of_blocks(i,j) = 0;
            else
                LL_mean_of_blocks(i,j) = 1;
            end
        end
    end
    hashd = reshape(LL_mean_of_blocks',[1 size(LL_mean_of_blocks,1)*size(LL_mean_of_blocks,2)]);
