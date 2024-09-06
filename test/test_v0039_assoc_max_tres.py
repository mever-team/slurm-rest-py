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

from slurm_rest.models.v0039_assoc_max_tres import V0039AssocMaxTres

class TestV0039AssocMaxTres(unittest.TestCase):
    """V0039AssocMaxTres unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V0039AssocMaxTres:
        """Test V0039AssocMaxTres
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V0039AssocMaxTres`
        """
        model = V0039AssocMaxTres()
        if include_optional:
            return V0039AssocMaxTres(
                total = [
                    slurm_rest.models.v0/0/39_tres.v0.0.39_tres(
                        type = '', 
                        name = '', 
                        id = 56, 
                        count = 56, )
                    ],
                minutes = slurm_rest.models.v0_0_39_assoc_max_tres_minutes.v0_0_39_assoc_max_tres_minutes(
                    per = slurm_rest.models.v0_0_39_assoc_max_tres_minutes_per.v0_0_39_assoc_max_tres_minutes_per(
                        job = [
                            slurm_rest.models.v0/0/39_tres.v0.0.39_tres(
                                type = '', 
                                name = '', 
                                id = 56, 
                                count = 56, )
                            ], ), 
                    total = [
                        slurm_rest.models.v0/0/39_tres.v0.0.39_tres(
                            type = '', 
                            name = '', 
                            id = 56, 
                            count = 56, )
                        ], ),
                group = slurm_rest.models.v0_0_39_assoc_max_tres_group.v0_0_39_assoc_max_tres_group(
                    minutes = [
                        slurm_rest.models.v0/0/39_tres.v0.0.39_tres(
                            type = '', 
                            name = '', 
                            id = 56, 
                            count = 56, )
                        ], 
                    active = [
                        slurm_rest.models.v0/0/39_tres.v0.0.39_tres(
                            type = '', 
                            name = '', 
                            id = 56, 
                            count = 56, )
                        ], ),
                per = slurm_rest.models.v0_0_39_assoc_max_tres_per.v0_0_39_assoc_max_tres_per(
                    job = [
                        slurm_rest.models.v0/0/39_tres.v0.0.39_tres(
                            type = '', 
                            name = '', 
                            id = 56, 
                            count = 56, )
                        ], 
                    node = [
                        slurm_rest.models.v0/0/39_tres.v0.0.39_tres(
                            type = '', 
                            name = '', 
                            id = 56, 
                            count = 56, )
                        ], )
            )
        else:
            return V0039AssocMaxTres(
        )
        """

    def testV0039AssocMaxTres(self):
        """Test V0039AssocMaxTres"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()