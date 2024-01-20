class APPLE:

    def __init__(self, department_name, device_type, devices_count):
        self.department_name = department_name
        self.device_type = device_type
        self.devices_count = devices_count

    def devices_for_department(self):
        print(f'For {self.department_name} there\'re {self.devices_count} {self.device_type} in usage now')

    def new_devices(self, devices):
        self.devices_count = self.devices_count + devices

    def broken_devices(self, broken):
        self.devices_count = (100 * broken) / self.devices_count

    @staticmethod
    def department_efficiency(releases_amount):
        efficiency = 12 / releases_amount
        return efficiency

    @classmethod
    def allowed_dev(cls, department_name, device_type, devices_count):
        if devices_count > 23:
            raise PermissionError('To much devices')
        else:
            return cls(department_name, device_type, devices_count)


QA = APPLE('QA department', 'ios_13', 22)
QA.devices_for_department()
QA.new_devices(20)
print(QA.devices_count)
QA.broken_devices(6)
print(QA.devices_count)
QA = APPLE.allowed_dev('QA department', 'ios_13', 22)
efficiency = APPLE.department_efficiency(6)
print(efficiency)
