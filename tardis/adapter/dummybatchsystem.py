from ..configuration.configuration import Configuration
from ..interfaces.batchsystemadapter import BatchSystemAdapter
from ..interfaces.batchsystemadapter import MachineStatus


class DummyBatchSystemAdapter(BatchSystemAdapter):
    def __init__(self):
        config = Configuration()
        self.dummy_config = config.BatchSystem

    async def disintegrate_machine(self, dns_name):
        return

    async def drain_machine(self, dns_name):
        return

    async def integrate_machine(self, dns_name):
        return

    async def get_allocation(self, dns_name):
        return self.dummy_config.allocation

    async def get_machine_status(self, dns_name):
        return getattr(MachineStatus, self.dummy_config.machine_status)

    async def get_utilization(self, dns_name):
        return self.dummy_config.utilization