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

from slurm_rest.models.v0041_openapi_job_info_resp_jobs_inner_job_resources_nodes import V0041OpenapiJobInfoRespJobsInnerJobResourcesNodes

class TestV0041OpenapiJobInfoRespJobsInnerJobResourcesNodes(unittest.TestCase):
    """V0041OpenapiJobInfoRespJobsInnerJobResourcesNodes unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V0041OpenapiJobInfoRespJobsInnerJobResourcesNodes:
        """Test V0041OpenapiJobInfoRespJobsInnerJobResourcesNodes
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V0041OpenapiJobInfoRespJobsInnerJobResourcesNodes`
        """
        model = V0041OpenapiJobInfoRespJobsInnerJobResourcesNodes()
        if include_optional:
            return V0041OpenapiJobInfoRespJobsInnerJobResourcesNodes(
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
                    ]
            )
        else:
            return V0041OpenapiJobInfoRespJobsInnerJobResourcesNodes(
        )
        """

    def testV0041OpenapiJobInfoRespJobsInnerJobResourcesNodes(self):
        """Test V0041OpenapiJobInfoRespJobsInnerJobResourcesNodes"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()