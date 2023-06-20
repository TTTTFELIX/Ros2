#!/usr/bin/env python3
import rclpy
from rclpy.node import Node


class MyNewNode(Node):
    def __init__(self):
        super().__init__("MyFirstNewNode")

def main(args = None):
    rclpy.init(args=args)
    node = MyNewNode()
    rclpy.spin(node)
    rclpy.shutdown()



if __name__ == "__main__":
    main()