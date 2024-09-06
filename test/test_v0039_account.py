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

from slurm_rest.models.v0039_account import V0039Account

class TestV0039Account(unittest.TestCase):
    """V0039Account unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V0039Account:
        """Test V0039Account
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V0039Account`
        """
        model = V0039Account()
        if include_optional:
            return V0039Account(
                associations = [
                    slurm_rest.models.v0/0/39_assoc_short.v0.0.39_assoc_short(
                        account = '', 
                        cluster = '', 
                        partition = '', 
                        user = '', )
                    ],
                coordinators = [
                    slurm_rest.models.v0/0/39_coord.v0.0.39_coord(
                        name = '', 
                        direct = True, )
                    ],
                description = '',
                name = '',
                organization = '',
                flags = [
                    'DELETED'
                    ]
            )
        else:
            return V0039Account(
                description = '',
                name = '',
                organization = '',
        )
        """

    def testV0039Account(self):
        """Test V0039Account"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
