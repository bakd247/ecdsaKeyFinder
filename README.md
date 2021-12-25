# ecdsaKeyFinder
A Python based ECDSA secp256k1 private key recovery tool
This tool is intended to be used by anyone who has forgotten thier password to their wallet and would in fact have the public key and an encrypted version of their private key.

This tool cannot be used to find a private key for an address.
It can only be used to recover the private key belonging to a Known Pulbic Key.

If your wallet has signed transacitons to spend coins in the past then the public key is makde public at that point. Address reuse is highly discouraged because of the vulnerability that this tool exploits.

This Tool is to be used for recovery of Private Keys only!!!!

DO NOT GIVE OUT YOUR KEYS TO ANYONE!!!

If You do in fact find a matching key.  This key must be multiplied by the cooresponding power of two that it collides with (modulo "n") in order to end up back at the key being searched for.

By Creating A List of Collisions and searching through this list there is a higher probability of finding a Matching Key.

Please Be sure to install the tinyec and hashlib package in pytohn3 before running this benchmark with the folowing command.
pip install tinyec
pip install hashlib


Please check back periodically for updates and optomizations.
