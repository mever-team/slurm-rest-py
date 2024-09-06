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

from slurm_rest.models.v0041_openapi_slurmdbd_stats_resp_statistics_rollups_monthly import V0041OpenapiSlurmdbdStatsRespStatisticsRollupsMonthly

class TestV0041OpenapiSlurmdbdStatsRespStatisticsRollupsMonthly(unittest.TestCase):
    """V0041OpenapiSlurmdbdStatsRespStatisticsRollupsMonthly unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V0041OpenapiSlurmdbdStatsRespStatisticsRollupsMonthly:
        """Test V0041OpenapiSlurmdbdStatsRespStatisticsRollupsMonthly
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V0041OpenapiSlurmdbdStatsRespStatisticsRollupsMonthly`
        """
        model = V0041OpenapiSlurmdbdStatsRespStatisticsRollupsMonthly()
        if include_optional:
            return V0041OpenapiSlurmdbdStatsRespStatisticsRollupsMonthly(
                count = 56,
                last_run = 56,
                duration = slurm_rest.models.v0_0_41_openapi_slurmdbd_stats_resp_statistics_rollups_monthly_duration.v0_0_41_openapi_slurmdbd_stats_resp_statistics_rollups_monthly_duration(
                    last = 56, 
                    max = 56, 
                    time = 56, )
            )
        else:
            return V0041OpenapiSlurmdbdStatsRespStatisticsRollupsMonthly(
        )
        """

    def testV0041OpenapiSlurmdbdStatsRespStatisticsRollupsMonthly(self):
        """Test V0041OpenapiSlurmdbdStatsRespStatisticsRollupsMonthly"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
