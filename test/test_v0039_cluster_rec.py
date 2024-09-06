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

from slurm_rest.models.v0039_cluster_rec import V0039ClusterRec

class TestV0039ClusterRec(unittest.TestCase):
    """V0039ClusterRec unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V0039ClusterRec:
        """Test V0039ClusterRec
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V0039ClusterRec`
        """
        model = V0039ClusterRec()
        if include_optional:
            return V0039ClusterRec(
                controller = slurm_rest.models.v0_0_40_cluster_rec_controller.v0_0_40_cluster_rec_controller(
                    host = '', 
                    port = 56, ),
                flags = [
                    'REGISTERING'
                    ],
                name = '',
                nodes = '',
                select_plugin = '',
                associations = slurm_rest.models.v0_0_39_cluster_rec_associations.v0_0_39_cluster_rec_associations(
                    root = slurm_rest.models.v0/0/39_assoc_short.v0.0.39_assoc_short(
                        account = '', 
                        cluster = '', 
                        partition = '', 
                        user = '', ), ),
                rpc_version = 56,
                tres = [
                    slurm_rest.models.v0/0/39_tres.v0.0.39_tres(
                        type = '', 
                        name = '', 
                        id = 56, 
                        count = 56, )
                    ]
            )
        else:
            return V0039ClusterRec(
        )
        """

    def testV0039ClusterRec(self):
        """Test V0039ClusterRec"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
