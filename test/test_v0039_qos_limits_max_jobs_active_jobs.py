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

from slurm_rest.models.v0039_qos_limits_max_jobs_active_jobs import V0039QosLimitsMaxJobsActiveJobs

class TestV0039QosLimitsMaxJobsActiveJobs(unittest.TestCase):
    """V0039QosLimitsMaxJobsActiveJobs unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V0039QosLimitsMaxJobsActiveJobs:
        """Test V0039QosLimitsMaxJobsActiveJobs
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V0039QosLimitsMaxJobsActiveJobs`
        """
        model = V0039QosLimitsMaxJobsActiveJobs()
        if include_optional:
            return V0039QosLimitsMaxJobsActiveJobs(
                per = slurm_rest.models.v0_0_39_qos_limits_max_jobs_active_jobs_per.v0_0_39_qos_limits_max_jobs_active_jobs_per(
                    account = slurm_rest.models.v0/0/39_uint32_no_val.v0.0.39_uint32_no_val(
                        set = True, 
                        infinite = True, 
                        number = 56, ), 
                    user = slurm_rest.models.v0/0/39_uint32_no_val.v0.0.39_uint32_no_val(
                        set = True, 
                        infinite = True, 
                        number = 56, ), )
            )
        else:
            return V0039QosLimitsMaxJobsActiveJobs(
        )
        """

    def testV0039QosLimitsMaxJobsActiveJobs(self):
        """Test V0039QosLimitsMaxJobsActiveJobs"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()