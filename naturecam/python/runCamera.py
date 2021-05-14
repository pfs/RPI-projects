#!/usr/bin/env/python

from datetime import datetime,date
from optparse import OptionParser
from picamera import PiCamera
from gpiozero import MotionSensor
from time import sleep
import os

def capture(camera,options):

        """captures the image to a file"""

        outURL=options.output
        n=options.n
        delay=float(options.delay)/1000.
        
        baseDir=os.path.dirname(outURL)

        #prepare a daily archive folder
        today=date.today().isoformat()
        archive=os.path.join(baseDir,today)
        os.system('mkdir -p %s'%archive)

        #take n pictures
	try:
                now=datetime.now().isoformat()
                baseOutF=os.path.join(archive,'photo_%s_{counter:03d}.png'%now)
                i=0
                for outF in camera.capture_continuous(baseOutF):                                
                        sleep(delay)
                        i+=1
                        if i>=n: break
                os.system('cp -v %s %s'%(outF,outURL))                

	except Exception as e:
		print '<'*50
                print 'Something went wrong'
		print e
		print '<'*50

        
def captureAfterPIRTrigger(camera,options):

        """captures the image to a file after a PIR trigger"""

        try:
                pir = MotionSensor(4,sample_rate=10,queue_len=20,threshold=0.5,partial=False)
                pir.wait_for_motion()
                
                capture(camera,options)

                pir.close()

        except Exception as e:
                print '<'*50
                print 'Something went wrong'
                print e
                print '<'*50                                           
                     
def main():

	parser = OptionParser()
	parser.add_option("-c", "--cmd",     dest="cmd",    help="command")
	parser.add_option("-o", "--output",  dest="output", help="output")
        parser.add_option("-n", "--nphotos", dest="n",      help="# photos",   default=1,   type=int)
        parser.add_option("-d", "--delay",   dest="delay",  help="delay (ms)", default=250, type=int)
	(options, args) = parser.parse_args()

        """
        see documentation @
        https://picamera.readthedocs.io/en/release-1.13/
        https://gpiozero.readthedocs.io/en/stable/api_input.html#motion-sensor-d-sun-pir
        """
        
	print 'Starting camera'

	camera = PiCamera()
	print 'Running',options.cmd
	if options.cmd=='capture':
		capture(camera,options)
        if options.cmd=='trigcapture':
                captureAfterPIRTrigger(camera,options)
                
	print 'Closing camera'
	camera.close()

        
if __name__ == "__main__":
    main()
