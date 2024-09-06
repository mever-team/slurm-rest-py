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

from slurm_rest.models.v0040_assoc_short import V0040AssocShort

class TestV0040AssocShort(unittest.TestCase):
    """V0040AssocShort unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V0040AssocShort:
        """Test V0040AssocShort
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V0040AssocShort`
        """
        model = V0040AssocShort()
        if include_optional:
            return V0040AssocShort(
                account = '',
                cluster = '',
                partition = '',
                user = '',
                id = 56
            )
        else:
            return V0040AssocShort(
                user = '',
        )
        """

    def testV0040AssocShort(self):
        """Test V0040AssocShort"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
