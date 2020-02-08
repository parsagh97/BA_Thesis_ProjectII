def crete_database(path, copy_path):
    # os.mkdir(path+'/jpeg')
    # for j in range(1, 11):
    #     os.mkdir(path + '/' + 'jpeg' + str(j))
    for item in os.listdir(path):
        file, _format = os.path.splitext(item)
        if _format:
            im = Image.open(path + '/' + item)
            for k in range(5):
                im.save(copy_path + '/' + file + '_jpeg'+str(k) + _format, 'JPEG', quaity = k*10)
