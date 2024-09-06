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

from slurm_rest.models.v0039_qos_limits import V0039QosLimits

class TestV0039QosLimits(unittest.TestCase):
    """V0039QosLimits unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V0039QosLimits:
        """Test V0039QosLimits
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V0039QosLimits`
        """
        model = V0039QosLimits()
        if include_optional:
            return V0039QosLimits(
                grace_time = slurm_rest.models.v0/0/39_uint32_no_val.v0.0.39_uint32_no_val(
                    set = True, 
                    infinite = True, 
                    number = 56, ),
                max = slurm_rest.models.v0_0_39_qos_limits_max.v0_0_39_qos_limits_max(
                    active_jobs = slurm_rest.models.v0_0_39_qos_limits_max_active_jobs.v0_0_39_qos_limits_max_active_jobs(
                        accruing = slurm_rest.models.v0/0/39_uint32_no_val.v0.0.39_uint32_no_val(
                            set = True, 
                            infinite = True, 
                            number = 56, ), 
                        count = slurm_rest.models.v0/0/39_uint32_no_val.v0.0.39_uint32_no_val(
                            set = True, 
                            infinite = True, 
                            number = 56, ), ), 
                    tres = slurm_rest.models.v0_0_39_qos_limits_max_tres.v0_0_39_qos_limits_max_tres(
                        total = [
                            slurm_rest.models.v0/0/39_tres.v0.0.39_tres(
                                type = '', 
                                name = '', 
                                id = 56, )
                            ], 
                        minutes = slurm_rest.models.v0_0_39_qos_limits_max_tres_minutes.v0_0_39_qos_limits_max_tres_minutes(
                            per = slurm_rest.models.v0_0_39_qos_limits_max_tres_minutes_per.v0_0_39_qos_limits_max_tres_minutes_per(
                                qos = [
                                    slurm_rest.models.v0/0/39_tres.v0.0.39_tres(
                                        type = '', 
                                        name = '', 
                                        id = 56, )
                                    ], 
                                job = , 
                                account = , 
                                user = , ), ), 
                        per = slurm_rest.models.v0_0_39_qos_limits_max_tres_per.v0_0_39_qos_limits_max_tres_per(
                            account = , 
                            job = , 
                            node = , 
                            user = , ), ), 
                    wall_clock = slurm_rest.models.v0_0_39_qos_limits_max_wall_clock.v0_0_39_qos_limits_max_wall_clock(), 
                    jobs = slurm_rest.models.v0_0_39_qos_limits_max_jobs.v0_0_39_qos_limits_max_jobs(), 
                    accruing = slurm_rest.models.v0_0_39_qos_limits_max_jobs_active_jobs.v0_0_39_qos_limits_max_jobs_active_jobs(), ),
                factor = 1.337,
                min = slurm_rest.models.v0_0_39_qos_limits_min.v0_0_39_qos_limits_min(
                    priority_threshold = slurm_rest.models.v0/0/39_uint32_no_val.v0.0.39_uint32_no_val(
                        set = True, 
                        infinite = True, 
                        number = 56, ), 
                    tres = slurm_rest.models.v0_0_39_qos_limits_min_tres.v0_0_39_qos_limits_min_tres(
                        per = slurm_rest.models.v0_0_39_assoc_max_tres_minutes_per.v0_0_39_assoc_max_tres_minutes_per(
                            job = [
                                slurm_rest.models.v0/0/39_tres.v0.0.39_tres(
                                    type = '', 
                                    name = '', 
                                    id = 56, 
                                    count = 56, )
                                ], ), ), )
            )
        else:
            return V0039QosLimits(
        )
        """

    def testV0039QosLimits(self):
        """Test V0039QosLimits"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
