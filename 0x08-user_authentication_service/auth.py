#!/usr/bin/env python3
""" 4. Hash password """
import bcrypt


def _hash_password(password: str) -> bytes:
    """ Return a hash password """
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
