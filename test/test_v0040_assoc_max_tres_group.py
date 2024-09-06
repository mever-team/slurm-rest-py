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

from slurm_rest.models.v0040_assoc_max_tres_group import V0040AssocMaxTresGroup

class TestV0040AssocMaxTresGroup(unittest.TestCase):
    """V0040AssocMaxTresGroup unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V0040AssocMaxTresGroup:
        """Test V0040AssocMaxTresGroup
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V0040AssocMaxTresGroup`
        """
        model = V0040AssocMaxTresGroup()
        if include_optional:
            return V0040AssocMaxTresGroup(
                minutes = [
                    slurm_rest.models.v0/0/40_tres.v0.0.40_tres(
                        type = '', 
                        name = '', 
                        id = 56, 
                        count = 56, )
                    ],
                active = [
                    slurm_rest.models.v0/0/40_tres.v0.0.40_tres(
                        type = '', 
                        name = '', 
                        id = 56, 
                        count = 56, )
                    ]
            )
        else:
            return V0040AssocMaxTresGroup(
        )
        """

    def testV0040AssocMaxTresGroup(self):
        """Test V0040AssocMaxTresGroup"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
