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

from slurm_rest.models.v0040_update_node_msg import V0040UpdateNodeMsg

class TestV0040UpdateNodeMsg(unittest.TestCase):
    """V0040UpdateNodeMsg unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V0040UpdateNodeMsg:
        """Test V0040UpdateNodeMsg
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V0040UpdateNodeMsg`
        """
        model = V0040UpdateNodeMsg()
        if include_optional:
            return V0040UpdateNodeMsg(
                comment = '',
                cpu_bind = 56,
                extra = '',
                features = [
                    ''
                    ],
                features_act = [
                    ''
                    ],
                gres = '',
                address = [
                    ''
                    ],
                hostname = [
                    ''
                    ],
                name = [
                    ''
                    ],
                state = [
                    'INVALID'
                    ],
                reason = '',
                reason_uid = '',
                resume_after = slurm_rest.models.v0/0/40_uint32_no_val.v0.0.40_uint32_no_val(
                    set = True, 
                    infinite = True, 
                    number = 56, ),
                weight = slurm_rest.models.v0/0/40_uint32_no_val.v0.0.40_uint32_no_val(
                    set = True, 
                    infinite = True, 
                    number = 56, )
            )
        else:
            return V0040UpdateNodeMsg(
        )
        """

    def testV0040UpdateNodeMsg(self):
        """Test V0040UpdateNodeMsg"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()