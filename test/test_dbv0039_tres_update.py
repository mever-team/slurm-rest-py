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

from slurm_rest.models.dbv0039_tres_update import Dbv0039TresUpdate

class TestDbv0039TresUpdate(unittest.TestCase):
    """Dbv0039TresUpdate unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Dbv0039TresUpdate:
        """Test Dbv0039TresUpdate
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Dbv0039TresUpdate`
        """
        model = Dbv0039TresUpdate()
        if include_optional:
            return Dbv0039TresUpdate(
                tres = [
                    slurm_rest.models.v0/0/39_tres.v0.0.39_tres(
                        type = '', 
                        name = '', 
                        id = 56, 
                        count = 56, )
                    ]
            )
        else:
            return Dbv0039TresUpdate(
        )
        """

    def testDbv0039TresUpdate(self):
        """Test Dbv0039TresUpdate"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
