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

from slurm_rest.models.v0041_openapi_licenses_resp_licenses_inner import V0041OpenapiLicensesRespLicensesInner

class TestV0041OpenapiLicensesRespLicensesInner(unittest.TestCase):
    """V0041OpenapiLicensesRespLicensesInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V0041OpenapiLicensesRespLicensesInner:
        """Test V0041OpenapiLicensesRespLicensesInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V0041OpenapiLicensesRespLicensesInner`
        """
        model = V0041OpenapiLicensesRespLicensesInner()
        if include_optional:
            return V0041OpenapiLicensesRespLicensesInner(
                license_name = '',
                total = 56,
                used = 56,
                free = 56,
                remote = True,
                reserved = 56,
                last_consumed = 56,
                last_deficit = 56,
                last_update = 56
            )
        else:
            return V0041OpenapiLicensesRespLicensesInner(
        )
        """

    def testV0041OpenapiLicensesRespLicensesInner(self):
        """Test V0041OpenapiLicensesRespLicensesInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()