def crete_database(path, copy_path):
    for item in os.listdir(path):
        file, _format = os.path.splitext(item)
        if _format:
            im = Image.open(path + '/' + item)
            for k in range(1, 15):
                im_filter = im.filter(ImageFilter.GaussianBlur(k))
                im_filter.save(copy_path + '/' + file + '_gaussian'+str(k)+_format, 'JPEG', quality=100)
