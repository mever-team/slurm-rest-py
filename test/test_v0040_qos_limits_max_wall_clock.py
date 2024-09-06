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

from slurm_rest.models.v0040_qos_limits_max_wall_clock import V0040QosLimitsMaxWallClock

class TestV0040QosLimitsMaxWallClock(unittest.TestCase):
    """V0040QosLimitsMaxWallClock unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V0040QosLimitsMaxWallClock:
        """Test V0040QosLimitsMaxWallClock
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V0040QosLimitsMaxWallClock`
        """
        model = V0040QosLimitsMaxWallClock()
        if include_optional:
            return V0040QosLimitsMaxWallClock(
                per = slurm_rest.models.v0_0_40_qos_limits_max_wall_clock_per.v0_0_40_qos_limits_max_wall_clock_per(
                    qos = slurm_rest.models.v0/0/40_uint32_no_val.v0.0.40_uint32_no_val(
                        set = True, 
                        infinite = True, 
                        number = 56, ), 
                    job = slurm_rest.models.v0/0/40_uint32_no_val.v0.0.40_uint32_no_val(
                        set = True, 
                        infinite = True, 
                        number = 56, ), )
            )
        else:
            return V0040QosLimitsMaxWallClock(
        )
        """

    def testV0040QosLimitsMaxWallClock(self):
        """Test V0040QosLimitsMaxWallClock"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
