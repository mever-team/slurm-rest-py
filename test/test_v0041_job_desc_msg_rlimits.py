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

from slurm_rest.models.v0041_job_desc_msg_rlimits import V0041JobDescMsgRlimits

class TestV0041JobDescMsgRlimits(unittest.TestCase):
    """V0041JobDescMsgRlimits unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V0041JobDescMsgRlimits:
        """Test V0041JobDescMsgRlimits
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V0041JobDescMsgRlimits`
        """
        model = V0041JobDescMsgRlimits()
        if include_optional:
            return V0041JobDescMsgRlimits(
                cpu = slurm_rest.models.v0_0_41_job_desc_msg_rlimits_cpu.v0_0_41_job_desc_msg_rlimits_cpu(
                    set = True, 
                    infinite = True, 
                    number = 56, ),
                fsize = slurm_rest.models.v0_0_41_job_desc_msg_rlimits_fsize.v0_0_41_job_desc_msg_rlimits_fsize(
                    set = True, 
                    infinite = True, 
                    number = 56, ),
                data = slurm_rest.models.v0_0_41_job_desc_msg_rlimits_data.v0_0_41_job_desc_msg_rlimits_data(
                    set = True, 
                    infinite = True, 
                    number = 56, ),
                stack = slurm_rest.models.v0_0_41_job_desc_msg_rlimits_stack.v0_0_41_job_desc_msg_rlimits_stack(
                    set = True, 
                    infinite = True, 
                    number = 56, ),
                core = slurm_rest.models.v0_0_41_job_desc_msg_rlimits_core.v0_0_41_job_desc_msg_rlimits_core(
                    set = True, 
                    infinite = True, 
                    number = 56, ),
                rss = slurm_rest.models.v0_0_41_job_desc_msg_rlimits_rss.v0_0_41_job_desc_msg_rlimits_rss(
                    set = True, 
                    infinite = True, 
                    number = 56, ),
                nproc = slurm_rest.models.v0_0_41_job_desc_msg_rlimits_nproc.v0_0_41_job_desc_msg_rlimits_nproc(
                    set = True, 
                    infinite = True, 
                    number = 56, ),
                nofile = slurm_rest.models.v0_0_41_job_desc_msg_rlimits_nofile.v0_0_41_job_desc_msg_rlimits_nofile(
                    set = True, 
                    infinite = True, 
                    number = 56, ),
                memlock = slurm_rest.models.v0_0_41_job_desc_msg_rlimits_memlock.v0_0_41_job_desc_msg_rlimits_memlock(
                    set = True, 
                    infinite = True, 
                    number = 56, ),
                var_as = slurm_rest.models.v0_0_41_job_desc_msg_rlimits_as.v0_0_41_job_desc_msg_rlimits_as(
                    set = True, 
                    infinite = True, 
                    number = 56, )
            )
        else:
            return V0041JobDescMsgRlimits(
        )
        """

    def testV0041JobDescMsgRlimits(self):
        """Test V0041JobDescMsgRlimits"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
