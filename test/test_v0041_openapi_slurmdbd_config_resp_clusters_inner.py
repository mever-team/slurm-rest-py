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

from slurm_rest.models.v0041_openapi_slurmdbd_config_resp_clusters_inner import V0041OpenapiSlurmdbdConfigRespClustersInner

class TestV0041OpenapiSlurmdbdConfigRespClustersInner(unittest.TestCase):
    """V0041OpenapiSlurmdbdConfigRespClustersInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V0041OpenapiSlurmdbdConfigRespClustersInner:
        """Test V0041OpenapiSlurmdbdConfigRespClustersInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V0041OpenapiSlurmdbdConfigRespClustersInner`
        """
        model = V0041OpenapiSlurmdbdConfigRespClustersInner()
        if include_optional:
            return V0041OpenapiSlurmdbdConfigRespClustersInner(
                controller = slurm_rest.models.v0_0_40_cluster_rec_controller.v0_0_40_cluster_rec_controller(
                    host = '', 
                    port = 56, ),
                flags = [
                    'REGISTERING'
                    ],
                name = '',
                nodes = '',
                select_plugin = '',
                associations = slurm_rest.models.v0_0_41_openapi_slurmdbd_config_resp_clusters_inner_associations.v0_0_41_openapi_slurmdbd_config_resp_clusters_inner_associations(
                    root = slurm_rest.models.v0_0_41_openapi_slurmdbd_jobs_resp_jobs_inner_association.v0_0_41_openapi_slurmdbd_jobs_resp_jobs_inner_association(
                        account = '', 
                        cluster = '', 
                        partition = '', 
                        user = '', 
                        id = 56, ), ),
                rpc_version = 56,
                tres = [
                    slurm_rest.models.v0_0_41_openapi_slurmdbd_jobs_resp_jobs_inner_steps_inner_tres_requested_max_inner.v0_0_41_openapi_slurmdbd_jobs_resp_jobs_inner_steps_inner_tres_requested_max_inner(
                        type = '', 
                        name = '', 
                        id = 56, 
                        count = 56, )
                    ]
            )
        else:
            return V0041OpenapiSlurmdbdConfigRespClustersInner(
        )
        """

    def testV0041OpenapiSlurmdbdConfigRespClustersInner(self):
        """Test V0041OpenapiSlurmdbdConfigRespClustersInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
