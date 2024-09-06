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

from slurm_rest.models.v0041_openapi_slurmdbd_stats_resp_statistics_rollups_hourly import V0041OpenapiSlurmdbdStatsRespStatisticsRollupsHourly

class TestV0041OpenapiSlurmdbdStatsRespStatisticsRollupsHourly(unittest.TestCase):
    """V0041OpenapiSlurmdbdStatsRespStatisticsRollupsHourly unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V0041OpenapiSlurmdbdStatsRespStatisticsRollupsHourly:
        """Test V0041OpenapiSlurmdbdStatsRespStatisticsRollupsHourly
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V0041OpenapiSlurmdbdStatsRespStatisticsRollupsHourly`
        """
        model = V0041OpenapiSlurmdbdStatsRespStatisticsRollupsHourly()
        if include_optional:
            return V0041OpenapiSlurmdbdStatsRespStatisticsRollupsHourly(
                count = 56,
                last_run = 56,
                duration = slurm_rest.models.v0_0_41_openapi_slurmdbd_stats_resp_statistics_rollups_hourly_duration.v0_0_41_openapi_slurmdbd_stats_resp_statistics_rollups_hourly_duration(
                    last = 56, 
                    max = 56, 
                    time = 56, )
            )
        else:
            return V0041OpenapiSlurmdbdStatsRespStatisticsRollupsHourly(
        )
        """

    def testV0041OpenapiSlurmdbdStatsRespStatisticsRollupsHourly(self):
        """Test V0041OpenapiSlurmdbdStatsRespStatisticsRollupsHourly"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()