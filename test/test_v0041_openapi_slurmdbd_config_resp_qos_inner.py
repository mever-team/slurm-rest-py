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

from slurm_rest.models.v0041_openapi_slurmdbd_config_resp_qos_inner import V0041OpenapiSlurmdbdConfigRespQosInner

class TestV0041OpenapiSlurmdbdConfigRespQosInner(unittest.TestCase):
    """V0041OpenapiSlurmdbdConfigRespQosInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V0041OpenapiSlurmdbdConfigRespQosInner:
        """Test V0041OpenapiSlurmdbdConfigRespQosInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V0041OpenapiSlurmdbdConfigRespQosInner`
        """
        model = V0041OpenapiSlurmdbdConfigRespQosInner()
        if include_optional:
            return V0041OpenapiSlurmdbdConfigRespQosInner(
                description = '',
                flags = [
                    'NOT_SET'
                    ],
                id = 56,
                limits = slurm_rest.models.v0_0_41_openapi_slurmdbd_config_resp_qos_inner_limits.v0_0_41_openapi_slurmdbd_config_resp_qos_inner_limits(
                    grace_time = 56, 
                    max = slurm_rest.models.v0_0_41_openapi_slurmdbd_config_resp_qos_inner_limits_max.v0_0_41_openapi_slurmdbd_config_resp_qos_inner_limits_max(
                        active_jobs = slurm_rest.models.v0_0_41_openapi_slurmdbd_config_resp_qos_inner_limits_max_active_jobs.v0_0_41_openapi_slurmdbd_config_resp_qos_inner_limits_max_active_jobs(
                            accruing = slurm_rest.models.v0_0_41_openapi_slurmdbd_jobs_resp_jobs_inner_array_task_id.v0_0_41_openapi_slurmdbd_jobs_resp_jobs_inner_array_task_id(
                                set = True, 
                                infinite = True, 
                                number = 56, ), 
                            count = slurm_rest.models.v0_0_41_openapi_slurmdbd_jobs_resp_jobs_inner_array_task_id.v0_0_41_openapi_slurmdbd_jobs_resp_jobs_inner_array_task_id(
                                set = True, 
                                infinite = True, 
                                number = 56, ), ), 
                        tres = slurm_rest.models.v0_0_41_openapi_slurmdbd_config_resp_qos_inner_limits_max_tres.v0_0_41_openapi_slurmdbd_config_resp_qos_inner_limits_max_tres(
                            total = [
                                slurm_rest.models.v0_0_41_openapi_slurmdbd_jobs_resp_jobs_inner_steps_inner_tres_requested_max_inner.v0_0_41_openapi_slurmdbd_jobs_resp_jobs_inner_steps_inner_tres_requested_max_inner(
                                    type = '', 
                                    name = '', 
                                    id = 56, )
                                ], 
                            minutes = slurm_rest.models.v0_0_41_openapi_slurmdbd_config_resp_qos_inner_limits_max_tres_minutes.v0_0_41_openapi_slurmdbd_config_resp_qos_inner_limits_max_tres_minutes(
                                per = slurm_rest.models.v0_0_41_openapi_slurmdbd_config_resp_qos_inner_limits_max_tres_minutes_per.v0_0_41_openapi_slurmdbd_config_resp_qos_inner_limits_max_tres_minutes_per(
                                    qos = [
                                        slurm_rest.models.v0_0_41_openapi_slurmdbd_jobs_resp_jobs_inner_steps_inner_tres_requested_max_inner.v0_0_41_openapi_slurmdbd_jobs_resp_jobs_inner_steps_inner_tres_requested_max_inner(
                                            type = '', 
                                            name = '', 
                                            id = 56, )
                                        ], 
                                    job = [
                                        
                                        ], 
                                    account = [
                                        
                                        ], 
                                    user = [
                                        
                                        ], ), ), 
                            per = slurm_rest.models.v0_0_41_openapi_slurmdbd_config_resp_qos_inner_limits_max_tres_per.v0_0_41_openapi_slurmdbd_config_resp_qos_inner_limits_max_tres_per(
                                node = [
                                    
                                    ], ), ), 
                        wall_clock = slurm_rest.models.v0_0_41_openapi_slurmdbd_config_resp_qos_inner_limits_max_wall_clock.v0_0_41_openapi_slurmdbd_config_resp_qos_inner_limits_max_wall_clock(), 
                        jobs = slurm_rest.models.v0_0_41_openapi_slurmdbd_config_resp_qos_inner_limits_max_jobs.v0_0_41_openapi_slurmdbd_config_resp_qos_inner_limits_max_jobs(), 
                        accruing = slurm_rest.models.v0_0_41_openapi_slurmdbd_config_resp_qos_inner_limits_max_jobs_active_jobs.v0_0_41_openapi_slurmdbd_config_resp_qos_inner_limits_max_jobs_active_jobs(), ), 
                    factor = slurm_rest.models.v0_0_41_openapi_slurmdbd_config_resp_qos_inner_limits_factor.v0_0_41_openapi_slurmdbd_config_resp_qos_inner_limits_factor(
                        set = True, 
                        infinite = True, 
                        number = 1.337, ), 
                    min = slurm_rest.models.v0_0_41_openapi_slurmdbd_config_resp_qos_inner_limits_min.v0_0_41_openapi_slurmdbd_config_resp_qos_inner_limits_min(
                        priority_threshold = , ), ),
                name = '',
                preempt = slurm_rest.models.v0_0_41_openapi_slurmdbd_config_resp_qos_inner_preempt.v0_0_41_openapi_slurmdbd_config_resp_qos_inner_preempt(
                    list = [
                        ''
                        ], 
                    mode = [
                        'DISABLED'
                        ], 
                    exempt_time = slurm_rest.models.v0_0_41_openapi_slurmdbd_jobs_resp_jobs_inner_array_task_id.v0_0_41_openapi_slurmdbd_jobs_resp_jobs_inner_array_task_id(
                        set = True, 
                        infinite = True, 
                        number = 56, ), ),
                priority = slurm_rest.models.v0_0_41_openapi_slurmdbd_jobs_resp_jobs_inner_array_task_id.v0_0_41_openapi_slurmdbd_jobs_resp_jobs_inner_array_task_id(
                    set = True, 
                    infinite = True, 
                    number = 56, ),
                usage_factor = slurm_rest.models.v0_0_41_openapi_slurmdbd_config_resp_qos_inner_limits_factor.v0_0_41_openapi_slurmdbd_config_resp_qos_inner_limits_factor(
                    set = True, 
                    infinite = True, 
                    number = 1.337, ),
                usage_threshold = slurm_rest.models.v0_0_41_openapi_slurmdbd_config_resp_qos_inner_limits_factor.v0_0_41_openapi_slurmdbd_config_resp_qos_inner_limits_factor(
                    set = True, 
                    infinite = True, 
                    number = 1.337, )
            )
        else:
            return V0041OpenapiSlurmdbdConfigRespQosInner(
        )
        """

    def testV0041OpenapiSlurmdbdConfigRespQosInner(self):
        """Test V0041OpenapiSlurmdbdConfigRespQosInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
