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

from slurm_rest.models.v0040_openapi_meta_plugin import V0040OpenapiMetaPlugin

class TestV0040OpenapiMetaPlugin(unittest.TestCase):
    """V0040OpenapiMetaPlugin unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V0040OpenapiMetaPlugin:
        """Test V0040OpenapiMetaPlugin
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V0040OpenapiMetaPlugin`
        """
        model = V0040OpenapiMetaPlugin()
        if include_optional:
            return V0040OpenapiMetaPlugin(
                type = '',
                name = '',
                data_parser = '',
                accounting_storage = ''
            )
        else:
            return V0040OpenapiMetaPlugin(
        )
        """

    def testV0040OpenapiMetaPlugin(self):
        """Test V0040OpenapiMetaPlugin"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
