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

from slurm_rest.models.v0039_partitions_response import V0039PartitionsResponse

class TestV0039PartitionsResponse(unittest.TestCase):
    """V0039PartitionsResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V0039PartitionsResponse:
        """Test V0039PartitionsResponse
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V0039PartitionsResponse`
        """
        model = V0039PartitionsResponse()
        if include_optional:
            return V0039PartitionsResponse(
                meta = slurm_rest.models.v0/0/39_meta.v0.0.39_meta(
                    plugin = slurm_rest.models.v0_0_39_meta_plugin.v0_0_39_meta_plugin(
                        type = '', 
                        name = '', ), 
                    slurm = slurm_rest.models.v0_0_39_meta_slurm.v0_0_39_meta_Slurm(
                        version = slurm_rest.models.v0_0_39_meta_slurm_version.v0_0_39_meta_Slurm_version(
                            major = 56, 
                            micro = 56, 
                            minor = 56, ), 
                        release = '', ), ),
                errors = [
                    slurm_rest.models.v0/0/39_error.v0.0.39_error(
                        error_number = 56, 
                        error = '', 
                        source = '', 
                        description = '', )
                    ],
                warnings = [
                    slurm_rest.models.v0/0/39_warning.v0.0.39_warning(
                        warning = '', 
                        source = '', 
                        description = '', )
                    ],
                partitions = [
                    slurm_rest.models.v0/0/39_partition_info.v0.0.39_partition_info(
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
                        defaults = slurm_rest.models.v0_0_39_partition_info_defaults.v0_0_39_partition_info_defaults(
                            memory_per_cpu = 56, 
                            time = slurm_rest.models.v0/0/39_uint32_no_val.v0.0.39_uint32_no_val(
                                set = True, 
                                infinite = True, 
                                number = 56, ), 
                            job = '', ), 
                        grace_time = 56, 
                        maximums = slurm_rest.models.v0_0_39_partition_info_maximums.v0_0_39_partition_info_maximums(
                            cpus_per_node = slurm_rest.models.v0/0/39_uint32_no_val.v0.0.39_uint32_no_val(
                                set = True, 
                                infinite = True, 
                                number = 56, ), 
                            cpus_per_socket = , 
                            memory_per_cpu = 56, 
                            shares = 56, 
                            over_time_limit = slurm_rest.models.v0/0/39_uint16_no_val.v0.0.39_uint16_no_val(
                                set = True, 
                                infinite = True, 
                                number = 56, ), ), 
                        minimums = slurm_rest.models.v0_0_40_partition_info_minimums.v0_0_40_partition_info_minimums(), 
                        name = '', 
                        node_sets = '', 
                        priority = slurm_rest.models.v0_0_40_partition_info_priority.v0_0_40_partition_info_priority(
                            job_factor = 56, 
                            tier = 56, ), 
                        timeouts = slurm_rest.models.v0_0_39_partition_info_timeouts.v0_0_39_partition_info_timeouts(
                            resume = slurm_rest.models.v0/0/39_uint16_no_val.v0.0.39_uint16_no_val(
                                set = True, 
                                infinite = True, 
                                number = 56, ), 
                            suspend = , ), 
                        suspend_time = , )
                    ]
            )
        else:
            return V0039PartitionsResponse(
        )
        """

    def testV0039PartitionsResponse(self):
        """Test V0039PartitionsResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()