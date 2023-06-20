#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from example_interfaces.msg import Int64
from example_interfaces.srv import SetBool

class NumberCounterNode(Node):
    def __init__(self):
        super().__init__("number_counter")

        self.number = 0
        self.subscriber_ = self.create_subscription(
            Int64, "number_publish", self.callback_number_count, 10)
        self.get_logger().info("Number counter has been started")

        self.publisher_ = self.create_publisher(
            Int64, "number_counter_pulisher", 10)

        self.reset_counter_service_ = self.create_service(SetBool, "reset_counter", self.callback_reset_counter)

    def callback_reset_counter(self, request, response):
        if request.data:
            self.number = 0
            response.success = True
            response.message = "Counter has been reset to 0"
        else:
            response.success = False
            response.message = "Counter has not been reset to 0"


    def callback_number_count(self, msg):
        # have to convert integer to string to print to the log
        self.number += msg.data
        new_msg = Int64()
        new_msg.data = self.number
        self.publisher_.publish(new_msg)


def main(args=None):
    rclpy.init(args=args)
    node = NumberCounterNode()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == "__main__":
    main()
