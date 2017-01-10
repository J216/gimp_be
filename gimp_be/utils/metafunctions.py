#list functions
def listFunctions():
    import types
    funcs=[f for f in globals().values() if type(f) == types.FunctionType]
    list_func=[]
    for fnc in funcs:
        list_func.append(str(fnc)[10:-15]+'()')
    return list_func


# help information
def help():
    doLog('help()')
    helpString = (" "
                  "\n##"
                  "\n## Now with more fruit, and related flavours, than ever/"
                  "\n##"
                  "\n############################################################"
                  "\n#         Da func that Jared made     ver " + version + "            #"
                                                                             "\n############################################################"
                                                                             "\n#            imageSetup(w,h)"
                                                                             "\n#            imageSavePNG(sName,simage,itName,sClose)          <--itName sClose are bool; for name iteration, close after saving"
                                                                             "\n#            imageSaveJPG(sName,simage,itName,sClose)          <--same as imageSavePNG() but saves as JPEG instead of PNG"
                                                                             "\n#            qX()                                            <--quick export currently using jpg"
                                                                             "\n#            qXJ()                                           <--quick jpg export"
                                                                             "\n#            qXP()                                           <--quick png export"
                                                                             "\n#            qS()                                            <--quick setup of new image 1920x1080"
                                                                             "\n#            qT()                                            <--quick tweet with default message"
                                                                             "\n#            stringIncrement(serial_string)                  <--takes a string of ucase and lcase and adds one"
                                                                             "\n#            updateImage()                                   <--updates image to active drawable area"
                                                                             "\n#            addNewLayer(image,opacity,msk)                    <--msk is bool for adding mask layer"
                                                                             "\n#            loadLayer(image_file)"
                                                                             "\n#            loadDirLayer(image_folder, opt)"
                                                                             "\n#            layerScaleAll()"
                                                                             "\n#            flatten(image)"
                                                                             "\n#            clear()                                         <--clears active drawable"
                                                                             "\n#            brushSize(sizeIn)"
                                                                             "\n#            brushOpacity(opIn)"
                                                                             "\n#            brushColor()                                    <--() sets random foreground and background color, (int,int,int) sets foreground"
                                                                             "\n#            randomBrush()"
                                                                             "\n#            randomDynamics()"
                                                                             "\n#            drawBrush(x1,y1)"
                                                                             "\n#            drawMultiBrush(brush_strokes,options)"
                                                                             "\n#            drawStar(x1,y1,siz)"
                                                                             "\n#            drawRandomStars(starNum,size)"
                                                                             "\n#            randomCircleFill(num,size,opt,sq)"
                                                                             "\n#            randomRectFill(num,size,opt,sq)"
                                                                             "\n#            randomBlend()"
                                                                             "\n#            drawRays(num,rayLength,centerX,centerY)"
                                                                             "\n#            drawRaysCenter(num,rayLength,centerX,centerY)"
                                                                             "\n#            randomSizeBrushStrokes(num)"
                                                                             "\n#            drawBars(barNum,opt)"
                                                                             "\n#            drawCNT()"
                                                                             "\n#            drawSinWave(barSpace,barLen,mag,x_offset,y_offset)"
                                                                             "\n#            drawSinWaveDouble(barSpace,barLen,mag)"
                                                                             "\n#            drawTree(x1, y1, angle, depth)                  <--draws fractal tree of given depth 40 degree branching"
                                                                             "\n#            drawTriTree(x1, y1, angle, depth)"
                                                                             "\n#            drawColorTriTree(x1, y1, angle, depth)"
                                                                             "\n#            drawOddTree(x1, y1, angle, depth)"
                                                                             "\n#            drawForestTree(x1, y1, angle, depth, size)"
                                                                             "\n#            tweetImage(twitter_message, image_path)         <--tweet image using subprocess py tweet_image.py"
                                                                             "\n#            closeAll()                                      <--only works on images opened by python"
                                                                             "\n#            doPainting(paint_string)                        <--see doPainting('help')"
                                                                             "\n#            helpInfo()                                      <--it shows this screen"
                                                                             "\n#"
                                                                             "\n##"
                                                                             "\n############################################################"
                  )
    logDump()
    print helpString
