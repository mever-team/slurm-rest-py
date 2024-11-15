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

from slurm_rest.models.v0039_job_array_response_msg_inner import V0039JobArrayResponseMsgInner

class TestV0039JobArrayResponseMsgInner(unittest.TestCase):
    """V0039JobArrayResponseMsgInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V0039JobArrayResponseMsgInner:
        """Test V0039JobArrayResponseMsgInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V0039JobArrayResponseMsgInner`
        """
        model = V0039JobArrayResponseMsgInner()
        if include_optional:
            return V0039JobArrayResponseMsgInner(
                job_id = 56,
                error_code = 56,
                error = '',
                why = ''
            )
        else:
            return V0039JobArrayResponseMsgInner(
        )
        """

    def testV0039JobArrayResponseMsgInner(self):
        """Test V0039JobArrayResponseMsgInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
