import requests
from aeiotconf import SvcAddress


class AEEndpoint:
    svcAddress = SvcAddress()
    def execute_algorithm(self, algorithm_id):
        execution = {"algorithm": algorithm_id}
        resp = requests.post(self.svcAddress.aeAddr()+"executions", json=execution)
        return resp.status_code

