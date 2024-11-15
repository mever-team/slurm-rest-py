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

from slurm_rest.models.v0041_openapi_slurmdbd_config_resp_associations_inner_max_tres_minutes import V0041OpenapiSlurmdbdConfigRespAssociationsInnerMaxTresMinutes

class TestV0041OpenapiSlurmdbdConfigRespAssociationsInnerMaxTresMinutes(unittest.TestCase):
    """V0041OpenapiSlurmdbdConfigRespAssociationsInnerMaxTresMinutes unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V0041OpenapiSlurmdbdConfigRespAssociationsInnerMaxTresMinutes:
        """Test V0041OpenapiSlurmdbdConfigRespAssociationsInnerMaxTresMinutes
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V0041OpenapiSlurmdbdConfigRespAssociationsInnerMaxTresMinutes`
        """
        model = V0041OpenapiSlurmdbdConfigRespAssociationsInnerMaxTresMinutes()
        if include_optional:
            return V0041OpenapiSlurmdbdConfigRespAssociationsInnerMaxTresMinutes(
                total = [
                    slurm_rest.models.v0_0_41_openapi_slurmdbd_jobs_resp_jobs_inner_steps_inner_tres_requested_max_inner.v0_0_41_openapi_slurmdbd_jobs_resp_jobs_inner_steps_inner_tres_requested_max_inner(
                        type = '', 
                        name = '', 
                        id = 56, 
                        count = 56, )
                    ],
                per = slurm_rest.models.v0_0_41_openapi_slurmdbd_config_resp_qos_inner_limits_min_tres_per.v0_0_41_openapi_slurmdbd_config_resp_qos_inner_limits_min_tres_per(
                    job = [
                        slurm_rest.models.v0_0_41_openapi_slurmdbd_jobs_resp_jobs_inner_steps_inner_tres_requested_max_inner.v0_0_41_openapi_slurmdbd_jobs_resp_jobs_inner_steps_inner_tres_requested_max_inner(
                            type = '', 
                            name = '', 
                            id = 56, 
                            count = 56, )
                        ], )
            )
        else:
            return V0041OpenapiSlurmdbdConfigRespAssociationsInnerMaxTresMinutes(
        )
        """

    def testV0041OpenapiSlurmdbdConfigRespAssociationsInnerMaxTresMinutes(self):
        """Test V0041OpenapiSlurmdbdConfigRespAssociationsInnerMaxTresMinutes"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
