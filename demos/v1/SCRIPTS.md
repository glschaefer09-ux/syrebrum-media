# 01-syrebrum-desktop-overview

Length: 1:25 (85.5 s) · 1920x1080 H.264 MP4 · silent audio track

## YouTube title

Syrebrum: desktop overview (Ask Sy, capability map, jobs, approvals)

## YouTube description

A live walkthrough of the Syrebrum desktop app with a fictional roofing company, Demo Roofing Co. Sy (here running on Claude through Claude Code) drafts a customer text, the Connected accounts page shows what works now and what each part needs, and jobs and customer messages wait for the owner's approval before anything is sent.

All names, phone numbers (555) and email addresses (.invalid) in this video are fictional. Recorded 28 Oct 2026.

## Cards

Title card: "SYREBRUM · Your office, run with your AI · Desktop overview · real app, fictional demo data". End card: "Recorded live in a Syrebrum dev build · all names and numbers are fictional".

## Captions used (in order)

1. Syrebrum: one desktop app for running a small business Demo data: a fictional company, Demo Roofing Co.
2. Ask Sy: chat with the AI you already use (here: Claude, through Claude Code on this PC)
3. A live reply: Sy drafts the message. Nothing goes to a customer without your OK.
4. Connected accounts: what Syrebrum can do right now, and the one next step for everything else
5. Business packs: the Roofing pack (on a free demo key) and the Small Business tools included in the trial
6. Jobs from the website, the answering service and chat wait on one board for your OK
7. Approvals: every customer message and invoice waits here, exactly as it will be sent
# 02-road-office-phone-app

Length: 1:31 (91.0 s) · 1920x1080 H.264 MP4 · silent audio track

## YouTube title

Syrebrum Road Office: the phone app (chat, Needs you, schedule, cash payment)

## YouTube description

The Syrebrum phone page at a phone screen size, signed in to a dev copy of Syrebrum with fictional data. It shows a live AI-drafted text in Chat, the Needs you list, the Inbox (nothing connected in this demo), the job schedule, and recording a cash payment against an invoice; nothing is charged or sent.

All names, phone numbers (555) and email addresses (.invalid) in this video are fictional. Recorded 28 Oct 2026.

## Cards

Title card: "SYREBRUM ROAD OFFICE · Your office in your pocket · Phone app · real app, fictional demo data". End card as in the other videos.

## Captions used (in order)

1. Road Office: Syrebrum on your phone
2. It opens on Chat with your own AI
3. A live reply from Claude: a draft only. Nothing is sent.
4. Needs you: what is waiting on you, like a part running low
5. Inbox: calls, texts and email in one list, once a phone line or mailbox is connected (none in this demo)
6. Schedule: the job board, today's jobs and what waits for your OK
7. Money: invoices on your phone
8. Paid in cash on the spot? Record it in two taps
9. Nothing is charged and nothing is sent to the customer
10. Invoice marked paid: Cash
# 03-jobs-inventory-warranty

Length: 1:33 (93.2 s) · 1920x1080 H.264 MP4 · silent audio track

## YouTube title

Syrebrum: jobs, inventory and warranties in one flow

## YouTube description

One job from request to report in the Syrebrum desktop app, with fictional data: approving a website job, the service plans tab, receiving stock, using parts on a job at markup, confirming the warranty record that this drafted, and the parts report with cost, charge, markup and margin.

All names, phone numbers (555) and email addresses (.invalid) in this video are fictional. Recorded 28 Oct 2026.

## Cards

Title card: "SYREBRUM · Jobs, inventory and warranties · One job from request to report · real app, fictional demo data".

## Captions used (in order)

1. The job board: a website request from Pat Example waits for the owner's OK
2. Approve it at the time the customer asked for
3. Booked. The confirmation is drafted and waits in Approvals: nothing is sent to the customer from here
4. Service plans: repeat visits that put themselves on the board
5. Inventory: each part's stock, average cost, price, markup and margin
6. Stock in: 20 bundles of shingles received from the supplier
7. Stock out: 6 bundles used on Casey Placeholder's job (job 4), priced from the item's markup
8. Shingles carry a warranty, so a warranty record was drafted. The owner adds the serial and confirms it
9. Reports: parts cost, charged, markup and margin, by part and by job
# 04-syrebrum-ops-preview

Length: 1:08 (68.4 s) · 1920x1080 H.264 MP4 · silent audio track

## YouTube title

Syrebrum Ops (preview): shared memory and task board for people and AIs

## YouTube description

A preview of Syrebrum Ops, the CCDops web app from the CrossPCAI engine, running on a throwaway server with fictional data. It shows the briefing, the Queue in board, table and agenda views, a task claimed by a demo AI seat with its lease and attempt count, a block-editor page, team chat and the memory page. The earlier chat messages and AI-authored records were seeded for the demo; they are not live AI output.

All names, phone numbers (555) and email addresses (.invalid) in this video are fictional. Recorded 28 Oct 2026.

## Cards

Title card: "SYREBRUM OPS (PREVIEW) · A shared memory and task board · For your people and your AIs". End card: "Recorded live on a throwaway Syrebrum Ops server · all names are fictional". Ops ran with CCDOPS_INTERNAL=1 (licence gate open) on the throwaway server.

## Captions used (in order)

1. Syrebrum Ops (preview): the briefing every person and AI reads first. Fictional demo data on a throwaway server
2. The Queue: one task board for people and AI seats
3. A task claimed by an AI seat carries a lease and an attempt count. A retry is a new attempt, never an overwrite
4. Pages: docs next to the work, in a block editor
5. Team chat for people and AI seats (the earlier messages are seeded sample data)
6. Memory: each fact says who added it. A person's confirmation outranks an AI's guess
# 05-syrebrum-mesh-explainer

Length: 0:47 (47.0 s) · 1920x1080 H.264 MP4 · silent audio track

## YouTube title

Syrebrum Mesh: explainer (not a live demo)

## YouTube description

An explainer, not a live demo: the recording machine is not on a mesh. It shows the mesh client's fixed join flags printed from the engine source, the mesh test suite passing on that machine, and the honest status of no mesh installed there.

All names, phone numbers (555) and email addresses (.invalid) in this video are fictional. Recorded 28 Oct 2026.

## Cards

Title card: "EXPLAINER · Syrebrum Mesh · Not a live demo · real code and tests run on a test machine".

## Captions used (in order)

1. Explainer: Syrebrum Mesh can't be shown live on this machine
2. The join flags are fixed in code: no DNS takeover, no route takeover, no exit node
3. The mesh test suite, run on this machine: invites, safety flags, private state, per-user control pipe
4. And the honest status here: no mesh is installed on this test machine
5. Explainer, not a live demo

## Commands run on camera (real output)

- `python3 -c "from crosspcai import mesh; print(*mesh.SAFE_UP_FLAGS, sep='\n')"` (exit 0)
- `python3 -m pytest tests/test_mesh.py -v -p no:cacheprovider 2>&1 | grep -E 'PASSED|SKIPPED|FAILED|passed'` (exit 0)
- `python3 -c "from crosspcai import mesh; import json; print(json.dumps(mesh.status(), indent=1))"` (exit 0)
# 06-failstop-explainer

Length: 0:55 (55.5 s) · 1920x1080 H.264 MP4 · silent audio track

## YouTube title

Failstop: explainer (Guard, signed audit log, kill switch)

## YouTube description

An explainer, not a live demo of the full product. On a throwaway CrossPCAI test hub, Guard refuses a delete from an unknown agent, the signed and hash-chained audit log verifies, and an edited copy of the log is caught and the first altered entry named. It ends with the cloud-AI kill switch in the Syrebrum Ops preview and a slide summarising how the Failstop code scores behaviour.

All names, phone numbers (555) and email addresses (.invalid) in this video are fictional. Recorded 28 Oct 2026.

## Cards

Title card: "EXPLAINER · Failstop · Not a live demo of the full product · real commands on a test machine".

## Captions used (in order)

1. Explainer: Failstop's parts, run for real on a test machine
2. An unknown AI agent asks the hub to delete a folder...
3. ...and Guard refuses it: unknown agents are read-only by default
4. Every decision is written to a signed, hash-chained audit log
5. Change one word in a copy of the log, and verification names the first entry that was altered
6. The kill switch in Syrebrum Ops (preview): stop every cloud AI connection at once. Only a person can turn it back on
7. Explainer, not a live demo of the full product

## Commands run on camera (real output)

- `DEMO_CLIENT=unknown-bot python3 fleet_demo.py task "" "rm -rf projects"` (exit 0)
- `ls -d projects` (exit 0)
- `python3 -m crosspcai.cli audit verify --log audit.jsonl 2>/dev/null` (exit 0)
- `cp audit.jsonl tampered.jsonl && sed -i 's/"verdict": "deny"/"verdict": "allow"/' tampered.jsonl` (exit 0)
- `python3 -m crosspcai.cli audit verify --log tampered.jsonl 2>/dev/null` (exit 1)
# 07-crosspcai-explainer

Length: 0:52 (52.2 s) · 1920x1080 H.264 MP4 · silent audio track

## YouTube title

CrossPCAI: explainer (one hub, tasks routed to the right machine)

## YouTube description

An explainer on a throwaway test hub with two workers on one machine, not a real office fleet. A task that needs a C compiler runs on the worker that has gcc, a task no machine can run is refused at once with the hub's reason, and the built-in recipes are listed.

All names, phone numbers (555) and email addresses (.invalid) in this video are fictional. Recorded 28 Oct 2026.

## Cards

Title card: "EXPLAINER · CrossPCAI · The engine inside Syrebrum · real hub and workers on a test machine".

## Captions used (in order)

1. Explainer: CrossPCAI's hub and workers, on a test machine
2. Two workers are connected. Only build-box has a C compiler
3. A task that needs gcc goes to the machine that has it
4. A task no connected machine can run is refused at once, with the reason
5. Anything else goes to whichever machine is least busy
6. Ready-made recipes: jobs written for owners, not engineers
7. Explainer, not a live demo of a real fleet

## Commands run on camera (real output)

- `python3 fleet_demo.py machines` (exit 0)
- `cat hello.c` (exit 0)
- `python3 fleet_demo.py task gcc "gcc hello.c -o hello && ./hello"` (exit 0)
- `python3 fleet_demo.py task windows "ver"` (exit 0)
- `python3 fleet_demo.py task "" "echo hello from $(hostname)"` (exit 0)
- `python3 -m crosspcai.cli recipe list 2>/dev/null` (exit 0)
