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

from slurm_rest.models.v0039_cluster_rec_associations import V0039ClusterRecAssociations

class TestV0039ClusterRecAssociations(unittest.TestCase):
    """V0039ClusterRecAssociations unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V0039ClusterRecAssociations:
        """Test V0039ClusterRecAssociations
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V0039ClusterRecAssociations`
        """
        model = V0039ClusterRecAssociations()
        if include_optional:
            return V0039ClusterRecAssociations(
                root = slurm_rest.models.v0/0/39_assoc_short.v0.0.39_assoc_short(
                    account = '', 
                    cluster = '', 
                    partition = '', 
                    user = '', )
            )
        else:
            return V0039ClusterRecAssociations(
        )
        """

    def testV0039ClusterRecAssociations(self):
        """Test V0039ClusterRecAssociations"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
