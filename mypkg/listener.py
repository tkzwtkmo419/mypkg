#SPDX-FileCopyrightText: 2022 Takumi Takazawa tkzwpen0419@outlook.jp
#SPDX-License=Identifier: BSD-3-Clause

import rclpy
from rclpy.node import Node
def cb(msg):
    global node
    node.get_logger().info("Listen: %d" % msg.data)

rclpy.init()
node = Node("listener")
pub = node.create_subscription(Int16, "countup", cb, 10)

rclpy.spin(node)

