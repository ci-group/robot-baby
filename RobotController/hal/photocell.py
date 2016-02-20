from RobotController.hal.PCF8591P import PCF8591P

READING_RANGE = 255


class Photocell(PCF8591P):

    def __init__(self, __i2cBus, __addr):
        self.__init__(__i2cBus, __addr)

    def readADC(self, __val=PCF8591P.CHANNEL[0]):
        return 1 + self.readADC(__val) / -READING_RANGE