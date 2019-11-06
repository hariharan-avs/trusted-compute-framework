import json
import logging
import automation_framework.worker.worker_params as worker
from automation_framework.utilities.tamper_utility import tamper_object

logger = logging.getLogger(__name__)

class WorkerUpdate():
    def __init__(self):
        self.id_obj = {"jsonrpc": "2.0", "method": "WorkerUpdate", "id": 11}
        self.params_obj = {}
        self.details_obj = {}

    def add_json_values(self, input_json, worker_obj, tamper):

        input_json_temp = input_json

        if "workerId" in input_json_temp["params"].keys() :
            if input_json_temp["params"]["workerId"] != "" :
                self.set_worker_id(input_json_temp["params"]["workerId"])
            else :
                worker_id = worker_obj.worker_id
                self.set_worker_id(worker_id)

        if "id" in input_json_temp.keys() :
            self.set_request_id(input_json_temp["id"])

        if "details" in input_json_temp["params"].keys() :
            if ("hashingAlgorithm" in
                 input_json_temp["params"]["details"].keys()) :
                if input_json_temp["params"]["details"]["hashingAlgorithm"] != "" :
                    self.set_hashing_algorithm(
                    input_json_temp["params"]["details"]["hashingAlgorithm"])
                else :
                    self.set_hashing_algorithm(worker_obj.hashing_algorithm)

            if ("signingAlgorithm" in
                 input_json_temp["params"]["details"].keys()) :
                self.set_signing_algorithm(
                input_json_temp["params"]["details"]["signingAlgorithm"])

            if ("keyEncryptionAlgorithm" in
                 input_json_temp["params"]["details"].keys()) :
                self.set_key_encryption_algorithm(
                input_json_temp["params"]["details"]["keyEncryptionAlgorithm"])

            if ("dataEncryptionAlgorithm" in
                 input_json_temp["params"]["details"].keys()) :
                self.set_data_encryption_algorithm(
                input_json_temp["params"]["details"]["dataEncryptionAlgorithm"])

        # self.params_obj = tamper_object(self.params_obj.copy(), tamper)
        for key in tamper["params"].keys() :
            param = key
            value = tamper["params"][key]
            self.set_unknown_parameter(param, value)

    def set_unknown_parameter(self, param, value):
        self.params_obj[param] = value

    def set_worker_id(self, worker_id):
        self.params_obj["workerId"] = worker_id

    def set_request_id(self, request_id):
        self.id_obj["id"] = request_id

    def set_hashing_algorithm(self, hashing_algorithm):
        self.details_obj["hashingAlgorithm"] = hashing_algorithm

    def set_signing_algorithm(self, signing_algorithm):
        self.details_obj["signingAlgorithm"] = signing_algorithm

    def set_key_encryption_algorithm(self, key_encryption_algorithm):
        self.details_obj["keyEncryptionAlgorithm"] = key_encryption_algorithm

    def set_data_encryption_algorithm(self, data_encryption_algorithm):
        self.details_obj["dataEncryptionAlgorithm"] = data_encryption_algorithm

    def get_params(self):
        return self.params_obj.copy()

    def get_details(self):
        return self.details_obj.copy()

    def to_string(self):
        json_rpc_request = self.id_obj
        json_rpc_request["params"] = self.get_params()
        json_rpc_request["params"]["details"] = self.get_details()

        return json.dumps(json_rpc_request, indent=4)
