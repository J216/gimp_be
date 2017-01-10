def saveJPG(file_name):
    """
    Save image JPG par: name, close
    :param file_name:
    :return:
    """
    from gimpfu import pdb,gimp,CLIP_TO_IMAGE
    import datetime
    time_stamp = datetime.datetime.now()
    image = gimp.image_list()[0]
    new_image = pdb.gimp_image_duplicate(image)
    layer = pdb.gimp_image_merge_visible_layers(new_image, CLIP_TO_IMAGE)
    comment = "Digital Art - " + str(time_stamp)
    pdb.file_jpeg_save(new_image, layer, file_name, file_name, .65, 0, 0, 0, comment, 2, 1, 0, 0)
    pdb.gimp_image_delete(new_image)


def saveXCFProject(file_in):
    """
    save project file of current image
    :param file_in:
    :return:
    """
    from gimpfu import pdb, gimp
    image = gimp.image_list()[0]
    drawable = pdb.gimp_image_active_drawable(image)
    pdb.gimp_xcf_save(1, image, drawable, file_in, file_in)


def savePNG(sName, image, itName, sClose):
    """
    Save image PNG par: name, close
    :param sName:
    :param image:
    :param itName:
    :param sClose:
    :return:
    """
    global export_file_name
    global default_save_path
    from string import letters
    from gimpfu import pdb, CLIP_TO_IMAGE
    from gimp_be.utils.string_tools import stringIncrement
    import datetime, re, os, random

    #replace slash with forward
    sName=sName.replace('\\','/')

    #extract path
    temp_path = sName[:sName.rfind("/") + 1]

    #extract file name
    temp_file = sName[sName.rfind("/") + 1:]

    #regex search for -ABC-1234 in name
    p = re.compile('-\D\D\D-\d\d\d\d')
    m = p.search(sName)

    #removes extension from file name
    if "." in temp_file:
        pureName = temp_file[:temp_file.rfind('.')]
        temp_file = pureName
    else:
        pureName = temp_file
    m = p.search(pureName)

    #Handles file already existing with the same name
    if os.path.isfile(temp_path + pureName + ".png"):
        #if regex doesn't find the pattern it appends -ABC-1000 before extension
        if m is None:
            temp_file = pureName + "-" + random.choice(letters) + random.choice(letters) + random.choice(
                letters) + "-" + `random.randrange(1000, 2000)`
        #check if new file name already exists and increment if needed
        while os.path.isfile(temp_path + temp_file + ".png"):
            intEnd = pureName[len(pureName) - 4:len(pureName)]
            letId = pureName[len(pureName) - 8:len(pureName) - 5]
            # Handle roll over case for 9999
            if intEnd == "9999":
                letId = stringIncrement(letId)
                pureName = pureName[:len(pureName) - 8] + letId + pureName[len(pureName) - 5:]
            numIntEnd = 0
            numIntEnd = int(intEnd)
            numIntEnd = numIntEnd + 1
            pureName = pureName[:len(pureName) - 5]
            intEnd = `numIntEnd`
            if len(intEnd) < 4:
                intEnd = "0" + intEnd
                if len(intEnd) < 4:
                    intEnd = "0" + intEnd
                    if len(intEnd) < 4:
                        intEnd = "0" + intEnd
            temp_file = pureName + "-" + intEnd[len(intEnd) - 4:]
    elif not os.path.isfile(temp_path + pureName + ".png") and itName:
        temp_file = pureName + "-" + random.choice(letters) + random.choice(letters) + random.choice(
            letters) + "-" + `random.randrange(1000, 2000)`

    #SAVE FILE WITH UNIQUE NAME
    try:
        new_image = pdb.gimp_image_duplicate(image)
        layer = pdb.gimp_image_merge_visible_layers(new_image, CLIP_TO_IMAGE)
        sName = temp_path + temp_file + ".png"
        export_file_name = sName
        pdb.gimp_file_save(new_image, layer, sName, '?')
        pdb.gimp_image_delete(new_image)
        if sClose:
            pdb.gimp_image_delete(image)
        return True
    except:
        return False




