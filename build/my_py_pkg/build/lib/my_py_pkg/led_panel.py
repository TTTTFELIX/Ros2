#!/usr/bin/env python3
import rclpy
from rclpy.node import Node

from my_robot_interfaces.msg import LedStateArray
from my_robot_interfaces.srv import SetLed

class LedPanelNode(Node):
    def __init__(self):
        super().__init__("led_panel")
        self.led_states_ = [0,0,0]
        self.led_states_publisher_ = self.create_publisher(LedStateArray, "led_states", 10)
        self.led_states_timer_ = self.create_timer(4, self.led_states_publisher)

        self.set_led_server_ = self.create_service(SetLed, "set_led", self.callback_set_led)

        self.get_logger().info("Led panel has been started.")

    def led_states_publisher(self):
        msg = LedStateArray()
        msg.led_states = self.led_states_
        self.led_states_publisher_.publish(msg)

    def callback_set_led(self, request, response):
        led_number = request.led_number
        states = request.states

        if led_number >= len(self.led_states_) or led_number < 0:
            response.success = False
            return response
        
        if states not in [0,1]:
            response.success = False
            return response

        self.led_states_[led_number] = states
        response.success = True
        self.led_states_publisher()
        return response


def main(args=None):
    rclpy.init(args=args)
    node = LedPanelNode()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == "__main__":
    main()