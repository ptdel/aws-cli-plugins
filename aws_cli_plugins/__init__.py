from .cve import CVE


def awscli_initialize(cli):
    cli.register("building-command-table.main", add_cve)


def add_cve(command_table, session, **kwargs):
    command_table["cve"] = CVE(session)
