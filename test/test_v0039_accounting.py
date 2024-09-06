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

from slurm_rest.models.v0039_accounting import V0039Accounting

class TestV0039Accounting(unittest.TestCase):
    """V0039Accounting unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V0039Accounting:
        """Test V0039Accounting
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V0039Accounting`
        """
        model = V0039Accounting()
        if include_optional:
            return V0039Accounting(
                allocated = slurm_rest.models.v0_0_40_accounting_allocated.v0_0_40_accounting_allocated(
                    seconds = 56, ),
                id = 56,
                start = 56,
                tres = slurm_rest.models.v0/0/39_tres.v0.0.39_tres(
                    type = '', 
                    name = '', 
                    id = 56, 
                    count = 56, )
            )
        else:
            return V0039Accounting(
        )
        """

    def testV0039Accounting(self):
        """Test V0039Accounting"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
