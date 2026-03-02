class Device:
    def __init__(self):
        self._status = "OFF"

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        print(f"Status changed from {self._status} to {value}")
        self._status = value

# Test Code
if __name__ == "__main__":
    device = Device()
    print(f"Current status: {device.status}")
    
    device.status = "ON"
    device.status = "SLEEP"
    device.status = "OFF"
