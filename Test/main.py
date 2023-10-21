
from direct.showbase.ShowBase import ShowBase
from direct.actor.Actor import Actor
from direct.task import Task
from math import pi, sin, cos
from direct.interval.IntervalGlobal import Sequence 
from panda3d.core import Point3


class Game(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        self.model = loader.loadModel('models/environment')
        self.model.reparentTo(render)

        self.model.setPos(-8,42,0)
        self.model.setScale(1,1,1)

        base.camLens.setFov(90)

        pandaActor = Actor('models/panda-model',{'walk': 'models/panda-walk4'})

        pandaActor.setScale(0.005,0.05,0.05)
        pandaActor.reparentTo(render)

        pandaActor.loop('walk')



        posInterval1 = pandaActor.posInterval( 
                                        5, 
                                        Point3(0, -10, 0), 
                                        startPos=Point3(0, 10, 0)) 
 
                                         
        posInterval2 = pandaActor.posInterval( 
                                        5, 
                                        Point3(0, 10, 0), 
                                        startPos=Point3(0, -10, 0)) 
 
        hprInterval1 = pandaActor.hprInterval( 
                                        1, 
                                        Point3(180, 0, 0), 
                                        startHpr=Point3(0, 0, 0)) 
        hprInterval2 = pandaActor.hprInterval( 
                                        1, 
                                        Point3(0, 0, 0), 
                                        startHpr=Point3(180, 0, 0)) 
 
         # створюємо послідовність об'єднавши інтервали 
        self.pandaPace = Sequence(posInterval1, hprInterval1, 
                                  posInterval2, hprInterval2, 
                                  name="pandaPace") 
        #запускаємо послідовність 
        self.pandaPace.loop()



        #self.taskMgr.add(self.MoveCameraTask,'MoveCameraTask')

    def MoveCameraTask (self,task):

        angleDegrees = task.time * 60.0  
        angleRadians = angleDegrees * (pi / 180)

        self.camera.setPos(20 * sin(angleRadians), -20 * cos(angleRadians), 7)
        self.camera.setHpr(angleDegrees, 0, 0)

        return task.cont


game = Game()
game.run()

