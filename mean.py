def crete_database(path, copy_path):
    for item in os.listdir(path):
        file, _format = os.path.splitext(item)
        if _format:
            im = cv2.imread(path + '/' + item)
            for k in range(1, 16):
                figure_size = k*2
                new_image = cv2.blur(im, (figure_size, figure_size))
                cv2.imwrite(copy_path +'/' + file + '_rotate'+str(figure_size) + _format, new_image)
