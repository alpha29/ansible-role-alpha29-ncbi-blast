import pytest


@pytest.mark.parametrize("name,version,description", [
    ("blastn", "2.9.0+", "Nucleotide-Nucleotide BLAST 2.9.0+"),
    ("blastp", "2.9.0+", "Protein-Protein BLAST 2.9.0+"),
    ("blastx", "2.9.0+", "Translated Query-Protein Subject BLAST 2.9.0+"),
    ("tblastx", "2.9.0+", "Translated Query-Translated Subject BLAST 2.9.0+"),
    ("tblastn", "2.9.0+", "Protein Query-Translated Subject BLAST 2.9.0+"),
    ("psiblast", "2.9.0+", "Position-Specific Iterated BLAST 2.9.0+"),
    ("rpsblast", "2.9.0+", "Reverse Position Specific BLAST 2.9.0+"),
    ("rpstblastn", "2.9.0+", "Translated Reverse Position Specific BLAST 2.9.0+"),
])
def test_search_applications(host, name, version, description):
    """
    These applications execute a BLAST search.
    """
    cmd = f"{name} -h"
    cmd_result = host.run(cmd)
    assert description in cmd_result.stdout, "'{}' returned stdout '{}', stderr '{}'".format(cmd,
                                                                                               cmd_result.stdout,
                                                                                               cmd_result.stderr)


@pytest.mark.parametrize("name,version,description", [
    ("makeblastdb", "2.9.0+", "Application to create BLAST databases, version 2.9.0+"),
    ("blastdb_aliastool", "2.9.0+", "Application to create BLAST database aliases, version 2.9.0+"),
    ("makeprofiledb", "2.9.0+", "Application to create databases for rpsblast, cobalt and deltablast,"),
    ("blastdbcmd", "2.9.0+", "BLAST database client, version 2.9.0+"),
])
def test_db_applications(host, name, version, description):
    """
    These applications either create or examine a BLAST database.
    """
    cmd = f"{name} -h"
    cmd_result = host.run(cmd)
    assert description in cmd_result.stdout, "'{}' returned stdout '{}', stderr '{}'".format(cmd,
                                                                                               cmd_result.stdout,
                                                                                               cmd_result.stderr)


@pytest.mark.parametrize("name,version,description", [
    ("segmasker", "1.0.0", "Low complexity region masker based on the SEG algorithm"),
    ("dustmasker", "1.0.0", "Low complexity region masker based on Symmetric DUST algorithm"),
    ("windowmasker", "1.0.0", "Window based sequence masker"),
])
def test_seq_filtering_applications(host, name, version, description):
    """
    https://www.ncbi.nlm.nih.gov/books/NBK279668/#usermanual.Sequence_filtering_applicatio
    Segmasker is an application that identifies and masks low complexity regions of protein sequences.
    The dustmasker application provides a similar functionality for nucleotide sequences.
    Windowmasker uses a genome to identify sequences represented too often to be of interest to most users.
    """
    cmd = f"{name} -h"
    cmd_result = host.run(cmd)
    assert description in cmd_result.stdout, "'{}' returned stdout '{}', stderr '{}'".format(cmd,
                                                                                               cmd_result.stdout,
                                                                                               cmd_result.stderr)