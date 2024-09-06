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

from slurm_rest.models.v0040_cluster_rec_controller import V0040ClusterRecController

class TestV0040ClusterRecController(unittest.TestCase):
    """V0040ClusterRecController unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V0040ClusterRecController:
        """Test V0040ClusterRecController
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V0040ClusterRecController`
        """
        model = V0040ClusterRecController()
        if include_optional:
            return V0040ClusterRecController(
                host = '',
                port = 56
            )
        else:
            return V0040ClusterRecController(
        )
        """

    def testV0040ClusterRecController(self):
        """Test V0040ClusterRecController"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()