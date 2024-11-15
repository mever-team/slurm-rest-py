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

from slurm_rest.models.v0041_openapi_job_info_resp_jobs_inner_job_resources import V0041OpenapiJobInfoRespJobsInnerJobResources

class TestV0041OpenapiJobInfoRespJobsInnerJobResources(unittest.TestCase):
    """V0041OpenapiJobInfoRespJobsInnerJobResources unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V0041OpenapiJobInfoRespJobsInnerJobResources:
        """Test V0041OpenapiJobInfoRespJobsInnerJobResources
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V0041OpenapiJobInfoRespJobsInnerJobResources`
        """
        model = V0041OpenapiJobInfoRespJobsInnerJobResources()
        if include_optional:
            return V0041OpenapiJobInfoRespJobsInnerJobResources(
                select_type = [
                    'CPU'
                    ],
                nodes = slurm_rest.models.v0_0_41_openapi_job_info_resp_jobs_inner_job_resources_nodes.v0_0_41_openapi_job_info_resp_jobs_inner_job_resources_nodes(
                    count = 56, 
                    select_type = [
                        'AVAILABLE'
                        ], 
                    list = '', 
                    whole = True, 
                    allocation = [
                        slurm_rest.models.v0_0_41_openapi_job_info_resp_jobs_inner_job_resources_nodes_allocation_inner.v0_0_41_openapi_job_info_resp_jobs_inner_job_resources_nodes_allocation_inner(
                            index = 56, 
                            name = '', 
                            cpus = slurm_rest.models.v0_0_41_openapi_job_info_resp_jobs_inner_job_resources_nodes_allocation_inner_cpus.v0_0_41_openapi_job_info_resp_jobs_inner_job_resources_nodes_allocation_inner_cpus(
                                count = 56, 
                                used = 56, ), 
                            memory = slurm_rest.models.v0_0_41_openapi_job_info_resp_jobs_inner_job_resources_nodes_allocation_inner_memory.v0_0_41_openapi_job_info_resp_jobs_inner_job_resources_nodes_allocation_inner_memory(
                                used = 56, 
                                allocated = 56, ), 
                            sockets = [
                                slurm_rest.models.v0_0_41_openapi_job_info_resp_jobs_inner_job_resources_nodes_allocation_inner_sockets_inner.v0_0_41_openapi_job_info_resp_jobs_inner_job_resources_nodes_allocation_inner_sockets_inner(
                                    index = 56, 
                                    cores = [
                                        slurm_rest.models.v0_0_41_openapi_job_info_resp_jobs_inner_job_resources_nodes_allocation_inner_sockets_inner_cores_inner.v0_0_41_openapi_job_info_resp_jobs_inner_job_resources_nodes_allocation_inner_sockets_inner_cores_inner(
                                            index = 56, 
                                            status = [
                                                'INVALID'
                                                ], )
                                        ], )
                                ], )
                        ], ),
                cpus = 56,
                threads_per_core = slurm_rest.models.v0_0_41_openapi_job_info_resp_jobs_inner_job_resources_threads_per_core.v0_0_41_openapi_job_info_resp_jobs_inner_job_resources_threads_per_core(
                    set = True, 
                    infinite = True, 
                    number = 56, )
            )
        else:
            return V0041OpenapiJobInfoRespJobsInnerJobResources(
                select_type = [
                    'CPU'
                    ],
                cpus = 56,
                threads_per_core = slurm_rest.models.v0_0_41_openapi_job_info_resp_jobs_inner_job_resources_threads_per_core.v0_0_41_openapi_job_info_resp_jobs_inner_job_resources_threads_per_core(
                    set = True, 
                    infinite = True, 
                    number = 56, ),
        )
        """

    def testV0041OpenapiJobInfoRespJobsInnerJobResources(self):
        """Test V0041OpenapiJobInfoRespJobsInnerJobResources"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
