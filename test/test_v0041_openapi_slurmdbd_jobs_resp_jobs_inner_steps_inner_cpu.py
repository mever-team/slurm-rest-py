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

from slurm_rest.models.v0041_openapi_slurmdbd_jobs_resp_jobs_inner_steps_inner_cpu import V0041OpenapiSlurmdbdJobsRespJobsInnerStepsInnerCPU

class TestV0041OpenapiSlurmdbdJobsRespJobsInnerStepsInnerCPU(unittest.TestCase):
    """V0041OpenapiSlurmdbdJobsRespJobsInnerStepsInnerCPU unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V0041OpenapiSlurmdbdJobsRespJobsInnerStepsInnerCPU:
        """Test V0041OpenapiSlurmdbdJobsRespJobsInnerStepsInnerCPU
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V0041OpenapiSlurmdbdJobsRespJobsInnerStepsInnerCPU`
        """
        model = V0041OpenapiSlurmdbdJobsRespJobsInnerStepsInnerCPU()
        if include_optional:
            return V0041OpenapiSlurmdbdJobsRespJobsInnerStepsInnerCPU(
                requested_frequency = slurm_rest.models.v0_0_41_openapi_slurmdbd_jobs_resp_jobs_inner_steps_inner_cpu_requested_frequency.v0_0_41_openapi_slurmdbd_jobs_resp_jobs_inner_steps_inner_CPU_requested_frequency(
                    min = slurm_rest.models.v0_0_41_openapi_slurmdbd_jobs_resp_jobs_inner_array_task_id.v0_0_41_openapi_slurmdbd_jobs_resp_jobs_inner_array_task_id(
                        set = True, 
                        infinite = True, 
                        number = 56, ), 
                    max = slurm_rest.models.v0_0_41_openapi_slurmdbd_jobs_resp_jobs_inner_array_task_id.v0_0_41_openapi_slurmdbd_jobs_resp_jobs_inner_array_task_id(
                        set = True, 
                        infinite = True, 
                        number = 56, ), ),
                governor = ''
            )
        else:
            return V0041OpenapiSlurmdbdJobsRespJobsInnerStepsInnerCPU(
        )
        """

    def testV0041OpenapiSlurmdbdJobsRespJobsInnerStepsInnerCPU(self):
        """Test V0041OpenapiSlurmdbdJobsRespJobsInnerStepsInnerCPU"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()