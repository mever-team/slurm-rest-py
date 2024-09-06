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

from slurm_rest.models.v0039_job_array import V0039JobArray

class TestV0039JobArray(unittest.TestCase):
    """V0039JobArray unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V0039JobArray:
        """Test V0039JobArray
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V0039JobArray`
        """
        model = V0039JobArray()
        if include_optional:
            return V0039JobArray(
                job_id = 56,
                limits = slurm_rest.models.v0_0_40_job_array_limits.v0_0_40_job_array_limits(
                    max = slurm_rest.models.v0_0_40_job_array_limits_max.v0_0_40_job_array_limits_max(
                        running = slurm_rest.models.v0_0_40_job_array_limits_max_running.v0_0_40_job_array_limits_max_running(
                            tasks = 56, ), ), ),
                task_id = slurm_rest.models.v0/0/39_uint32_no_val.v0.0.39_uint32_no_val(
                    set = True, 
                    infinite = True, 
                    number = 56, ),
                task = ''
            )
        else:
            return V0039JobArray(
        )
        """

    def testV0039JobArray(self):
        """Test V0039JobArray"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
