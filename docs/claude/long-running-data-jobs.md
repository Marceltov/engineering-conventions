# Long-running data jobs

**A large file move, copy, rescan, reindex or other bulk data job runs in the service that owns the data, started by a wrapper script on the nearest layer that survives a redeploy, detached from the Claude session, resumable after an interruption and followable by a person through a log and a status command.** Decided 2026-11-23.

## Why

On 2026-11-23 a full reindex of a storage migration was started as a background job of a Claude session. The person running the migration could not see how far it was, and the job's fate was tied to a session that can be interrupted, compacted or closed. A job that takes hours outlives a conversation, so it can't live in one.

## How

Before starting a job that takes more than a few minutes or touches tens of thousands of files, write its wrapper as a small directory on the nearest layer that survives a redeploy:

```text
<job>/
  run.sh      # does the work, appends to run.log
  status.sh   # prints where it stands, safe to run at any time
  run.log     # timestamped: start, each step, result
  done        # or one marker per finished step
```

- **In the right layer.** The work runs where the data's owner runs it, for example `docker exec <service> <command>`. The wrapper does not live in the container, because a deploy recreates it and deletes the script and log. It does not live on the hypervisor when a guest can hold it. For a containerized service in a VM or LXC guest, that means the guest.
- **Detached.** Start it so that it survives the session and the SSH connection. On a systemd host: `systemd-run --unit=<job> /path/to/<job>/run.sh`. The session starts it and can then end.
- **Resumable.** Running `run.sh` again continues the job. Finished steps leave a marker and are skipped; each step is safe to repeat. Prefer a tool that resumes by itself (`rsync`, `rclone`). When a step can only start over, its comment says so.
- **Followable.** `status.sh` answers without reading code: is it running, since when, how far (files done of total where the tool can tell, otherwise a measure that grows), errors so far, and the machine's IO pressure. The person gets the exact command to run from where they work, for example `watch -n 30 ssh <host> /path/to/<job>/status.sh`.
- **Checked at the end.** A job's exit code is not its result. The last step compares what the job was meant to produce (file counts, sizes or checksums) and writes the outcome to the log.
- **Announced.** Before starting, say what the job will compete with on the same disk, such as backups. After starting, tell the person the unit name, the log path and the status command.
- **Cleaned up.** Say when the job directory can be removed. Keep it until the result has been accepted.

## Rules out

- A bulk data job running as a foreground command or background task of a Claude session.
- A job that has to start from zero after an interruption when its work can be split into steps.
- A job whose progress can only be seen by asking Claude.
- A wrapper, log or marker stored inside a container that a deploy recreates.
- Reporting a job as finished from its exit code alone.

## Reference

First applied in Marcel's homelab management repository, to a storage migration's search reindex (a systemd unit with `run.sh`, `status.sh`, a log and a done marker).
