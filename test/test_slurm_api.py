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

from slurm_rest.api.slurm_api import SlurmApi


class TestSlurmApi(unittest.TestCase):
    """SlurmApi unit test stubs"""

    def setUp(self) -> None:
        self.api = SlurmApi()

    def tearDown(self) -> None:
        pass

    def test_slurm_v0039_cancel_job(self) -> None:
        """Test case for slurm_v0039_cancel_job

        cancel or signal job
        """
        pass

    def test_slurm_v0039_delete_node(self) -> None:
        """Test case for slurm_v0039_delete_node

        delete node
        """
        pass

    def test_slurm_v0039_diag(self) -> None:
        """Test case for slurm_v0039_diag

        get diagnostics
        """
        pass

    def test_slurm_v0039_get_job(self) -> None:
        """Test case for slurm_v0039_get_job

        get job info
        """
        pass

    def test_slurm_v0039_get_jobs(self) -> None:
        """Test case for slurm_v0039_get_jobs

        get list of jobs
        """
        pass

    def test_slurm_v0039_get_node(self) -> None:
        """Test case for slurm_v0039_get_node

        get node info
        """
        pass

    def test_slurm_v0039_get_nodes(self) -> None:
        """Test case for slurm_v0039_get_nodes

        get all node info
        """
        pass

    def test_slurm_v0039_get_partition(self) -> None:
        """Test case for slurm_v0039_get_partition

        get partition info
        """
        pass

    def test_slurm_v0039_get_partitions(self) -> None:
        """Test case for slurm_v0039_get_partitions

        get all partition info
        """
        pass

    def test_slurm_v0039_get_reservation(self) -> None:
        """Test case for slurm_v0039_get_reservation

        get reservation info
        """
        pass

    def test_slurm_v0039_get_reservations(self) -> None:
        """Test case for slurm_v0039_get_reservations

        get all reservation info
        """
        pass

    def test_slurm_v0039_ping(self) -> None:
        """Test case for slurm_v0039_ping

        ping test
        """
        pass

    def test_slurm_v0039_slurmctld_get_licenses(self) -> None:
        """Test case for slurm_v0039_slurmctld_get_licenses

        get all Slurm tracked license info
        """
        pass

    def test_slurm_v0039_submit_job(self) -> None:
        """Test case for slurm_v0039_submit_job

        submit new job
        """
        pass

    def test_slurm_v0039_update_job(self) -> None:
        """Test case for slurm_v0039_update_job

        update job
        """
        pass

    def test_slurm_v0039_update_node(self) -> None:
        """Test case for slurm_v0039_update_node

        update node properties
        """
        pass

    def test_slurm_v0040_delete_job(self) -> None:
        """Test case for slurm_v0040_delete_job

        cancel or signal job
        """
        pass

    def test_slurm_v0040_delete_jobs(self) -> None:
        """Test case for slurm_v0040_delete_jobs

        send signal to list of jobs
        """
        pass

    def test_slurm_v0040_delete_node(self) -> None:
        """Test case for slurm_v0040_delete_node

        delete node
        """
        pass

    def test_slurm_v0040_get_diag(self) -> None:
        """Test case for slurm_v0040_get_diag

        get diagnostics
        """
        pass

    def test_slurm_v0040_get_job(self) -> None:
        """Test case for slurm_v0040_get_job

        get job info
        """
        pass

    def test_slurm_v0040_get_jobs(self) -> None:
        """Test case for slurm_v0040_get_jobs

        get list of jobs
        """
        pass

    def test_slurm_v0040_get_jobs_state(self) -> None:
        """Test case for slurm_v0040_get_jobs_state

        get list of job states
        """
        pass

    def test_slurm_v0040_get_licenses(self) -> None:
        """Test case for slurm_v0040_get_licenses

        get all Slurm tracked license info
        """
        pass

    def test_slurm_v0040_get_node(self) -> None:
        """Test case for slurm_v0040_get_node

        get node info
        """
        pass

    def test_slurm_v0040_get_nodes(self) -> None:
        """Test case for slurm_v0040_get_nodes

        get node(s) info
        """
        pass

    def test_slurm_v0040_get_partition(self) -> None:
        """Test case for slurm_v0040_get_partition

        get partition info
        """
        pass

    def test_slurm_v0040_get_partitions(self) -> None:
        """Test case for slurm_v0040_get_partitions

        get all partition info
        """
        pass

    def test_slurm_v0040_get_ping(self) -> None:
        """Test case for slurm_v0040_get_ping

        ping test
        """
        pass

    def test_slurm_v0040_get_reconfigure(self) -> None:
        """Test case for slurm_v0040_get_reconfigure

        request slurmctld reconfigure
        """
        pass

    def test_slurm_v0040_get_reservation(self) -> None:
        """Test case for slurm_v0040_get_reservation

        get reservation info
        """
        pass

    def test_slurm_v0040_get_reservations(self) -> None:
        """Test case for slurm_v0040_get_reservations

        get all reservation info
        """
        pass

    def test_slurm_v0040_get_shares(self) -> None:
        """Test case for slurm_v0040_get_shares

        get fairshare info
        """
        pass

    def test_slurm_v0040_post_job(self) -> None:
        """Test case for slurm_v0040_post_job

        update job
        """
        pass

    def test_slurm_v0040_post_job_submit(self) -> None:
        """Test case for slurm_v0040_post_job_submit

        submit new job
        """
        pass

    def test_slurm_v0040_post_node(self) -> None:
        """Test case for slurm_v0040_post_node

        update node properties
        """
        pass

    def test_slurm_v0041_delete_job(self) -> None:
        """Test case for slurm_v0041_delete_job

        cancel or signal job
        """
        pass

    def test_slurm_v0041_delete_jobs(self) -> None:
        """Test case for slurm_v0041_delete_jobs

        send signal to list of jobs
        """
        pass

    def test_slurm_v0041_delete_node(self) -> None:
        """Test case for slurm_v0041_delete_node

        delete node
        """
        pass

    def test_slurm_v0041_get_diag(self) -> None:
        """Test case for slurm_v0041_get_diag

        get diagnostics
        """
        pass

    def test_slurm_v0041_get_job(self) -> None:
        """Test case for slurm_v0041_get_job

        get job info
        """
        pass

    def test_slurm_v0041_get_jobs(self) -> None:
        """Test case for slurm_v0041_get_jobs

        get list of jobs
        """
        pass

    def test_slurm_v0041_get_jobs_state(self) -> None:
        """Test case for slurm_v0041_get_jobs_state

        get list of job states
        """
        pass

    def test_slurm_v0041_get_licenses(self) -> None:
        """Test case for slurm_v0041_get_licenses

        get all Slurm tracked license info
        """
        pass

    def test_slurm_v0041_get_node(self) -> None:
        """Test case for slurm_v0041_get_node

        get node info
        """
        pass

    def test_slurm_v0041_get_nodes(self) -> None:
        """Test case for slurm_v0041_get_nodes

        get node(s) info
        """
        pass

    def test_slurm_v0041_get_partition(self) -> None:
        """Test case for slurm_v0041_get_partition

        get partition info
        """
        pass

    def test_slurm_v0041_get_partitions(self) -> None:
        """Test case for slurm_v0041_get_partitions

        get all partition info
        """
        pass

    def test_slurm_v0041_get_ping(self) -> None:
        """Test case for slurm_v0041_get_ping

        ping test
        """
        pass

    def test_slurm_v0041_get_reconfigure(self) -> None:
        """Test case for slurm_v0041_get_reconfigure

        request slurmctld reconfigure
        """
        pass

    def test_slurm_v0041_get_reservation(self) -> None:
        """Test case for slurm_v0041_get_reservation

        get reservation info
        """
        pass

    def test_slurm_v0041_get_reservations(self) -> None:
        """Test case for slurm_v0041_get_reservations

        get all reservation info
        """
        pass

    def test_slurm_v0041_get_shares(self) -> None:
        """Test case for slurm_v0041_get_shares

        get fairshare info
        """
        pass

    def test_slurm_v0041_post_job(self) -> None:
        """Test case for slurm_v0041_post_job

        update job
        """
        pass

    def test_slurm_v0041_post_job_allocate(self) -> None:
        """Test case for slurm_v0041_post_job_allocate

        submit new job allocation without any steps that must be signaled to stop
        """
        pass

    def test_slurm_v0041_post_job_submit(self) -> None:
        """Test case for slurm_v0041_post_job_submit

        submit new job
        """
        pass

    def test_slurm_v0041_post_node(self) -> None:
        """Test case for slurm_v0041_post_node

        update node properties
        """
        pass

    def test_slurmdb_v0039_add_clusters(self) -> None:
        """Test case for slurmdb_v0039_add_clusters

        Add clusters
        """
        pass

    def test_slurmdb_v0039_add_wckeys(self) -> None:
        """Test case for slurmdb_v0039_add_wckeys

        Add wckeys
        """
        pass

    def test_slurmdb_v0039_delete_account(self) -> None:
        """Test case for slurmdb_v0039_delete_account

        Delete account
        """
        pass

    def test_slurmdb_v0039_delete_association(self) -> None:
        """Test case for slurmdb_v0039_delete_association

        Delete association
        """
        pass

    def test_slurmdb_v0039_delete_associations(self) -> None:
        """Test case for slurmdb_v0039_delete_associations

        Delete associations
        """
        pass

    def test_slurmdb_v0039_delete_cluster(self) -> None:
        """Test case for slurmdb_v0039_delete_cluster

        Delete cluster
        """
        pass

    def test_slurmdb_v0039_delete_qos(self) -> None:
        """Test case for slurmdb_v0039_delete_qos

        Delete QOS
        """
        pass

    def test_slurmdb_v0039_delete_user(self) -> None:
        """Test case for slurmdb_v0039_delete_user

        Delete user
        """
        pass

    def test_slurmdb_v0039_delete_wckey(self) -> None:
        """Test case for slurmdb_v0039_delete_wckey

        Delete wckey
        """
        pass

    def test_slurmdb_v0039_diag(self) -> None:
        """Test case for slurmdb_v0039_diag

        Get slurmdb diagnostics
        """
        pass

    def test_slurmdb_v0039_get_account(self) -> None:
        """Test case for slurmdb_v0039_get_account

        Get account info
        """
        pass

    def test_slurmdb_v0039_get_accounts(self) -> None:
        """Test case for slurmdb_v0039_get_accounts

        Get account list
        """
        pass

    def test_slurmdb_v0039_get_association(self) -> None:
        """Test case for slurmdb_v0039_get_association

        Get association info
        """
        pass

    def test_slurmdb_v0039_get_associations(self) -> None:
        """Test case for slurmdb_v0039_get_associations

        Get association list
        """
        pass

    def test_slurmdb_v0039_get_cluster(self) -> None:
        """Test case for slurmdb_v0039_get_cluster

        Get cluster info
        """
        pass

    def test_slurmdb_v0039_get_clusters(self) -> None:
        """Test case for slurmdb_v0039_get_clusters

        Get cluster list
        """
        pass

    def test_slurmdb_v0039_get_config(self) -> None:
        """Test case for slurmdb_v0039_get_config

        Dump all configuration information
        """
        pass

    def test_slurmdb_v0039_get_job(self) -> None:
        """Test case for slurmdb_v0039_get_job

        Get job info
        """
        pass

    def test_slurmdb_v0039_get_jobs(self) -> None:
        """Test case for slurmdb_v0039_get_jobs

        Get job list
        """
        pass

    def test_slurmdb_v0039_get_qos(self) -> None:
        """Test case for slurmdb_v0039_get_qos

        Get QOS list
        """
        pass

    def test_slurmdb_v0039_get_single_qos(self) -> None:
        """Test case for slurmdb_v0039_get_single_qos

        Get QOS info
        """
        pass

    def test_slurmdb_v0039_get_tres(self) -> None:
        """Test case for slurmdb_v0039_get_tres

        Get TRES info
        """
        pass

    def test_slurmdb_v0039_get_user(self) -> None:
        """Test case for slurmdb_v0039_get_user

        Get user info
        """
        pass

    def test_slurmdb_v0039_get_users(self) -> None:
        """Test case for slurmdb_v0039_get_users

        Get user list
        """
        pass

    def test_slurmdb_v0039_get_wckey(self) -> None:
        """Test case for slurmdb_v0039_get_wckey

        Get wckey info
        """
        pass

    def test_slurmdb_v0039_get_wckeys(self) -> None:
        """Test case for slurmdb_v0039_get_wckeys

        Get wckey list
        """
        pass

    def test_slurmdb_v0039_set_config(self) -> None:
        """Test case for slurmdb_v0039_set_config

        Load all configuration information
        """
        pass

    def test_slurmdb_v0039_update_accounts(self) -> None:
        """Test case for slurmdb_v0039_update_accounts

        Update accounts
        """
        pass

    def test_slurmdb_v0039_update_associations(self) -> None:
        """Test case for slurmdb_v0039_update_associations

        Set associations info
        """
        pass

    def test_slurmdb_v0039_update_qos(self) -> None:
        """Test case for slurmdb_v0039_update_qos

        Set QOS info
        """
        pass

    def test_slurmdb_v0039_update_tres(self) -> None:
        """Test case for slurmdb_v0039_update_tres

        Set TRES info
        """
        pass

    def test_slurmdb_v0039_update_users(self) -> None:
        """Test case for slurmdb_v0039_update_users

        Update user
        """
        pass


if __name__ == '__main__':
    unittest.main()
