def crete_database(path, copy_path):
    # os.mkdir(path+'/resize')
    for item in os.listdir(path):
        file, _format = os.path.splitext(item)
        if _format:
            im = Image.open(path + '/' + item)
            a,b = im.size
            for k in range(1, 9):
                imResize = im.resize((int(a*k*0.25), int(b*k*0.25)), Image.ANTIALIAS)
                imResize.save(copy_path+'/'+file+'_resize'+str(k*0.25)+_format,'JPEG', quality=100) 
