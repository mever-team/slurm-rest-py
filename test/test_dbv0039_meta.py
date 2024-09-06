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

from slurm_rest.models.dbv0039_meta import Dbv0039Meta

class TestDbv0039Meta(unittest.TestCase):
    """Dbv0039Meta unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Dbv0039Meta:
        """Test Dbv0039Meta
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Dbv0039Meta`
        """
        model = Dbv0039Meta()
        if include_optional:
            return Dbv0039Meta(
                plugin = slurm_rest.models.v0_0_39_meta_plugin.v0_0_39_meta_plugin(
                    type = '', 
                    name = '', ),
                slurm = slurm_rest.models.v0_0_39_meta_slurm.v0_0_39_meta_Slurm(
                    version = slurm_rest.models.v0_0_39_meta_slurm_version.v0_0_39_meta_Slurm_version(
                        major = 56, 
                        micro = 56, 
                        minor = 56, ), 
                    release = '', )
            )
        else:
            return Dbv0039Meta(
        )
        """

    def testDbv0039Meta(self):
        """Test Dbv0039Meta"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
