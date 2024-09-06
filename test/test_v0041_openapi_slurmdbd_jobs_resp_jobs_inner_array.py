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

from slurm_rest.models.v0041_openapi_slurmdbd_jobs_resp_jobs_inner_array import V0041OpenapiSlurmdbdJobsRespJobsInnerArray

class TestV0041OpenapiSlurmdbdJobsRespJobsInnerArray(unittest.TestCase):
    """V0041OpenapiSlurmdbdJobsRespJobsInnerArray unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V0041OpenapiSlurmdbdJobsRespJobsInnerArray:
        """Test V0041OpenapiSlurmdbdJobsRespJobsInnerArray
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V0041OpenapiSlurmdbdJobsRespJobsInnerArray`
        """
        model = V0041OpenapiSlurmdbdJobsRespJobsInnerArray()
        if include_optional:
            return V0041OpenapiSlurmdbdJobsRespJobsInnerArray(
                job_id = 56,
                limits = slurm_rest.models.v0_0_40_job_array_limits.v0_0_40_job_array_limits(
                    max = slurm_rest.models.v0_0_40_job_array_limits_max.v0_0_40_job_array_limits_max(
                        running = slurm_rest.models.v0_0_40_job_array_limits_max_running.v0_0_40_job_array_limits_max_running(
                            tasks = 56, ), ), ),
                task_id = slurm_rest.models.v0_0_41_openapi_slurmdbd_jobs_resp_jobs_inner_array_task_id.v0_0_41_openapi_slurmdbd_jobs_resp_jobs_inner_array_task_id(
                    set = True, 
                    infinite = True, 
                    number = 56, ),
                task = ''
            )
        else:
            return V0041OpenapiSlurmdbdJobsRespJobsInnerArray(
        )
        """

    def testV0041OpenapiSlurmdbdJobsRespJobsInnerArray(self):
        """Test V0041OpenapiSlurmdbdJobsRespJobsInnerArray"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
