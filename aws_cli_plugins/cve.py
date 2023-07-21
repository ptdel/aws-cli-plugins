import re
import feedparser
from datetime import datetime
from dateutil.parser import parse
from colored import fore, style
from awscli.customizations.commands import BasicCommand


today = datetime.today()
# TODO: find out how to read ~/.aws/config and maybe allow user ability to set
# which AWS RSS feeds they want (e.g. marketing?)
cves = feedparser.parse("https://alas.aws.amazon.com/AL2/alas.rss")


def threat_level(msg):
    if bool(re.search("important", msg)):
        return re.sub("important", lambda t: f"{fore.RED}{t.group()}{style.RESET}", msg)

    elif bool(re.search("medium", msg)):
        return re.sub(
            "medium", lambda t: f"{fore.ORANGE_1}{t.group()}{style.RESET}", msg
        )

    elif bool(re.search("low", msg)):
        return re.sub("low", lambda t: f"{fore.YELLOW}{t.group()}{style.RESET}", msg)


def get_client(session, region, endpoint_url, verify, config=None):
    return session.create_client(
        "<some-service>",
        region_name=region,
        endpoint_url=endpoint_url,
        verify=verify,
        config=config,
    )


class CVE(BasicCommand):
    NAME = "latest"
    DESCRIPTION = "latest news from aws"
    SYNOPSIS = "aws spend"
    EXAMPLES = ""
    ARG_TABLE = []
    SUBCOMMANDS = []  # TODO: --limit ?

    def _run_main(self, parsed_args, parsed_globals):
        print("Publishing this month's CVE's for Amazon Linux 2 ...")
        for cve in cves.entries:
            published = parse(cve.published)
            if today.month == published.month:
                colorized_message = threat_level(cve.title)
                format_published = published.strftime("%m-%d-%Y")
                print(f"{format_published} | {colorized_message}")
