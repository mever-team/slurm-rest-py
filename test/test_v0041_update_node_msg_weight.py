# coding: utf-8

"""
    Slurm REST API

    API to access and control Slurm

    The version of the OpenAPI document: Slurm-24.05.2&openapi/slurmdbd&openapi/v0.0.39&openapi/dbv0.0.39&openapi/slurmctld
    Contact: sales@schedmd.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from slurm_rest.models.v0041_update_node_msg_weight import V0041UpdateNodeMsgWeight

class TestV0041UpdateNodeMsgWeight(unittest.TestCase):
    """V0041UpdateNodeMsgWeight unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V0041UpdateNodeMsgWeight:
        """Test V0041UpdateNodeMsgWeight
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V0041UpdateNodeMsgWeight`
        """
        model = V0041UpdateNodeMsgWeight()
        if include_optional:
            return V0041UpdateNodeMsgWeight(
                set = True,
                infinite = True,
                number = 56
            )
        else:
            return V0041UpdateNodeMsgWeight(
        )
        """

    def testV0041UpdateNodeMsgWeight(self):
        """Test V0041UpdateNodeMsgWeight"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()