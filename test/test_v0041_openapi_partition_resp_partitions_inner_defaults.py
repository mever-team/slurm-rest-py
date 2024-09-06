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

from slurm_rest.models.v0041_openapi_partition_resp_partitions_inner_defaults import V0041OpenapiPartitionRespPartitionsInnerDefaults

class TestV0041OpenapiPartitionRespPartitionsInnerDefaults(unittest.TestCase):
    """V0041OpenapiPartitionRespPartitionsInnerDefaults unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V0041OpenapiPartitionRespPartitionsInnerDefaults:
        """Test V0041OpenapiPartitionRespPartitionsInnerDefaults
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V0041OpenapiPartitionRespPartitionsInnerDefaults`
        """
        model = V0041OpenapiPartitionRespPartitionsInnerDefaults()
        if include_optional:
            return V0041OpenapiPartitionRespPartitionsInnerDefaults(
                memory_per_cpu = 56,
                partition_memory_per_cpu = slurm_rest.models.v0_0_41_openapi_slurmdbd_jobs_resp_jobs_inner_required_memory_per_cpu.v0_0_41_openapi_slurmdbd_jobs_resp_jobs_inner_required_memory_per_cpu(
                    set = True, 
                    infinite = True, 
                    number = 56, ),
                partition_memory_per_node = slurm_rest.models.v0_0_41_openapi_slurmdbd_jobs_resp_jobs_inner_required_memory_per_cpu.v0_0_41_openapi_slurmdbd_jobs_resp_jobs_inner_required_memory_per_cpu(
                    set = True, 
                    infinite = True, 
                    number = 56, ),
                time = slurm_rest.models.v0_0_41_openapi_slurmdbd_jobs_resp_jobs_inner_array_task_id.v0_0_41_openapi_slurmdbd_jobs_resp_jobs_inner_array_task_id(
                    set = True, 
                    infinite = True, 
                    number = 56, ),
                job = ''
            )
        else:
            return V0041OpenapiPartitionRespPartitionsInnerDefaults(
        )
        """

    def testV0041OpenapiPartitionRespPartitionsInnerDefaults(self):
        """Test V0041OpenapiPartitionRespPartitionsInnerDefaults"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
