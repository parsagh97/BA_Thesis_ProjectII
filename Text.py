def crete_database(path,path_to_font):
    for i in range(1, 11):
        os.mkdir(path+'/text'+str(i))
    for item in os.listdir(path):
        file, _format = os.path.splitext(item)
        if _format:
            # im = Image.open(path + '/' + item)
            for k in range(1, 11):
                im = Image.open(path+'/'+item)
                width, height = im.size
                draw = ImageDraw.Draw(im)
                font = ImageFont.truetype(path_to_font, 15*k)
                draw.text((0,0), str(file),
                          (randint(100, 255), randint(100, 255), randint(100, 255)), font=font)
                im.save(path+'/text'+str(k)+'/'+ file +'_text'+ _format, 'JPEG', quality=100)
