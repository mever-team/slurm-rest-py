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

from slurm_rest.models.v0041_openapi_shares_resp import V0041OpenapiSharesResp

class TestV0041OpenapiSharesResp(unittest.TestCase):
    """V0041OpenapiSharesResp unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V0041OpenapiSharesResp:
        """Test V0041OpenapiSharesResp
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V0041OpenapiSharesResp`
        """
        model = V0041OpenapiSharesResp()
        if include_optional:
            return V0041OpenapiSharesResp(
                shares = slurm_rest.models.v0_0_41_openapi_shares_resp_shares.v0_0_41_openapi_shares_resp_shares(
                    shares = [
                        slurm_rest.models.v0_0_41_openapi_shares_resp_shares_shares_inner.v0_0_41_openapi_shares_resp_shares_shares_inner(
                            id = 56, 
                            cluster = '', 
                            name = '', 
                            parent = '', 
                            partition = '', 
                            shares_normalized = slurm_rest.models.v0_0_41_openapi_shares_resp_shares_shares_inner_shares_normalized.v0_0_41_openapi_shares_resp_shares_shares_inner_shares_normalized(
                                set = True, 
                                infinite = True, 
                                number = 1.337, ), 
                            tres = slurm_rest.models.v0_0_41_openapi_shares_resp_shares_shares_inner_tres.v0_0_41_openapi_shares_resp_shares_shares_inner_tres(
                                run_seconds = [
                                    slurm_rest.models.v0_0_41_openapi_shares_resp_shares_shares_inner_tres_run_seconds_inner.v0_0_41_openapi_shares_resp_shares_shares_inner_tres_run_seconds_inner(
                                        name = '', 
                                        value = slurm_rest.models.v0_0_41_openapi_shares_resp_shares_shares_inner_tres_run_seconds_inner_value.v0_0_41_openapi_shares_resp_shares_shares_inner_tres_run_seconds_inner_value(
                                            set = True, 
                                            infinite = True, 
                                            number = 56, ), )
                                    ], 
                                group_minutes = [
                                    slurm_rest.models.v0_0_41_openapi_shares_resp_shares_shares_inner_tres_run_seconds_inner.v0_0_41_openapi_shares_resp_shares_shares_inner_tres_run_seconds_inner(
                                        name = '', )
                                    ], 
                                usage = [
                                    slurm_rest.models.v0_0_41_openapi_shares_resp_shares_shares_inner_tres_usage_inner.v0_0_41_openapi_shares_resp_shares_shares_inner_tres_usage_inner(
                                        name = '', )
                                    ], ), 
                            effective_usage = 1.337, 
                            usage_normalized = slurm_rest.models.v0_0_41_openapi_shares_resp_shares_shares_inner_usage_normalized.v0_0_41_openapi_shares_resp_shares_shares_inner_usage_normalized(
                                set = True, 
                                infinite = True, 
                                number = 1.337, ), 
                            usage = 56, 
                            fairshare = slurm_rest.models.v0_0_40_assoc_shares_obj_wrap_fairshare.v0_0_40_assoc_shares_obj_wrap_fairshare(
                                factor = 1.337, 
                                level = 1.337, ), 
                            type = [
                                'USER'
                                ], )
                        ], 
                    total_shares = 56, ),
                meta = slurm_rest.models.v0_0_41_openapi_slurmdbd_jobs_resp_meta.v0_0_41_openapi_slurmdbd_jobs_resp_meta(
                    plugin = slurm_rest.models.v0_0_40_openapi_meta_plugin.v0_0_40_openapi_meta_plugin(
                        type = '', 
                        name = '', 
                        data_parser = '', 
                        accounting_storage = '', ), 
                    client = slurm_rest.models.v0_0_40_openapi_meta_client.v0_0_40_openapi_meta_client(
                        source = '', 
                        user = '', 
                        group = '', ), 
                    command = [
                        ''
                        ], 
                    slurm = slurm_rest.models.v0_0_40_openapi_meta_slurm.v0_0_40_openapi_meta_slurm(
                        version = slurm_rest.models.v0_0_40_openapi_meta_slurm_version.v0_0_40_openapi_meta_slurm_version(
                            major = '', 
                            micro = '', 
                            minor = '', ), 
                        release = '', 
                        cluster = '', ), ),
                errors = [
                    slurm_rest.models.v0_0_41_openapi_slurmdbd_jobs_resp_errors_inner.v0_0_41_openapi_slurmdbd_jobs_resp_errors_inner(
                        description = '', 
                        error_number = 56, 
                        error = '', 
                        source = '', )
                    ],
                warnings = [
                    slurm_rest.models.v0_0_41_openapi_slurmdbd_jobs_resp_warnings_inner.v0_0_41_openapi_slurmdbd_jobs_resp_warnings_inner(
                        description = '', 
                        source = '', )
                    ]
            )
        else:
            return V0041OpenapiSharesResp(
                shares = slurm_rest.models.v0_0_41_openapi_shares_resp_shares.v0_0_41_openapi_shares_resp_shares(
                    shares = [
                        slurm_rest.models.v0_0_41_openapi_shares_resp_shares_shares_inner.v0_0_41_openapi_shares_resp_shares_shares_inner(
                            id = 56, 
                            cluster = '', 
                            name = '', 
                            parent = '', 
                            partition = '', 
                            shares_normalized = slurm_rest.models.v0_0_41_openapi_shares_resp_shares_shares_inner_shares_normalized.v0_0_41_openapi_shares_resp_shares_shares_inner_shares_normalized(
                                set = True, 
                                infinite = True, 
                                number = 1.337, ), 
                            tres = slurm_rest.models.v0_0_41_openapi_shares_resp_shares_shares_inner_tres.v0_0_41_openapi_shares_resp_shares_shares_inner_tres(
                                run_seconds = [
                                    slurm_rest.models.v0_0_41_openapi_shares_resp_shares_shares_inner_tres_run_seconds_inner.v0_0_41_openapi_shares_resp_shares_shares_inner_tres_run_seconds_inner(
                                        name = '', 
                                        value = slurm_rest.models.v0_0_41_openapi_shares_resp_shares_shares_inner_tres_run_seconds_inner_value.v0_0_41_openapi_shares_resp_shares_shares_inner_tres_run_seconds_inner_value(
                                            set = True, 
                                            infinite = True, 
                                            number = 56, ), )
                                    ], 
                                group_minutes = [
                                    slurm_rest.models.v0_0_41_openapi_shares_resp_shares_shares_inner_tres_run_seconds_inner.v0_0_41_openapi_shares_resp_shares_shares_inner_tres_run_seconds_inner(
                                        name = '', )
                                    ], 
                                usage = [
                                    slurm_rest.models.v0_0_41_openapi_shares_resp_shares_shares_inner_tres_usage_inner.v0_0_41_openapi_shares_resp_shares_shares_inner_tres_usage_inner(
                                        name = '', )
                                    ], ), 
                            effective_usage = 1.337, 
                            usage_normalized = slurm_rest.models.v0_0_41_openapi_shares_resp_shares_shares_inner_usage_normalized.v0_0_41_openapi_shares_resp_shares_shares_inner_usage_normalized(
                                set = True, 
                                infinite = True, 
                                number = 1.337, ), 
                            usage = 56, 
                            fairshare = slurm_rest.models.v0_0_40_assoc_shares_obj_wrap_fairshare.v0_0_40_assoc_shares_obj_wrap_fairshare(
                                factor = 1.337, 
                                level = 1.337, ), 
                            type = [
                                'USER'
                                ], )
                        ], 
                    total_shares = 56, ),
        )
        """

    def testV0041OpenapiSharesResp(self):
        """Test V0041OpenapiSharesResp"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
