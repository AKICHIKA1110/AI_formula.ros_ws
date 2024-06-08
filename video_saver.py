import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
import cv2
from cv_bridge import CvBridge

class VideoSaver(Node):
    def __init__(self):
        super().__init__('video_saver')
        self.subscription = self.create_subscription(
            Image,
            '/zed2/zed_node/left/image_rect_color', #ZEDカメラからのトピック名
            self.listener_callback,
            10)
        self.subscription  # prevent unused variable warning

        self.bridge = CvBridge()
        self.out = cv2.VideoWriter('output.avi', cv2.VideoWriter_fourcc(*'XVID'), 30.0, (1280, 720))

    def listener_callback(self, msg):
        cv_image = self.bridge.imgmsg_to_cv2(msg, "bgr8")
        self.out.write(cv_image)
        self.get_logger().info('Video frame saved')

    def destroy_node(self):
        self.out.close()
        super().destroy_node()

def main(args=None):
    rclpy.init(args=args)
    video_saver = VideoSaver()
    try:
        rclpy.spin(video_saver)
    except KeyboardInterrupt:
        pass
    finally:
        video_saver.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
