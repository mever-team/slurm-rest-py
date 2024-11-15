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

from slurm_rest.models.v0041_openapi_users_add_cond_resp_association_condition_association_priority import V0041OpenapiUsersAddCondRespAssociationConditionAssociationPriority

class TestV0041OpenapiUsersAddCondRespAssociationConditionAssociationPriority(unittest.TestCase):
    """V0041OpenapiUsersAddCondRespAssociationConditionAssociationPriority unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V0041OpenapiUsersAddCondRespAssociationConditionAssociationPriority:
        """Test V0041OpenapiUsersAddCondRespAssociationConditionAssociationPriority
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V0041OpenapiUsersAddCondRespAssociationConditionAssociationPriority`
        """
        model = V0041OpenapiUsersAddCondRespAssociationConditionAssociationPriority()
        if include_optional:
            return V0041OpenapiUsersAddCondRespAssociationConditionAssociationPriority(
                set = True,
                infinite = True,
                number = 56
            )
        else:
            return V0041OpenapiUsersAddCondRespAssociationConditionAssociationPriority(
        )
        """

    def testV0041OpenapiUsersAddCondRespAssociationConditionAssociationPriority(self):
        """Test V0041OpenapiUsersAddCondRespAssociationConditionAssociationPriority"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
