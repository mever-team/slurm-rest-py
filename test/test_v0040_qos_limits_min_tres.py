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

from slurm_rest.models.v0040_qos_limits_min_tres import V0040QosLimitsMinTres

class TestV0040QosLimitsMinTres(unittest.TestCase):
    """V0040QosLimitsMinTres unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V0040QosLimitsMinTres:
        """Test V0040QosLimitsMinTres
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V0040QosLimitsMinTres`
        """
        model = V0040QosLimitsMinTres()
        if include_optional:
            return V0040QosLimitsMinTres(
                per = slurm_rest.models.v0_0_40_qos_limits_min_tres_per.v0_0_40_qos_limits_min_tres_per(
                    job = [
                        slurm_rest.models.v0/0/40_tres.v0.0.40_tres(
                            type = '', 
                            name = '', 
                            id = 56, 
                            count = 56, )
                        ], )
            )
        else:
            return V0040QosLimitsMinTres(
        )
        """

    def testV0040QosLimitsMinTres(self):
        """Test V0040QosLimitsMinTres"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()