#!/usr/bin/env python3
import rclpy
from rclpy.node import Node

from example_interfaces.msg import String

class RobotNewsStationNode(Node):
    def __init__(self):
        super().__init__("robot_news_station")
        self.declare_parameter("robot_name", "No.38")

        self.robot_name = self.get_parameter("robot_name").value
        self.publisher_ = self.create_publisher(String, "robot_news", 10)
        self.timer_ = self.create_timer(1, self.publish_news)
        self.get_logger().info("Hi, this is " + self.robot_name +" from the Robot News Station!")


    def publish_news(self):
        msg = String()
        msg.data = "Hello, this is " + str(self.robot_name) + " from robot news station."
        self.publisher_.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node = RobotNewsStationNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main() 
