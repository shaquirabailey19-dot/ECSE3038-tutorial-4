# Task 3 — Idempotence

| Request | Status | Devices after |
|---|---|---|
| POST /devices (probe) | 201 | 5 |
| POST /devices (probe) again | 201 | 6 |
| PUT /devices/attic | 200 | 6 |
| PUT /devices/attic again | 200 | 6 |
| DELETE /devices/fridge | 200 | 5 |
| DELETE /devices/fridge again | 404 | 5 |

PUT and DELETE are idempotent: sending them twice left the system in the same
state as sending them once (DELETE's status changed to 404, but the state did
not). POST is not idempotent: the second POST added a duplicate probe, taking
the count from 5 to 6.