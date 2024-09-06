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

from slurm_rest.models.v0040_partition_info import V0040PartitionInfo

class TestV0040PartitionInfo(unittest.TestCase):
    """V0040PartitionInfo unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V0040PartitionInfo:
        """Test V0040PartitionInfo
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V0040PartitionInfo`
        """
        model = V0040PartitionInfo()
        if include_optional:
            return V0040PartitionInfo(
                nodes = slurm_rest.models.v0_0_40_partition_info_nodes.v0_0_40_partition_info_nodes(
                    allowed_allocation = '', 
                    configured = '', 
                    total = 56, ),
                accounts = slurm_rest.models.v0_0_40_partition_info_accounts.v0_0_40_partition_info_accounts(
                    allowed = '', 
                    deny = '', ),
                groups = slurm_rest.models.v0_0_40_partition_info_groups.v0_0_40_partition_info_groups(
                    allowed = '', ),
                qos = slurm_rest.models.v0_0_40_partition_info_qos.v0_0_40_partition_info_qos(
                    allowed = '', 
                    deny = '', 
                    assigned = '', ),
                alternate = '',
                tres = slurm_rest.models.v0_0_40_partition_info_tres.v0_0_40_partition_info_tres(
                    billing_weights = '', 
                    configured = '', ),
                cluster = '',
                cpus = slurm_rest.models.v0_0_40_partition_info_cpus.v0_0_40_partition_info_cpus(
                    task_binding = 56, 
                    total = 56, ),
                defaults = slurm_rest.models.v0_0_40_partition_info_defaults.v0_0_40_partition_info_defaults(
                    memory_per_cpu = 56, 
                    partition_memory_per_cpu = slurm_rest.models.v0/0/40_uint64_no_val.v0.0.40_uint64_no_val(
                        set = True, 
                        infinite = True, 
                        number = 56, ), 
                    partition_memory_per_node = slurm_rest.models.v0/0/40_uint64_no_val.v0.0.40_uint64_no_val(
                        set = True, 
                        infinite = True, 
                        number = 56, ), 
                    time = slurm_rest.models.v0/0/40_uint32_no_val.v0.0.40_uint32_no_val(
                        set = True, 
                        infinite = True, 
                        number = 56, ), 
                    job = '', ),
                grace_time = 56,
                maximums = slurm_rest.models.v0_0_40_partition_info_maximums.v0_0_40_partition_info_maximums(
                    cpus_per_node = slurm_rest.models.v0/0/40_uint32_no_val.v0.0.40_uint32_no_val(
                        set = True, 
                        infinite = True, 
                        number = 56, ), 
                    cpus_per_socket = slurm_rest.models.v0/0/40_uint32_no_val.v0.0.40_uint32_no_val(
                        set = True, 
                        infinite = True, 
                        number = 56, ), 
                    memory_per_cpu = 56, 
                    partition_memory_per_cpu = slurm_rest.models.v0/0/40_uint64_no_val.v0.0.40_uint64_no_val(
                        set = True, 
                        infinite = True, 
                        number = 56, ), 
                    partition_memory_per_node = slurm_rest.models.v0/0/40_uint64_no_val.v0.0.40_uint64_no_val(
                        set = True, 
                        infinite = True, 
                        number = 56, ), 
                    nodes = , 
                    shares = 56, 
                    oversubscribe = slurm_rest.models.v0_0_40_partition_info_maximums_oversubscribe.v0_0_40_partition_info_maximums_oversubscribe(
                        jobs = 56, 
                        flags = [
                            'force'
                            ], ), 
                    time = , 
                    over_time_limit = slurm_rest.models.v0/0/40_uint16_no_val.v0.0.40_uint16_no_val(
                        set = True, 
                        infinite = True, 
                        number = 56, ), ),
                minimums = slurm_rest.models.v0_0_40_partition_info_minimums.v0_0_40_partition_info_minimums(
                    nodes = 56, ),
                name = '',
                node_sets = '',
                priority = slurm_rest.models.v0_0_40_partition_info_priority.v0_0_40_partition_info_priority(
                    job_factor = 56, 
                    tier = 56, ),
                timeouts = slurm_rest.models.v0_0_40_partition_info_timeouts.v0_0_40_partition_info_timeouts(
                    resume = slurm_rest.models.v0/0/40_uint16_no_val.v0.0.40_uint16_no_val(
                        set = True, 
                        infinite = True, 
                        number = 56, ), 
                    suspend = slurm_rest.models.v0/0/40_uint16_no_val.v0.0.40_uint16_no_val(
                        set = True, 
                        infinite = True, 
                        number = 56, ), ),
                partition = slurm_rest.models.v0_0_40_partition_info_partition.v0_0_40_partition_info_partition(
                    state = [
                        'INACTIVE'
                        ], ),
                suspend_time = slurm_rest.models.v0/0/40_uint32_no_val.v0.0.40_uint32_no_val(
                    set = True, 
                    infinite = True, 
                    number = 56, )
            )
        else:
            return V0040PartitionInfo(
        )
        """

    def testV0040PartitionInfo(self):
        """Test V0040PartitionInfo"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
