from visual import *
MyScene = display(title = 'TERMOMETR',
                  autoscale = False,
                  range = (25,10,10))
MyScene.width = 500
MyScene.height = 600
termExtraCool = box(lenght = .1,
             color = color.blue,
             width = 7,
             height = 4,
             pos = (0, 0,0))
termCool = box(lenght = .1,
             color = color.cyan,
             width = 7,
             height = 4,
             pos = (0, 4,0)  )
termWarm = box(lenght = .1,
             color = color.yellow,
             width = 7,
             height = 4,
             pos = (0, 8,0))
termHot = box(lenght = .1,
             color = color.orange,
             width = 7,
             height = 4,
             pos = (0, 12,0))
termExtraHot = box(lenght = .1,
             color = color.red,
             width = 7,
             height = 4,
             pos = (0, 16,0))

stolbik = cylinder(color = color.red,
                   radius = 0.5,
                   axis = (0, 5, 0),
                   pos =(-0.5,-2, 0))
steklo = cylinder(color = color.white,
                   radius = 0.6,
                   axis = (0, -20, 0),
                   pos =(-0.5,18, 0),
                  opacity = 0.4)
shar = sphere(pos = (-0.5,19.8,0),
              radius = 2,
              color = color.white,
              opacity = 0.4)
deg = label(pos = (3, 0, 3))
sharRtut = sphere(pos = (-0.5, 19.8, 0),
                  radius = 1.9,
                  color = color.red,
                  opacity = 0)
while True :
    try :
        fileRead = open('temp.dt')
        result = fileRead.read()
        print(result)
        stolbik.axis = (0,int(result)/2.5 , 0)
        deg.pos = (-3, int(result)/2.5, -3)
        deg.text = result
        if int(result) > 50 :
            #print("TRUE")
            stolbik.axis = (0, 20, 0)
            deg.pos = (-3, 20, -3)
            deg.text = 'Welcome to Hell!  '+result
            shar.opacity = 0
            sharRtut.opacity  = 1
        else :
            shar.opacity = 0.4
            sharRtut.opacity = 0   
    except ValueError :
        #print("BAD VALUE")
        continue
    fileRead.close() 
