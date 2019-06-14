# clean-known-hosts
Scan ~/.ssh/known_hosts and output only those that are "good".

## Example

This will read your ~/.ssh/known_hosts, do a ping on each address, and only output the lines that succeed.

```bash
python3 clean-known-hosts > cleaned_known_hosts
```
