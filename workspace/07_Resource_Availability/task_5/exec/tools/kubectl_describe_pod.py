#!/usr/bin/env python3
"""
Simulated `kubectl describe pod` shim for the orderservice deployment.

Behaviour:
  - Prints describe output for all 5 orderservice pods in `staging`:
      3 new pods on the failing tag (ImagePullBackOff)
      2 old pods on the previous good tag (Running)
  - Header line summarises the pod list (mimicking `kubectl get pods -o wide`
    behaviour as a courtesy preamble) so the version diff is visible at a
    glance.
  - Always exits 0.
  - Each call appends a JSON record to state/poll_log.jsonl.

This is a local simulated tool for this workspace.
"""

import argparse
import json
import os
import sys
from datetime import datetime, timezone
from pathlib import Path

DEPLOYMENT = 'orderservice'
NAMESPACE = 'staging'
GOOD_TAG = 'v2.4.1'
BAD_TAG = 'v2.41'
REGISTRY = 'registry.internal'

WORKSPACE = Path(__file__).resolve().parent.parent
STATE_DIR = WORKSPACE / "state"
LOG_PATH = STATE_DIR / "poll_log.jsonl"


PODS = [{'name': 'orderservice-7d5b8f9c4-n9nz2',
  'namespace': 'staging',
  'replicaset': 'orderservice-7d5b8f9c4',
  'pod_template_hash': '7d5b8f9c4',
  'node': 'ip-10-0-12-44.ec2.internal',
  'node_ip': '10.0.12.44',
  'pod_ip': '10.0.12.243',
  'image': 'registry.internal/orderservice:v2.41',
  'version_label': 'v2.41',
  'status_phase': 'Pending',
  'container_state': 'Waiting',
  'container_reason': 'ImagePullBackOff',
  'ready': False,
  'restart_count': 0,
  'age_min': 4,
  'running': False},
 {'name': 'orderservice-7d5b8f9c4-2fk01',
  'namespace': 'staging',
  'replicaset': 'orderservice-7d5b8f9c4',
  'pod_template_hash': '7d5b8f9c4',
  'node': 'ip-10-0-12-83.ec2.internal',
  'node_ip': '10.0.12.83',
  'pod_ip': '10.0.12.114',
  'image': 'registry.internal/orderservice:v2.41',
  'version_label': 'v2.41',
  'status_phase': 'Pending',
  'container_state': 'Waiting',
  'container_reason': 'ImagePullBackOff',
  'ready': False,
  'restart_count': 0,
  'age_min': 3,
  'running': False},
 {'name': 'orderservice-7d5b8f9c4-amqhk',
  'namespace': 'staging',
  'replicaset': 'orderservice-7d5b8f9c4',
  'pod_template_hash': '7d5b8f9c4',
  'node': 'ip-10-0-12-17.ec2.internal',
  'node_ip': '10.0.12.17',
  'pod_ip': '10.0.12.113',
  'image': 'registry.internal/orderservice:v2.41',
  'version_label': 'v2.41',
  'status_phase': 'Pending',
  'container_state': 'Waiting',
  'container_reason': 'ImagePullBackOff',
  'ready': False,
  'restart_count': 0,
  'age_min': 4,
  'running': False},
 {'name': 'orderservice-6c4a3b2d1-axm5f',
  'namespace': 'staging',
  'replicaset': 'orderservice-6c4a3b2d1',
  'pod_template_hash': '6c4a3b2d1',
  'node': 'ip-10-0-11-82.ec2.internal',
  'node_ip': '10.0.11.82',
  'pod_ip': '10.0.11.72',
  'image': 'registry.internal/orderservice:v2.4.1',
  'version_label': 'v2.4.1',
  'status_phase': 'Running',
  'container_state': 'Running',
  'container_reason': '',
  'ready': True,
  'restart_count': 0,
  'age_min': 1035,
  'running': True},
 {'name': 'orderservice-6c4a3b2d1-khb9v',
  'namespace': 'staging',
  'replicaset': 'orderservice-6c4a3b2d1',
  'pod_template_hash': '6c4a3b2d1',
  'node': 'ip-10-0-11-93.ec2.internal',
  'node_ip': '10.0.11.93',
  'pod_ip': '10.0.11.231',
  'image': 'registry.internal/orderservice:v2.4.1',
  'version_label': 'v2.4.1',
  'status_phase': 'Running',
  'container_state': 'Running',
  'container_reason': '',
  'ready': True,
  'restart_count': 0,
  'age_min': 1002,
  'running': True}]

def _now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


def _ensure_state() -> None:
    STATE_DIR.mkdir(parents=True, exist_ok=True)


def _log(rec: dict) -> None:
    with LOG_PATH.open("a", encoding="utf-8") as f:
        f.write(json.dumps(rec, ensure_ascii=False) + "\n")


def _fmt_age(minutes: int) -> str:
    if minutes < 60:
        return f"{minutes}m"
    h = minutes // 60
    m = minutes % 60
    if m == 0:
        return f"{h}h"
    return f"{h}h{m}m"


def _render_pod(pod: dict) -> str:
    lines = []
    age = _fmt_age(pod["age_min"])
    lines.append(f"Name:         {pod['name']}")
    lines.append(f"Namespace:    {pod['namespace']}")
    lines.append("Priority:     0")
    lines.append(f"Node:         {pod['node']}/{pod['node_ip']}")
    lines.append(f"Start Time:   Tue, 02 Jun 2026 09:{27 if not pod['running'] else 10}:14 +0000")
    lines.append(f"Labels:       app={DEPLOYMENT}")
    lines.append(f"              pod-template-hash={pod['pod_template_hash']}")
    lines.append(f"              version={pod['version_label']}")
    lines.append("Annotations:  <none>")
    lines.append(f"Status:       {pod['status_phase']}")
    lines.append(f"IP:           {pod['pod_ip']}")
    lines.append(f"Controlled By:  ReplicaSet/{pod['replicaset']}")
    lines.append("Containers:")
    lines.append(f"  {DEPLOYMENT}:")
    if pod["running"]:
        lines.append(f"    Container ID:   containerd://{pod['version_label'].replace('.', '')}abc{pod['pod_template_hash']}")
    else:
        lines.append("    Container ID:")
    lines.append(f"    Image:          {pod['image']}")
    if pod["running"]:
        lines.append(f"    Image ID:       {REGISTRY}/{DEPLOYMENT}@sha256:7c9f2{pod['pod_template_hash']}aaa")
    else:
        lines.append("    Image ID:")
    lines.append("    Port:           8080/TCP")
    lines.append("    Host Port:      0/TCP")
    lines.append(f"    State:          {pod['container_state']}")
    if pod["running"]:
        lines.append(f"      Started:      Mon, 01 Jun 2026 17:42:11 +0000")
        lines.append("    Ready:          True")
    else:
        lines.append(f"      Reason:       {pod['container_reason']}")
        lines.append("    Last State:     Waiting")
        lines.append("      Reason:       ErrImagePull")
        lines.append("    Ready:          False")
    lines.append(f"    Restart Count:  {pod['restart_count']}")
    lines.append("    Requests:")
    lines.append("      cpu:        100m")
    lines.append("      memory:     128Mi")
    lines.append("    Limits:")
    lines.append("      cpu:        500m")
    lines.append("      memory:     512Mi")
    lines.append("Conditions:")
    if pod["running"]:
        lines.append("  Type              Status")
        lines.append("  Initialized       True")
        lines.append("  Ready             True")
        lines.append("  ContainersReady   True")
        lines.append("  PodScheduled      True")
    else:
        lines.append("  Type              Status")
        lines.append("  Initialized       True")
        lines.append("  Ready             False")
        lines.append("  ContainersReady   False")
        lines.append("  PodScheduled      True")
    lines.append("Events:")
    lines.append("  Type     Reason          Age                From               Message")
    lines.append("  ----     ------          ----               ----               -------")
    if pod["running"]:
        lines.append(f"  Normal   Scheduled       {age}              default-scheduler  Successfully assigned {NAMESPACE}/{pod['name']} to {pod['node']}")
        lines.append(f"  Normal   Pulled          {age}              kubelet            Container image \"{pod['image']}\" already present on machine")
        lines.append(f"  Normal   Created         {age}              kubelet            Created container {DEPLOYMENT}")
        lines.append(f"  Normal   Started         {age}              kubelet            Started container {DEPLOYMENT}")
    else:
        lines.append(f"  Normal   Scheduled       {age}                 default-scheduler  Successfully assigned {NAMESPACE}/{pod['name']} to {pod['node']}")
        lines.append(f"  Normal   Pulling         {age}                 kubelet            Pulling image \"{pod['image']}\"")
        lines.append(f"  Warning  Failed          {max(pod['age_min']-1,1)}m                 kubelet            Failed to pull image \"{pod['image']}\": rpc error: code = NotFound desc = failed to pull and unpack image \"{pod['image']}\": failed to resolve reference \"{pod['image']}\": {REGISTRY}/{DEPLOYMENT}:{BAD_TAG}: not found: manifest for {DEPLOYMENT}:{BAD_TAG} not found: tag not found")
        lines.append(f"  Warning  Failed          {max(pod['age_min']-1,1)}m                 kubelet            Error: ErrImagePull")
        lines.append(f"  Normal   BackOff         {max(pod['age_min']-2,1)}m (x4 over {age})    kubelet            Back-off pulling image \"{pod['image']}\"")
        lines.append(f"  Warning  Failed          {max(pod['age_min']-2,1)}m (x4 over {age})    kubelet            Error: ImagePullBackOff")
    return "\n".join(lines)


def _render_preamble(pods: list) -> str:
    # `kubectl get pods -o wide`-style preamble so the version diff is visible
    # before any individual describe blob.
    lines = []
    lines.append(f"# Pods in namespace `{NAMESPACE}` matching label app={DEPLOYMENT} (5 total)")
    lines.append("")
    lines.append("NAME                                  READY   STATUS             RESTARTS   AGE     IMAGE")
    for p in pods:
        ready = "1/1" if p["running"] else "0/1"
        status = "Running" if p["running"] else p["container_reason"]
        age = _fmt_age(p["age_min"])
        lines.append(f"{p['name']:<37} {ready:<7} {status:<18} {p['restart_count']:<10} {age:<7} {p['image']}")
    lines.append("")
    lines.append("-" * 80)
    lines.append(f"Showing `kubectl describe pod` for all {len(pods)} pods (newest first)")
    lines.append("-" * 80)
    return "\n".join(lines)


def main(argv: list) -> int:
    parser = argparse.ArgumentParser(
        prog="kubectl_describe_pod",
        description=(
            "Show describe output for the orderservice pods in staging. "
            "Accepts `-l app=orderservice` or a pod name, but always "
            "returns the full pod set for this sandbox."
        ),
    )
    parser.add_argument("name_pos", nargs="?", default=None)
    parser.add_argument("-n", "--namespace", default=NAMESPACE)
    parser.add_argument("-l", "--selector", default=None)
    parser.add_argument("-o", "--output", default=None)
    args = parser.parse_args(argv[1:])

    _ensure_state()

    preamble = _render_preamble(PODS)
    blocks = [_render_pod(p) for p in PODS]
    full_output = preamble + "\n\n" + ("\n\n" + ("=" * 80) + "\n\n").join(blocks) + "\n"
    sys.stdout.write(full_output)
    sys.stdout.flush()

    summary = {
        "n_pods": len(PODS),
        "n_failing": sum(1 for p in PODS if not p["running"]),
        "n_running": sum(1 for p in PODS if p["running"]),
        "failing_image": f"{REGISTRY}/{DEPLOYMENT}:{BAD_TAG}",
        "running_image": f"{REGISTRY}/{DEPLOYMENT}:{GOOD_TAG}",
    }
    _log({
        "ts": _now_iso(),
        "tool": "kubectl_describe_pod",
        "argv": argv[1:],
        "namespace": args.namespace,
        "selector": args.selector,
        "exit_status": 0,
        "summary": summary,
    })
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
