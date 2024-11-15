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

from slurm_rest.models.v0041_openapi_slurmdbd_jobs_resp_jobs_inner_steps_inner_cpu_requested_frequency import V0041OpenapiSlurmdbdJobsRespJobsInnerStepsInnerCPURequestedFrequency

class TestV0041OpenapiSlurmdbdJobsRespJobsInnerStepsInnerCPURequestedFrequency(unittest.TestCase):
    """V0041OpenapiSlurmdbdJobsRespJobsInnerStepsInnerCPURequestedFrequency unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V0041OpenapiSlurmdbdJobsRespJobsInnerStepsInnerCPURequestedFrequency:
        """Test V0041OpenapiSlurmdbdJobsRespJobsInnerStepsInnerCPURequestedFrequency
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V0041OpenapiSlurmdbdJobsRespJobsInnerStepsInnerCPURequestedFrequency`
        """
        model = V0041OpenapiSlurmdbdJobsRespJobsInnerStepsInnerCPURequestedFrequency()
        if include_optional:
            return V0041OpenapiSlurmdbdJobsRespJobsInnerStepsInnerCPURequestedFrequency(
                min = slurm_rest.models.v0_0_41_openapi_slurmdbd_jobs_resp_jobs_inner_array_task_id.v0_0_41_openapi_slurmdbd_jobs_resp_jobs_inner_array_task_id(
                    set = True, 
                    infinite = True, 
                    number = 56, ),
                max = slurm_rest.models.v0_0_41_openapi_slurmdbd_jobs_resp_jobs_inner_array_task_id.v0_0_41_openapi_slurmdbd_jobs_resp_jobs_inner_array_task_id(
                    set = True, 
                    infinite = True, 
                    number = 56, )
            )
        else:
            return V0041OpenapiSlurmdbdJobsRespJobsInnerStepsInnerCPURequestedFrequency(
        )
        """

    def testV0041OpenapiSlurmdbdJobsRespJobsInnerStepsInnerCPURequestedFrequency(self):
        """Test V0041OpenapiSlurmdbdJobsRespJobsInnerStepsInnerCPURequestedFrequency"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
