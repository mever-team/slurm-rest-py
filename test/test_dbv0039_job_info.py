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

from slurm_rest.models.dbv0039_job_info import Dbv0039JobInfo

class TestDbv0039JobInfo(unittest.TestCase):
    """Dbv0039JobInfo unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Dbv0039JobInfo:
        """Test Dbv0039JobInfo
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Dbv0039JobInfo`
        """
        model = Dbv0039JobInfo()
        if include_optional:
            return Dbv0039JobInfo(
                meta = slurm_rest.models.dbv0/0/39_meta.dbv0.0.39_meta(
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
                    slurm_rest.models.dbv0/0/39_error.dbv0.0.39_error(
                        error_number = 56, 
                        error = '', 
                        source = '', 
                        description = '', )
                    ],
                warnings = [
                    slurm_rest.models.dbv0/0/39_warning.dbv0.0.39_warning(
                        warning = '', 
                        source = '', 
                        description = '', )
                    ],
                jobs = [
                    slurm_rest.models.v0/0/39_job.v0.0.39_job(
                        account = '', 
                        comment = slurm_rest.models.v0_0_40_job_comment.v0_0_40_job_comment(
                            administrator = '', 
                            job = '', 
                            system = '', ), 
                        allocation_nodes = 56, 
                        array = slurm_rest.models.v0_0_39_job_array.v0_0_39_job_array(
                            job_id = 56, 
                            limits = slurm_rest.models.v0_0_40_job_array_limits.v0_0_40_job_array_limits(
                                max = slurm_rest.models.v0_0_40_job_array_limits_max.v0_0_40_job_array_limits_max(
                                    running = slurm_rest.models.v0_0_40_job_array_limits_max_running.v0_0_40_job_array_limits_max_running(
                                        tasks = 56, ), ), ), 
                            task_id = slurm_rest.models.v0/0/39_uint32_no_val.v0.0.39_uint32_no_val(
                                set = True, 
                                infinite = True, 
                                number = 56, ), 
                            task = '', ), 
                        association = slurm_rest.models.v0/0/39_assoc_short.v0.0.39_assoc_short(
                            account = '', 
                            cluster = '', 
                            partition = '', 
                            user = '', ), 
                        block = '', 
                        cluster = '', 
                        constraints = '', 
                        container = '', 
                        derived_exit_code = slurm_rest.models.v0/0/39_job_exit_code.v0.0.39_job_exit_code(
                            status = '', 
                            return_code = 56, 
                            signal = slurm_rest.models.v0_0_39_job_exit_code_signal.v0_0_39_job_exit_code_signal(
                                signal_id = 56, 
                                name = '', ), ), 
                        time = slurm_rest.models.v0_0_39_job_time.v0_0_39_job_time(
                            elapsed = 56, 
                            eligible = 56, 
                            end = 56, 
                            start = 56, 
                            submission = 56, 
                            suspended = 56, 
                            system = slurm_rest.models.v0_0_40_job_time_system.v0_0_40_job_time_system(
                                seconds = 56, 
                                microseconds = 56, ), 
                            limit = slurm_rest.models.v0/0/39_uint32_no_val.v0.0.39_uint32_no_val(
                                set = True, 
                                infinite = True, 
                                number = 56, ), 
                            total = slurm_rest.models.v0_0_40_job_time_system.v0_0_40_job_time_system(
                                seconds = 56, 
                                microseconds = 56, ), 
                            user = , ), 
                        exit_code = slurm_rest.models.v0/0/39_job_exit_code.v0.0.39_job_exit_code(
                            status = '', 
                            return_code = 56, ), 
                        extra = '', 
                        failed_node = '', 
                        flags = [
                            'NONE'
                            ], 
                        group = '', 
                        het = slurm_rest.models.v0_0_39_job_het.v0_0_39_job_het(
                            job_id = 56, 
                            job_offset = , ), 
                        job_id = 56, 
                        name = '', 
                        licenses = '', 
                        mcs = slurm_rest.models.v0_0_40_job_mcs.v0_0_40_job_mcs(
                            label = '', ), 
                        nodes = '', 
                        partition = '', 
                        hold = True, 
                        priority = , 
                        qos = '', 
                        required = slurm_rest.models.v0_0_39_job_required.v0_0_39_job_required(
                            cpus = 56, 
                            memory_per_cpu = slurm_rest.models.v0/0/39_uint64_no_val.v0.0.39_uint64_no_val(
                                set = True, 
                                infinite = True, 
                                number = 56, ), 
                            memory_per_node = slurm_rest.models.v0/0/39_uint64_no_val.v0.0.39_uint64_no_val(
                                set = True, 
                                infinite = True, 
                                number = 56, ), 
                            memory = 56, ), 
                        kill_request_user = '', 
                        reservation = slurm_rest.models.v0_0_40_job_reservation.v0_0_40_job_reservation(
                            id = 56, 
                            name = '', ), 
                        script = '', 
                        state = slurm_rest.models.v0_0_39_job_state.v0_0_39_job_state(
                            current = '', 
                            reason = '', ), 
                        steps = [
                            slurm_rest.models.v0/0/39_step.v0.0.39_step(
                                nodes = slurm_rest.models.v0_0_39_step_nodes.v0_0_39_step_nodes(
                                    count = 56, 
                                    range = '', 
                                    list = [
                                        ''
                                        ], ), 
                                tasks = slurm_rest.models.v0_0_40_step_tasks.v0_0_40_step_tasks(
                                    count = 56, ), 
                                pid = '', 
                                cpu = slurm_rest.models.v0_0_39_step_cpu.v0_0_39_step_CPU(
                                    requested_frequency = slurm_rest.models.v0_0_39_step_cpu_requested_frequency.v0_0_39_step_CPU_requested_frequency(
                                        min = , ), 
                                    governor = '', ), 
                                kill_request_user = '', 
                                statistics = slurm_rest.models.v0_0_39_step_statistics.v0_0_39_step_statistics(
                                    energy = slurm_rest.models.v0_0_39_step_statistics_energy.v0_0_39_step_statistics_energy(
                                        consumed = , ), ), 
                                step = slurm_rest.models.v0_0_39_step_step.v0_0_39_step_step(
                                    id = slurm_rest.models.v0/0/39_slurm_step_id.v0.0.39_slurm_step_id(
                                        job_id = 56, 
                                        step_het_component = 56, 
                                        step_id = '', ), 
                                    name = '', ), 
                                task = slurm_rest.models.v0_0_40_step_task.v0_0_40_step_task(
                                    distribution = '', ), 
                                tres = slurm_rest.models.v0_0_39_step_tres.v0_0_39_step_tres(
                                    requested = slurm_rest.models.v0_0_39_step_tres_requested.v0_0_39_step_tres_requested(
                                        average = [
                                            slurm_rest.models.v0/0/39_tres.v0.0.39_tres(
                                                type = '', 
                                                name = '', 
                                                count = 56, )
                                            ], ), 
                                    allocated = [
                                        slurm_rest.models.v0/0/39_tres.v0.0.39_tres(
                                            type = '', 
                                            name = '', 
                                            count = 56, )
                                        ], ), )
                            ], 
                        submit_line = '', 
                        tres = slurm_rest.models.v0_0_39_job_tres.v0_0_39_job_tres(), 
                        used_gres = '', 
                        user = '', 
                        wckey = slurm_rest.models.v0/0/39_wckey_tag.v0.0.39_wckey_tag(), 
                        working_directory = '', )
                    ]
            )
        else:
            return Dbv0039JobInfo(
        )
        """

    def testDbv0039JobInfo(self):
        """Test Dbv0039JobInfo"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
