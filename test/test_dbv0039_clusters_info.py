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

from slurm_rest.models.dbv0039_clusters_info import Dbv0039ClustersInfo

class TestDbv0039ClustersInfo(unittest.TestCase):
    """Dbv0039ClustersInfo unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Dbv0039ClustersInfo:
        """Test Dbv0039ClustersInfo
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Dbv0039ClustersInfo`
        """
        model = Dbv0039ClustersInfo()
        if include_optional:
            return Dbv0039ClustersInfo(
                meta = slurm_rest.models.dbv0/0/39_meta.dbv0.0.39_meta(
                    plugin = slurm_rest.models.v0_0_39_meta_plugin.v0_0_39_meta_plugin(
                        type = '', 
                        name = '', ), 
                    slurm = slurm_rest.models.v0_0_39_meta_slurm.v0_0_39_meta_Slurm(
                        version = slurm_rest.models.v0_0_39_meta_slurm_version.v0_0_39_meta_Slurm_version(
                            major = 56, 
                            micro = 56, 
                            minor = 56, ), 
                        release = '', ), ),
                errors = [
                    slurm_rest.models.dbv0/0/39_error.dbv0.0.39_error(
                        error_number = 56, 
                        error = '', 
                        source = '', 
                        description = '', )
                    ],
                warnings = [
                    slurm_rest.models.dbv0/0/39_warning.dbv0.0.39_warning(
                        warning = '', 
                        source = '', 
                        description = '', )
                    ],
                clusters = [
                    slurm_rest.models.v0/0/39_cluster_rec.v0.0.39_cluster_rec(
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
                            ], )
                    ]
            )
        else:
            return Dbv0039ClustersInfo(
        )
        """

    def testDbv0039ClustersInfo(self):
        """Test Dbv0039ClustersInfo"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
