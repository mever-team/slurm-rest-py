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

from slurm_rest.models.v0039_step_nodes import V0039StepNodes

class TestV0039StepNodes(unittest.TestCase):
    """V0039StepNodes unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V0039StepNodes:
        """Test V0039StepNodes
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V0039StepNodes`
        """
        model = V0039StepNodes()
        if include_optional:
            return V0039StepNodes(
                count = 56,
                range = '',
                list = [
                    ''
                    ]
            )
        else:
            return V0039StepNodes(
        )
        """

    def testV0039StepNodes(self):
        """Test V0039StepNodes"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
