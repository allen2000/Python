def conshow(*args):
    outv=""
    for i in list(*args):
        outv=outv+i+"-"
    print(outv[0:-1])

conshow(('we','love','python',"!"))