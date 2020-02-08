def rotate(path):
    for items in os.listdir(path):
        file, _format = os.path.splitext(items)
        if _format:
            im = Image.open(path + '/' + items)
            rotated = im.rotate(randint(0, 360))
            rotated.save(path + '/rotate/' + file + '_rotated' + _format, 'JPEG', quality=90)
