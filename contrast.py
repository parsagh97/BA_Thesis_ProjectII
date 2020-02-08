def crete_database(path):
    for item in os.listdir(path):
        file, _format = os.path.splitext(item)
        if _format:
            im = Image.open(path + '/' + item)
            for k in range(1, 11):
                enhancer = ImageEnhance.Contrast(im)
                enhanced_im = enhancer.enhance(k/2)
                enhanced_im.save(path + '/contrast'+str(k*5)+'/' + file + '_contrast' + _format, 'JPEG', quality=100)
