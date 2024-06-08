import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2

class VideoSaver(Node):
    def __init__(self):
        super().__init__('video_saver')
        self.subscription = self.create_subscription(
            Image,
            '/aiformula_sensing/zedx/left_image/undistorted',
            self.listener_callback,
            10)
        self.bridge = CvBridge()
        self.video_path = "/path/to/save/video/output.mp4"
        self.out = cv2.VideoWriter(self.video_path, cv2.VideoWriter_fourcc(*'mp4v'), 30, (1920, 1080))

    def listener_callback(self, msg):
        cv_image = self.bridge.imgmsg_to_cv2(msg, "bgr8")
        self.out.write(cv_image)
        self.get_logger().info('Frame added to video.')

    def destroy_node(self):
        self.out.destroy()
        super().destroy_node()

def main(args=None):
    rclpy.init(args=args)
    video_saver = VideoSaver()
    rclpy.spin(video_saver)
    video_saver.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
