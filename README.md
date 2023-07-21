AWS CLI Extensions
==================
A collection of plugins that extend the amazon command line utility.

Example Plugin
--------------
The provided plugin gives some colorized output listing the current month's CVEs
for Amazon Linux 2.
```bash
❯ aws cve            
Publishing this month's CVE's for Amazon Linux 2 ...
07-17-2023 | ALAS-2023-2152 (medium): squashfs-tools
07-17-2023 | ALAS-2023-2151 (medium): python-pip
07-17-2023 | ALAS-2023-2150 (medium): python-rsa
07-17-2023 | ALAS-2023-2149 (important): ipa
...
```

About AWS CLI Plugins
---------------------
Although it's not very well documented, it's possible to write plugins for the
[aws cli][1]. [This issue][2] provides some details, and [this repo][3] led me
to having a working plugin.

For most common operations using the aws cli, using an [alias][4] is a simpler
way to add functionality to the aws cli.

In other more complex scenarios, where low-level access to the client is
required, or where some 3rd party is being integrated with, a plugin makes more
sense.

Writing a Plugin
----------------
* First, plugins must be importable:
```python
import aws_cli_plugins  # needs to work ...
```
* the plugin also needs a method called `awscli_initialize` which will inject the
new commands you're adding into the command table.
* your command (and subcommands) must inherit from the aws cli's [BasicCommand][5]
* your commands need to implement the `_run_main` method of `BasicCommand`

take a look at [s3][6] for a good reference on making subcommands and
interacting with the boto session.

[1]: https://aws.amazon.com/cli/
[2]: https://github.com/aws/aws-cli/issues/1261
[3]: https://github.com/shiftgig/awscli-console-login
[4]: https://docs.aws.amazon.com/cli/latest/userguide/cli-usage-alias.html
[5]: https://github.com/aws/aws-cli/blob/e6fab32b71e1c035e177dd929e7ea9917a4d39c5/awscli/customizations/commands.py#L42
[6]: https://github.com/aws/aws-cli/blob/develop/awscli/customizations/s3/s3.py
