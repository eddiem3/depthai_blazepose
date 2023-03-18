#!/usr/bin/env python3

from BlazeposeRenderer import BlazeposeRenderer
from BlazeposeDepthai import BlazeposeDepthai


import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge




class BlazePosePublisher(Node):
    def __init__(self):
        super().__init__('pose_publisher')
        self.publisher_ = self.create_publisher(Image,'pose_img', 10)
        timer_period = 0.1
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.br = CvBridge()


        self.tracker = BlazeposeDepthai(input_src='rgb', 
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

        self.renderer = BlazeposeRenderer(
            self.tracker, 
            show_3d=None, 
            output=None)

    def timer_callback(self):

        while True:
            # Run blazepose on next frame
            frame, body = self.tracker.next_frame()
            if frame is None: break

            # Draw 2d skeleton
            frame = self.renderer.draw(frame, body)
            key = self.renderer.waitKey(delay=1)
            if key == 27 or key == ord('q'):
                break

            self.publisher_.publish(self.br.cv2_to_imgmsg(frame))
        


def main(args=None):
    rclpy.init(args=args)

    blazepose = BlazePosePublisher()

    rclpy.spin(blazepose)

    blazepose.renderer.exit()
    blazepose.tracker.exit()


    minimal_publisher.destroy_node()
    rclpy.shutdown()

    


if __name__ == '__main__':
    main()
        








