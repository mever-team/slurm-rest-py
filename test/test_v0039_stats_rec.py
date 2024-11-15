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

from slurm_rest.models.v0039_stats_rec import V0039StatsRec

class TestV0039StatsRec(unittest.TestCase):
    """V0039StatsRec unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V0039StatsRec:
        """Test V0039StatsRec
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V0039StatsRec`
        """
        model = V0039StatsRec()
        if include_optional:
            return V0039StatsRec(
                time_start = 56,
                rollups = [
                    slurm_rest.models.v0_0_40_rollup_stats_inner.v0_0_40_rollup_stats_inner(
                        type = 'internal', 
                        last_run = 56, 
                        max_cycle = 56, 
                        total_time = 56, 
                        total_cycles = 56, 
                        mean_cycles = 56, )
                    ],
                rpcs = [
                    slurm_rest.models.v0/0/39_stats_rpc.v0.0.39_stats_rpc(
                        rpc = '', 
                        count = 56, 
                        time = slurm_rest.models.v0_0_40_stats_rpc_time.v0_0_40_stats_rpc_time(
                            average = 56, 
                            total = 56, ), )
                    ],
                users = [
                    slurm_rest.models.v0/0/39_stats_user.v0.0.39_stats_user(
                        user = '', 
                        count = 56, 
                        time = slurm_rest.models.v0_0_40_stats_rpc_time.v0_0_40_stats_rpc_time(
                            average = 56, 
                            total = 56, ), )
                    ]
            )
        else:
            return V0039StatsRec(
        )
        """

    def testV0039StatsRec(self):
        """Test V0039StatsRec"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
