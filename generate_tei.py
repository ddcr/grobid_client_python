#!/usr/bin/env python
#
from grobid_client.grobid_client import GrobidClient

if __name__ == "__main__":
    client = GrobidClient(config_path="./config-work.json")
    client.process("processHeaderDocument",
                   "/home/ddcr/Documents/Articles3",
                   output="/home/ddcr/Documents/Articles3-TEI",
                   n=2,
                   verbose=True,
                   force=True)
