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

from slurm_rest.models.v0040_job import V0040Job

class TestV0040Job(unittest.TestCase):
    """V0040Job unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V0040Job:
        """Test V0040Job
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V0040Job`
        """
        model = V0040Job()
        if include_optional:
            return V0040Job(
                account = '',
                comment = slurm_rest.models.v0_0_40_job_comment.v0_0_40_job_comment(
                    administrator = '', 
                    job = '', 
                    system = '', ),
                allocation_nodes = 56,
                array = slurm_rest.models.v0_0_40_job_array.v0_0_40_job_array(
                    job_id = 56, 
                    limits = slurm_rest.models.v0_0_40_job_array_limits.v0_0_40_job_array_limits(
                        max = slurm_rest.models.v0_0_40_job_array_limits_max.v0_0_40_job_array_limits_max(
                            running = slurm_rest.models.v0_0_40_job_array_limits_max_running.v0_0_40_job_array_limits_max_running(
                                tasks = 56, ), ), ), 
                    task_id = slurm_rest.models.v0/0/40_uint32_no_val.v0.0.40_uint32_no_val(
                        set = True, 
                        infinite = True, 
                        number = 56, ), 
                    task = '', ),
                association = slurm_rest.models.v0/0/40_assoc_short.v0.0.40_assoc_short(
                    account = '', 
                    cluster = '', 
                    partition = '', 
                    user = '', 
                    id = 56, ),
                block = '',
                cluster = '',
                constraints = '',
                container = '',
                derived_exit_code = slurm_rest.models.v0/0/40_process_exit_code_verbose.v0.0.40_process_exit_code_verbose(
                    status = [
                        'INVALID'
                        ], 
                    return_code = slurm_rest.models.v0/0/40_uint32_no_val.v0.0.40_uint32_no_val(
                        set = True, 
                        infinite = True, 
                        number = 56, ), 
                    signal = slurm_rest.models.v0_0_40_process_exit_code_verbose_signal.v0_0_40_process_exit_code_verbose_signal(
                        id = slurm_rest.models.v0/0/40_uint16_no_val.v0.0.40_uint16_no_val(
                            set = True, 
                            infinite = True, 
                            number = 56, ), 
                        name = '', ), ),
                time = slurm_rest.models.v0_0_40_job_time.v0_0_40_job_time(
                    elapsed = 56, 
                    eligible = 56, 
                    end = 56, 
                    start = 56, 
                    submission = 56, 
                    suspended = 56, 
                    system = slurm_rest.models.v0_0_40_job_time_system.v0_0_40_job_time_system(
                        seconds = 56, 
                        microseconds = 56, ), 
                    limit = slurm_rest.models.v0/0/40_uint32_no_val.v0.0.40_uint32_no_val(
                        set = True, 
                        infinite = True, 
                        number = 56, ), 
                    total = slurm_rest.models.v0_0_40_job_time_system.v0_0_40_job_time_system(
                        seconds = 56, 
                        microseconds = 56, ), 
                    user = , ),
                exit_code = slurm_rest.models.v0/0/40_process_exit_code_verbose.v0.0.40_process_exit_code_verbose(
                    status = [
                        'INVALID'
                        ], 
                    return_code = slurm_rest.models.v0/0/40_uint32_no_val.v0.0.40_uint32_no_val(
                        set = True, 
                        infinite = True, 
                        number = 56, ), 
                    signal = slurm_rest.models.v0_0_40_process_exit_code_verbose_signal.v0_0_40_process_exit_code_verbose_signal(
                        id = slurm_rest.models.v0/0/40_uint16_no_val.v0.0.40_uint16_no_val(
                            set = True, 
                            infinite = True, 
                            number = 56, ), 
                        name = '', ), ),
                extra = '',
                failed_node = '',
                flags = [
                    'NONE'
                    ],
                group = '',
                het = slurm_rest.models.v0_0_40_job_het.v0_0_40_job_het(
                    job_id = 56, 
                    job_offset = slurm_rest.models.v0/0/40_uint32_no_val.v0.0.40_uint32_no_val(
                        set = True, 
                        infinite = True, 
                        number = 56, ), ),
                job_id = 56,
                name = '',
                licenses = '',
                mcs = slurm_rest.models.v0_0_40_job_mcs.v0_0_40_job_mcs(
                    label = '', ),
                nodes = '',
                partition = '',
                hold = True,
                priority = slurm_rest.models.v0/0/40_uint32_no_val.v0.0.40_uint32_no_val(
                    set = True, 
                    infinite = True, 
                    number = 56, ),
                qos = '',
                required = slurm_rest.models.v0_0_40_job_required.v0_0_40_job_required(
                    cpus = 56, 
                    memory_per_cpu = slurm_rest.models.v0/0/40_uint64_no_val.v0.0.40_uint64_no_val(
                        set = True, 
                        infinite = True, 
                        number = 56, ), 
                    memory_per_node = slurm_rest.models.v0/0/40_uint64_no_val.v0.0.40_uint64_no_val(
                        set = True, 
                        infinite = True, 
                        number = 56, ), ),
                kill_request_user = '',
                reservation = slurm_rest.models.v0_0_40_job_reservation.v0_0_40_job_reservation(
                    id = 56, 
                    name = '', ),
                script = '',
                state = slurm_rest.models.v0_0_40_job_state.v0_0_40_job_state(
                    current = [
                        'PENDING'
                        ], 
                    reason = '', ),
                steps = [
                    slurm_rest.models.v0/0/40_step.v0.0.40_step(
                        time = slurm_rest.models.v0_0_40_step_time.v0_0_40_step_time(
                            elapsed = 56, 
                            end = slurm_rest.models.v0/0/40_uint64_no_val.v0.0.40_uint64_no_val(
                                set = True, 
                                infinite = True, 
                                number = 56, ), 
                            start = slurm_rest.models.v0/0/40_uint64_no_val.v0.0.40_uint64_no_val(
                                set = True, 
                                infinite = True, 
                                number = 56, ), 
                            suspended = 56, 
                            system = slurm_rest.models.v0_0_40_step_time_system.v0_0_40_step_time_system(
                                seconds = 56, 
                                microseconds = 56, ), 
                            total = slurm_rest.models.v0_0_40_step_time_system.v0_0_40_step_time_system(
                                seconds = 56, 
                                microseconds = 56, ), 
                            user = , ), 
                        exit_code = slurm_rest.models.v0/0/40_process_exit_code_verbose.v0.0.40_process_exit_code_verbose(
                            status = [
                                'INVALID'
                                ], 
                            return_code = slurm_rest.models.v0/0/40_uint32_no_val.v0.0.40_uint32_no_val(
                                set = True, 
                                infinite = True, 
                                number = 56, ), 
                            signal = slurm_rest.models.v0_0_40_process_exit_code_verbose_signal.v0_0_40_process_exit_code_verbose_signal(
                                id = slurm_rest.models.v0/0/40_uint16_no_val.v0.0.40_uint16_no_val(
                                    set = True, 
                                    infinite = True, 
                                    number = 56, ), 
                                name = '', ), ), 
                        nodes = slurm_rest.models.v0_0_40_step_nodes.v0_0_40_step_nodes(
                            count = 56, 
                            range = '', 
                            list = [
                                ''
                                ], ), 
                        tasks = slurm_rest.models.v0_0_40_step_tasks.v0_0_40_step_tasks(
                            count = 56, ), 
                        pid = '', 
                        cpu = slurm_rest.models.v0_0_40_step_cpu.v0_0_40_step_CPU(
                            requested_frequency = slurm_rest.models.v0_0_40_step_cpu_requested_frequency.v0_0_40_step_CPU_requested_frequency(
                                min = slurm_rest.models.v0/0/40_uint32_no_val.v0.0.40_uint32_no_val(
                                    set = True, 
                                    infinite = True, 
                                    number = 56, ), 
                                max = , ), 
                            governor = '', ), 
                        kill_request_user = '', 
                        state = [
                            'PENDING'
                            ], 
                        statistics = slurm_rest.models.v0_0_40_step_statistics.v0_0_40_step_statistics(
                            energy = slurm_rest.models.v0_0_40_step_statistics_energy.v0_0_40_step_statistics_energy(
                                consumed = , ), ), 
                        step = slurm_rest.models.v0_0_40_step_step.v0_0_40_step_step(
                            name = '', ), 
                        task = slurm_rest.models.v0_0_40_step_task.v0_0_40_step_task(
                            distribution = '', ), 
                        tres = slurm_rest.models.v0_0_40_step_tres.v0_0_40_step_tres(
                            requested = slurm_rest.models.v0_0_40_step_tres_requested.v0_0_40_step_tres_requested(
                                average = [
                                    slurm_rest.models.v0/0/40_tres.v0.0.40_tres(
                                        type = '', 
                                        name = '', 
                                        count = 56, )
                                    ], ), 
                            allocated = [
                                slurm_rest.models.v0/0/40_tres.v0.0.40_tres(
                                    type = '', 
                                    name = '', 
                                    count = 56, )
                                ], ), )
                    ],
                submit_line = '',
                tres = slurm_rest.models.v0_0_40_job_tres.v0_0_40_job_tres(
                    allocated = [
                        slurm_rest.models.v0/0/40_tres.v0.0.40_tres(
                            type = '', 
                            name = '', 
                            id = 56, 
                            count = 56, )
                        ], 
                    requested = [
                        slurm_rest.models.v0/0/40_tres.v0.0.40_tres(
                            type = '', 
                            name = '', 
                            id = 56, 
                            count = 56, )
                        ], ),
                used_gres = '',
                user = '',
                wckey = slurm_rest.models.v0/0/40_wckey_tag_struct.v0.0.40_wckey_tag_struct(
                    wckey = '', 
                    flags = [
                        'ASSIGNED_DEFAULT'
                        ], ),
                working_directory = ''
            )
        else:
            return V0040Job(
        )
        """

    def testV0040Job(self):
        """Test V0040Job"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
