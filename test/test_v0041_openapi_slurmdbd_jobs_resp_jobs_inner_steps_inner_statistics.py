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

from slurm_rest.models.v0041_openapi_slurmdbd_jobs_resp_jobs_inner_steps_inner_statistics import V0041OpenapiSlurmdbdJobsRespJobsInnerStepsInnerStatistics

class TestV0041OpenapiSlurmdbdJobsRespJobsInnerStepsInnerStatistics(unittest.TestCase):
    """V0041OpenapiSlurmdbdJobsRespJobsInnerStepsInnerStatistics unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V0041OpenapiSlurmdbdJobsRespJobsInnerStepsInnerStatistics:
        """Test V0041OpenapiSlurmdbdJobsRespJobsInnerStepsInnerStatistics
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V0041OpenapiSlurmdbdJobsRespJobsInnerStepsInnerStatistics`
        """
        model = V0041OpenapiSlurmdbdJobsRespJobsInnerStepsInnerStatistics()
        if include_optional:
            return V0041OpenapiSlurmdbdJobsRespJobsInnerStepsInnerStatistics(
                cpu = slurm_rest.models.v0_0_40_step_statistics_cpu.v0_0_40_step_statistics_CPU(
                    actual_frequency = 56, ),
                energy = slurm_rest.models.v0_0_41_openapi_slurmdbd_jobs_resp_jobs_inner_steps_inner_statistics_energy.v0_0_41_openapi_slurmdbd_jobs_resp_jobs_inner_steps_inner_statistics_energy(
                    consumed = slurm_rest.models.v0_0_41_openapi_slurmdbd_jobs_resp_jobs_inner_required_memory_per_cpu.v0_0_41_openapi_slurmdbd_jobs_resp_jobs_inner_required_memory_per_cpu(
                        set = True, 
                        infinite = True, 
                        number = 56, ), )
            )
        else:
            return V0041OpenapiSlurmdbdJobsRespJobsInnerStepsInnerStatistics(
        )
        """

    def testV0041OpenapiSlurmdbdJobsRespJobsInnerStepsInnerStatistics(self):
        """Test V0041OpenapiSlurmdbdJobsRespJobsInnerStepsInnerStatistics"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
