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

from slurm_rest.models.v0041_openapi_partition_resp import V0041OpenapiPartitionResp

class TestV0041OpenapiPartitionResp(unittest.TestCase):
    """V0041OpenapiPartitionResp unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V0041OpenapiPartitionResp:
        """Test V0041OpenapiPartitionResp
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V0041OpenapiPartitionResp`
        """
        model = V0041OpenapiPartitionResp()
        if include_optional:
            return V0041OpenapiPartitionResp(
                partitions = [
                    slurm_rest.models.v0_0_41_openapi_partition_resp_partitions_inner.v0_0_41_openapi_partition_resp_partitions_inner(
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
                        select_type = [
                            'CPU'
                            ], 
                        cpus = slurm_rest.models.v0_0_40_partition_info_cpus.v0_0_40_partition_info_cpus(
                            task_binding = 56, 
                            total = 56, ), 
                        defaults = slurm_rest.models.v0_0_41_openapi_partition_resp_partitions_inner_defaults.v0_0_41_openapi_partition_resp_partitions_inner_defaults(
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
                            job = '', ), 
                        grace_time = 56, 
                        maximums = slurm_rest.models.v0_0_41_openapi_partition_resp_partitions_inner_maximums.v0_0_41_openapi_partition_resp_partitions_inner_maximums(
                            cpus_per_node = slurm_rest.models.v0_0_41_openapi_slurmdbd_jobs_resp_jobs_inner_array_task_id.v0_0_41_openapi_slurmdbd_jobs_resp_jobs_inner_array_task_id(
                                set = True, 
                                infinite = True, 
                                number = 56, ), 
                            cpus_per_socket = , 
                            memory_per_cpu = 56, 
                            shares = 56, 
                            oversubscribe = slurm_rest.models.v0_0_40_partition_info_maximums_oversubscribe.v0_0_40_partition_info_maximums_oversubscribe(
                                jobs = 56, 
                                flags = [
                                    'force'
                                    ], ), 
                            over_time_limit = slurm_rest.models.v0_0_41_job_desc_msg_distribution_plane_size.v0_0_41_job_desc_msg_distribution_plane_size(
                                set = True, 
                                infinite = True, 
                                number = 56, ), ), 
                        minimums = slurm_rest.models.v0_0_40_partition_info_minimums.v0_0_40_partition_info_minimums(), 
                        name = '', 
                        node_sets = '', 
                        priority = slurm_rest.models.v0_0_40_partition_info_priority.v0_0_40_partition_info_priority(
                            job_factor = 56, 
                            tier = 56, ), 
                        timeouts = slurm_rest.models.v0_0_41_openapi_partition_resp_partitions_inner_timeouts.v0_0_41_openapi_partition_resp_partitions_inner_timeouts(
                            resume = slurm_rest.models.v0_0_41_job_desc_msg_distribution_plane_size.v0_0_41_job_desc_msg_distribution_plane_size(
                                set = True, 
                                infinite = True, 
                                number = 56, ), 
                            suspend = , ), 
                        partition = slurm_rest.models.v0_0_40_partition_info_partition.v0_0_40_partition_info_partition(
                            state = [
                                'INACTIVE'
                                ], ), 
                        suspend_time = , )
                    ],
                last_update = slurm_rest.models.v0_0_41_openapi_partition_resp_last_update.v0_0_41_openapi_partition_resp_last_update(
                    set = True, 
                    infinite = True, 
                    number = 56, ),
                meta = slurm_rest.models.v0_0_41_openapi_slurmdbd_jobs_resp_meta.v0_0_41_openapi_slurmdbd_jobs_resp_meta(
                    plugin = slurm_rest.models.v0_0_40_openapi_meta_plugin.v0_0_40_openapi_meta_plugin(
                        type = '', 
                        name = '', 
                        data_parser = '', 
                        accounting_storage = '', ), 
                    client = slurm_rest.models.v0_0_40_openapi_meta_client.v0_0_40_openapi_meta_client(
                        source = '', 
                        user = '', 
                        group = '', ), 
                    command = [
                        ''
                        ], 
                    slurm = slurm_rest.models.v0_0_40_openapi_meta_slurm.v0_0_40_openapi_meta_slurm(
                        version = slurm_rest.models.v0_0_40_openapi_meta_slurm_version.v0_0_40_openapi_meta_slurm_version(
                            major = '', 
                            micro = '', 
                            minor = '', ), 
                        release = '', 
                        cluster = '', ), ),
                errors = [
                    slurm_rest.models.v0_0_41_openapi_slurmdbd_jobs_resp_errors_inner.v0_0_41_openapi_slurmdbd_jobs_resp_errors_inner(
                        description = '', 
                        error_number = 56, 
                        error = '', 
                        source = '', )
                    ],
                warnings = [
                    slurm_rest.models.v0_0_41_openapi_slurmdbd_jobs_resp_warnings_inner.v0_0_41_openapi_slurmdbd_jobs_resp_warnings_inner(
                        description = '', 
                        source = '', )
                    ]
            )
        else:
            return V0041OpenapiPartitionResp(
                partitions = [
                    slurm_rest.models.v0_0_41_openapi_partition_resp_partitions_inner.v0_0_41_openapi_partition_resp_partitions_inner(
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
                        select_type = [
                            'CPU'
                            ], 
                        cpus = slurm_rest.models.v0_0_40_partition_info_cpus.v0_0_40_partition_info_cpus(
                            task_binding = 56, 
                            total = 56, ), 
                        defaults = slurm_rest.models.v0_0_41_openapi_partition_resp_partitions_inner_defaults.v0_0_41_openapi_partition_resp_partitions_inner_defaults(
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
                            job = '', ), 
                        grace_time = 56, 
                        maximums = slurm_rest.models.v0_0_41_openapi_partition_resp_partitions_inner_maximums.v0_0_41_openapi_partition_resp_partitions_inner_maximums(
                            cpus_per_node = slurm_rest.models.v0_0_41_openapi_slurmdbd_jobs_resp_jobs_inner_array_task_id.v0_0_41_openapi_slurmdbd_jobs_resp_jobs_inner_array_task_id(
                                set = True, 
                                infinite = True, 
                                number = 56, ), 
                            cpus_per_socket = , 
                            memory_per_cpu = 56, 
                            shares = 56, 
                            oversubscribe = slurm_rest.models.v0_0_40_partition_info_maximums_oversubscribe.v0_0_40_partition_info_maximums_oversubscribe(
                                jobs = 56, 
                                flags = [
                                    'force'
                                    ], ), 
                            over_time_limit = slurm_rest.models.v0_0_41_job_desc_msg_distribution_plane_size.v0_0_41_job_desc_msg_distribution_plane_size(
                                set = True, 
                                infinite = True, 
                                number = 56, ), ), 
                        minimums = slurm_rest.models.v0_0_40_partition_info_minimums.v0_0_40_partition_info_minimums(), 
                        name = '', 
                        node_sets = '', 
                        priority = slurm_rest.models.v0_0_40_partition_info_priority.v0_0_40_partition_info_priority(
                            job_factor = 56, 
                            tier = 56, ), 
                        timeouts = slurm_rest.models.v0_0_41_openapi_partition_resp_partitions_inner_timeouts.v0_0_41_openapi_partition_resp_partitions_inner_timeouts(
                            resume = slurm_rest.models.v0_0_41_job_desc_msg_distribution_plane_size.v0_0_41_job_desc_msg_distribution_plane_size(
                                set = True, 
                                infinite = True, 
                                number = 56, ), 
                            suspend = , ), 
                        partition = slurm_rest.models.v0_0_40_partition_info_partition.v0_0_40_partition_info_partition(
                            state = [
                                'INACTIVE'
                                ], ), 
                        suspend_time = , )
                    ],
                last_update = slurm_rest.models.v0_0_41_openapi_partition_resp_last_update.v0_0_41_openapi_partition_resp_last_update(
                    set = True, 
                    infinite = True, 
                    number = 56, ),
        )
        """

    def testV0041OpenapiPartitionResp(self):
        """Test V0041OpenapiPartitionResp"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
