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

from slurm_rest.models.v0041_openapi_job_info_resp_jobs_inner_job_resources_nodes_allocation_inner import V0041OpenapiJobInfoRespJobsInnerJobResourcesNodesAllocationInner

class TestV0041OpenapiJobInfoRespJobsInnerJobResourcesNodesAllocationInner(unittest.TestCase):
    """V0041OpenapiJobInfoRespJobsInnerJobResourcesNodesAllocationInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V0041OpenapiJobInfoRespJobsInnerJobResourcesNodesAllocationInner:
        """Test V0041OpenapiJobInfoRespJobsInnerJobResourcesNodesAllocationInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V0041OpenapiJobInfoRespJobsInnerJobResourcesNodesAllocationInner`
        """
        model = V0041OpenapiJobInfoRespJobsInnerJobResourcesNodesAllocationInner()
        if include_optional:
            return V0041OpenapiJobInfoRespJobsInnerJobResourcesNodesAllocationInner(
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
                    ]
            )
        else:
            return V0041OpenapiJobInfoRespJobsInnerJobResourcesNodesAllocationInner(
                index = 56,
                name = '',
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
                    ],
        )
        """

    def testV0041OpenapiJobInfoRespJobsInnerJobResourcesNodesAllocationInner(self):
        """Test V0041OpenapiJobInfoRespJobsInnerJobResourcesNodesAllocationInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
