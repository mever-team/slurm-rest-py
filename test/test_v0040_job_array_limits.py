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

from slurm_rest.models.v0040_job_array_limits import V0040JobArrayLimits

class TestV0040JobArrayLimits(unittest.TestCase):
    """V0040JobArrayLimits unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V0040JobArrayLimits:
        """Test V0040JobArrayLimits
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V0040JobArrayLimits`
        """
        model = V0040JobArrayLimits()
        if include_optional:
            return V0040JobArrayLimits(
                max = slurm_rest.models.v0_0_40_job_array_limits_max.v0_0_40_job_array_limits_max(
                    running = slurm_rest.models.v0_0_40_job_array_limits_max_running.v0_0_40_job_array_limits_max_running(
                        tasks = 56, ), )
            )
        else:
            return V0040JobArrayLimits(
        )
        """

    def testV0040JobArrayLimits(self):
        """Test V0040JobArrayLimits"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
