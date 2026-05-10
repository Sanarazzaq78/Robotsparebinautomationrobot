from robocorp.tasks import task
from robocorp import browser


def get_orders():
    orders = ["Order 1", "Order 2"]
    return orders


def open_robot_order_website():
    browser.goto("https://robotsparebinindustries.com/#/robot-order")

    orders = get_orders()
    print(orders)


@task
def order_robots_from_RobotSpareBin():
    open_robot_order_website()