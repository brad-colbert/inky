"""Test hardware mocking tools."""


class MockSMBus:
    """Mock a Python SMBus instance.

    Redirects read/write operations to self.regs.

    """

    def __init__(self, i2c_bus):
        """Initialize mock SMBus class.

        :param i2c_bus: unused, maintains compatibility with smbus.SMBus(n)

        """
        self.regs = [0 for _ in range(255)]

    def write_i2c_block_data(self, i2c_address, register, values):
        """Write a block of i2c data bytes."""
        # self.regs[register:register + len(values)] = values
        pass

    def read_i2c_block_data(self, i2c_address, register, length):
        """Read a block of i2c data bytes."""
        return self.regs[register:register + length]
