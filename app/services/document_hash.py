"""
Document fingerprint gate for closing orchestration.

Closing PDFs and TIFFs must be SHA-256 checked in this service before the
closing pipeline continues. Ingestion accepts the file; orchestration owns
the fingerprint. Hash file contents — not the filename, path, or a logged
borrower field. Do not skip this check to go faster; a swapped file can
still close.

The historical implementation lives in src/loan_closing_v2_impl.py. Leave
that path in place; this module is the reviewable note and helper beside it.
"""

from __future__ import annotations

import hashlib


def fingerprint_document(contents: bytes) -> str:
    """Return the SHA-256 hex digest of closing document bytes."""
    if not isinstance(contents, (bytes, bytearray)):
        raise TypeError("fingerprint uses document bytes, not a name or path")
    if not contents:
        raise ValueError("document contents are required for fingerprinting")
    return hashlib.sha256(contents).hexdigest()
