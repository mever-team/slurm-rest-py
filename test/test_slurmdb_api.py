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

from slurm_rest.api.slurmdb_api import SlurmdbApi


class TestSlurmdbApi(unittest.TestCase):
    """SlurmdbApi unit test stubs"""

    def setUp(self) -> None:
        self.api = SlurmdbApi()

    def tearDown(self) -> None:
        pass

    def test_slurmdb_v0040_delete_account(self) -> None:
        """Test case for slurmdb_v0040_delete_account

        Delete account
        """
        pass

    def test_slurmdb_v0040_delete_association(self) -> None:
        """Test case for slurmdb_v0040_delete_association

        Delete association
        """
        pass

    def test_slurmdb_v0040_delete_associations(self) -> None:
        """Test case for slurmdb_v0040_delete_associations

        Delete associations
        """
        pass

    def test_slurmdb_v0040_delete_cluster(self) -> None:
        """Test case for slurmdb_v0040_delete_cluster

        Delete cluster
        """
        pass

    def test_slurmdb_v0040_delete_single_qos(self) -> None:
        """Test case for slurmdb_v0040_delete_single_qos

        Delete QOS
        """
        pass

    def test_slurmdb_v0040_delete_user(self) -> None:
        """Test case for slurmdb_v0040_delete_user

        Delete user
        """
        pass

    def test_slurmdb_v0040_delete_wckey(self) -> None:
        """Test case for slurmdb_v0040_delete_wckey

        Delete wckey
        """
        pass

    def test_slurmdb_v0040_get_account(self) -> None:
        """Test case for slurmdb_v0040_get_account

        Get account info
        """
        pass

    def test_slurmdb_v0040_get_accounts(self) -> None:
        """Test case for slurmdb_v0040_get_accounts

        Get account list
        """
        pass

    def test_slurmdb_v0040_get_association(self) -> None:
        """Test case for slurmdb_v0040_get_association

        Get association info
        """
        pass

    def test_slurmdb_v0040_get_associations(self) -> None:
        """Test case for slurmdb_v0040_get_associations

        Get association list
        """
        pass

    def test_slurmdb_v0040_get_cluster(self) -> None:
        """Test case for slurmdb_v0040_get_cluster

        Get cluster info
        """
        pass

    def test_slurmdb_v0040_get_clusters(self) -> None:
        """Test case for slurmdb_v0040_get_clusters

        Get cluster list
        """
        pass

    def test_slurmdb_v0040_get_config(self) -> None:
        """Test case for slurmdb_v0040_get_config

        Dump all configuration information
        """
        pass

    def test_slurmdb_v0040_get_diag(self) -> None:
        """Test case for slurmdb_v0040_get_diag

        Get slurmdb diagnostics
        """
        pass

    def test_slurmdb_v0040_get_instance(self) -> None:
        """Test case for slurmdb_v0040_get_instance

        Get instance info
        """
        pass

    def test_slurmdb_v0040_get_instances(self) -> None:
        """Test case for slurmdb_v0040_get_instances

        Get instance list
        """
        pass

    def test_slurmdb_v0040_get_job(self) -> None:
        """Test case for slurmdb_v0040_get_job

        Get job info
        """
        pass

    def test_slurmdb_v0040_get_jobs(self) -> None:
        """Test case for slurmdb_v0040_get_jobs

        Get job list
        """
        pass

    def test_slurmdb_v0040_get_qos(self) -> None:
        """Test case for slurmdb_v0040_get_qos

        Get QOS list
        """
        pass

    def test_slurmdb_v0040_get_single_qos(self) -> None:
        """Test case for slurmdb_v0040_get_single_qos

        Get QOS info
        """
        pass

    def test_slurmdb_v0040_get_tres(self) -> None:
        """Test case for slurmdb_v0040_get_tres

        Get TRES info
        """
        pass

    def test_slurmdb_v0040_get_user(self) -> None:
        """Test case for slurmdb_v0040_get_user

        Get user info
        """
        pass

    def test_slurmdb_v0040_get_users(self) -> None:
        """Test case for slurmdb_v0040_get_users

        Get user list
        """
        pass

    def test_slurmdb_v0040_get_wckey(self) -> None:
        """Test case for slurmdb_v0040_get_wckey

        Get wckey info
        """
        pass

    def test_slurmdb_v0040_get_wckeys(self) -> None:
        """Test case for slurmdb_v0040_get_wckeys

        Get wckey list
        """
        pass

    def test_slurmdb_v0040_post_accounts(self) -> None:
        """Test case for slurmdb_v0040_post_accounts

        Add/update list of accounts
        """
        pass

    def test_slurmdb_v0040_post_accounts_association(self) -> None:
        """Test case for slurmdb_v0040_post_accounts_association

        Add accounts with conditional association
        """
        pass

    def test_slurmdb_v0040_post_associations(self) -> None:
        """Test case for slurmdb_v0040_post_associations

        Set associations info
        """
        pass

    def test_slurmdb_v0040_post_clusters(self) -> None:
        """Test case for slurmdb_v0040_post_clusters

        Get cluster list
        """
        pass

    def test_slurmdb_v0040_post_config(self) -> None:
        """Test case for slurmdb_v0040_post_config

        Load all configuration information
        """
        pass

    def test_slurmdb_v0040_post_qos(self) -> None:
        """Test case for slurmdb_v0040_post_qos

        Add or update QOSs
        """
        pass

    def test_slurmdb_v0040_post_tres(self) -> None:
        """Test case for slurmdb_v0040_post_tres

        Add TRES
        """
        pass

    def test_slurmdb_v0040_post_users(self) -> None:
        """Test case for slurmdb_v0040_post_users

        Update users
        """
        pass

    def test_slurmdb_v0040_post_users_association(self) -> None:
        """Test case for slurmdb_v0040_post_users_association

        Add users with conditional association
        """
        pass

    def test_slurmdb_v0040_post_wckeys(self) -> None:
        """Test case for slurmdb_v0040_post_wckeys

        Add or update wckeys
        """
        pass

    def test_slurmdb_v0041_delete_account(self) -> None:
        """Test case for slurmdb_v0041_delete_account

        Delete account
        """
        pass

    def test_slurmdb_v0041_delete_association(self) -> None:
        """Test case for slurmdb_v0041_delete_association

        Delete association
        """
        pass

    def test_slurmdb_v0041_delete_associations(self) -> None:
        """Test case for slurmdb_v0041_delete_associations

        Delete associations
        """
        pass

    def test_slurmdb_v0041_delete_cluster(self) -> None:
        """Test case for slurmdb_v0041_delete_cluster

        Delete cluster
        """
        pass

    def test_slurmdb_v0041_delete_single_qos(self) -> None:
        """Test case for slurmdb_v0041_delete_single_qos

        Delete QOS
        """
        pass

    def test_slurmdb_v0041_delete_user(self) -> None:
        """Test case for slurmdb_v0041_delete_user

        Delete user
        """
        pass

    def test_slurmdb_v0041_delete_wckey(self) -> None:
        """Test case for slurmdb_v0041_delete_wckey

        Delete wckey
        """
        pass

    def test_slurmdb_v0041_get_account(self) -> None:
        """Test case for slurmdb_v0041_get_account

        Get account info
        """
        pass

    def test_slurmdb_v0041_get_accounts(self) -> None:
        """Test case for slurmdb_v0041_get_accounts

        Get account list
        """
        pass

    def test_slurmdb_v0041_get_association(self) -> None:
        """Test case for slurmdb_v0041_get_association

        Get association info
        """
        pass

    def test_slurmdb_v0041_get_associations(self) -> None:
        """Test case for slurmdb_v0041_get_associations

        Get association list
        """
        pass

    def test_slurmdb_v0041_get_cluster(self) -> None:
        """Test case for slurmdb_v0041_get_cluster

        Get cluster info
        """
        pass

    def test_slurmdb_v0041_get_clusters(self) -> None:
        """Test case for slurmdb_v0041_get_clusters

        Get cluster list
        """
        pass

    def test_slurmdb_v0041_get_config(self) -> None:
        """Test case for slurmdb_v0041_get_config

        Dump all configuration information
        """
        pass

    def test_slurmdb_v0041_get_diag(self) -> None:
        """Test case for slurmdb_v0041_get_diag

        Get slurmdb diagnostics
        """
        pass

    def test_slurmdb_v0041_get_instance(self) -> None:
        """Test case for slurmdb_v0041_get_instance

        Get instance info
        """
        pass

    def test_slurmdb_v0041_get_instances(self) -> None:
        """Test case for slurmdb_v0041_get_instances

        Get instance list
        """
        pass

    def test_slurmdb_v0041_get_job(self) -> None:
        """Test case for slurmdb_v0041_get_job

        Get job info
        """
        pass

    def test_slurmdb_v0041_get_jobs(self) -> None:
        """Test case for slurmdb_v0041_get_jobs

        Get job list
        """
        pass

    def test_slurmdb_v0041_get_qos(self) -> None:
        """Test case for slurmdb_v0041_get_qos

        Get QOS list
        """
        pass

    def test_slurmdb_v0041_get_single_qos(self) -> None:
        """Test case for slurmdb_v0041_get_single_qos

        Get QOS info
        """
        pass

    def test_slurmdb_v0041_get_tres(self) -> None:
        """Test case for slurmdb_v0041_get_tres

        Get TRES info
        """
        pass

    def test_slurmdb_v0041_get_user(self) -> None:
        """Test case for slurmdb_v0041_get_user

        Get user info
        """
        pass

    def test_slurmdb_v0041_get_users(self) -> None:
        """Test case for slurmdb_v0041_get_users

        Get user list
        """
        pass

    def test_slurmdb_v0041_get_wckey(self) -> None:
        """Test case for slurmdb_v0041_get_wckey

        Get wckey info
        """
        pass

    def test_slurmdb_v0041_get_wckeys(self) -> None:
        """Test case for slurmdb_v0041_get_wckeys

        Get wckey list
        """
        pass

    def test_slurmdb_v0041_post_accounts(self) -> None:
        """Test case for slurmdb_v0041_post_accounts

        Add/update list of accounts
        """
        pass

    def test_slurmdb_v0041_post_accounts_association(self) -> None:
        """Test case for slurmdb_v0041_post_accounts_association

        Add accounts with conditional association
        """
        pass

    def test_slurmdb_v0041_post_associations(self) -> None:
        """Test case for slurmdb_v0041_post_associations

        Set associations info
        """
        pass

    def test_slurmdb_v0041_post_clusters(self) -> None:
        """Test case for slurmdb_v0041_post_clusters

        Get cluster list
        """
        pass

    def test_slurmdb_v0041_post_config(self) -> None:
        """Test case for slurmdb_v0041_post_config

        Load all configuration information
        """
        pass

    def test_slurmdb_v0041_post_qos(self) -> None:
        """Test case for slurmdb_v0041_post_qos

        Add or update QOSs
        """
        pass

    def test_slurmdb_v0041_post_tres(self) -> None:
        """Test case for slurmdb_v0041_post_tres

        Add TRES
        """
        pass

    def test_slurmdb_v0041_post_users(self) -> None:
        """Test case for slurmdb_v0041_post_users

        Update users
        """
        pass

    def test_slurmdb_v0041_post_users_association(self) -> None:
        """Test case for slurmdb_v0041_post_users_association

        Add users with conditional association
        """
        pass

    def test_slurmdb_v0041_post_wckeys(self) -> None:
        """Test case for slurmdb_v0041_post_wckeys

        Add or update wckeys
        """
        pass


if __name__ == '__main__':
    unittest.main()