#!/usr/bin/env python3

from BlazeposeRenderer import BlazeposeRenderer
from BlazeposeDepthai import BlazeposeDepthai


import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError




def pose_publisher()

        publisher = rospy.Publisher('pose_img', Image)
        br = CvBridge()


        tracker = BlazeposeDepthai(input_src='rgb', 
                                   pd_model=None,
                                   lm_model=None,
                                   smoothing=True,   
                                   xyz=False,            
                                   crop=True,
                                   internal_fps=None,
                                   internal_frame_height=640,
                                   force_detection=False,
                                   stats=True,
                                   trace=False)

        renderer = BlazeposeRenderer(
            tracker, 
            show_3d=None, 
            output=None)



        while True:
            # Run blazepose on next frame
            frame, body = tracker.next_frame()
            if frame is None: break

            # Draw 2d skeleton
            frame = renderer.draw(frame, body)
            key = renderer.waitKey(delay=1)
            if key == 27 or key == ord('q'):
                break

            publisher.publish(br.cv2_to_imgmsg(frame))
        

    


if __name__ == '__main__':
    rospy.init_node('pose_estimator')
    
    try:
        pose_publisher()
    except rospy.ROSInterruptException:
        pass

    blazepose.renderer.exit()
    blazepose.tracker.exit()










