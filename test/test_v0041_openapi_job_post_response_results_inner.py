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

from slurm_rest.models.v0041_openapi_job_post_response_results_inner import V0041OpenapiJobPostResponseResultsInner

class TestV0041OpenapiJobPostResponseResultsInner(unittest.TestCase):
    """V0041OpenapiJobPostResponseResultsInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V0041OpenapiJobPostResponseResultsInner:
        """Test V0041OpenapiJobPostResponseResultsInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V0041OpenapiJobPostResponseResultsInner`
        """
        model = V0041OpenapiJobPostResponseResultsInner()
        if include_optional:
            return V0041OpenapiJobPostResponseResultsInner(
                job_id = 56,
                step_id = '',
                error = '',
                error_code = 56,
                why = ''
            )
        else:
            return V0041OpenapiJobPostResponseResultsInner(
        )
        """

    def testV0041OpenapiJobPostResponseResultsInner(self):
        """Test V0041OpenapiJobPostResponseResultsInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()