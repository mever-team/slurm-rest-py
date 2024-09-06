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

from slurm_rest.models.v0040_partition_info_nodes import V0040PartitionInfoNodes

class TestV0040PartitionInfoNodes(unittest.TestCase):
    """V0040PartitionInfoNodes unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V0040PartitionInfoNodes:
        """Test V0040PartitionInfoNodes
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V0040PartitionInfoNodes`
        """
        model = V0040PartitionInfoNodes()
        if include_optional:
            return V0040PartitionInfoNodes(
                allowed_allocation = '',
                configured = '',
                total = 56
            )
        else:
            return V0040PartitionInfoNodes(
        )
        """

    def testV0040PartitionInfoNodes(self):
        """Test V0040PartitionInfoNodes"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
