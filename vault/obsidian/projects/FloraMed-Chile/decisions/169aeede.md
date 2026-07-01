---
id: 169aeede
type: decision
status: proposed
project: FloraMed-Chile
---

# ADR: Profile view protected by @login_required

**Status**: proposed
**ID**: 169aeede
**Proyecto**: [[projects/FloraMed-Chile/README|FloraMed-Chile]]

## Description

Implemented profile() FBV with @login_required decorator in plantas/views.py. Passes request.user as context variable profile_user. Template displays username, email, date_joined, and last_login with a circular avatar initial.

## Rationale

login_required decorator leverages Django's built-in auth system and redirects unauthenticated users to LOGIN_URL (/login/). FBV pattern maintained for consistency.
