import os, wandb
import wandb.apis.reports as wr

assert os.getenv("WANDB_API_KEY"), "You must set the WANDB_API_KEY environment variable"


def get_baseline_run(entity="vck281000", project="mlops-course-001", tag="baseline"):
    api = wandb.Api()
    runs = api.runs(f"{entity}/{project}", {"tags": {"$in": [tag]}})
    assert len(runs) == 1, 'Only one run should have tag "baseline"'
    return runs[0]


def compare_runs(
    entity="vck281000", project="mlops-course-001", tag="baseline", run_id=None
):
    entity = os.getenv("WANDB_ENTITY") or entity
    project = os.getenv("WANDB_PROJECT") or project
    tag = os.getenv("BASELINE_TAG") or tag
    run_id = os.getenv("RUN_ID") or run_id

    assert run_id, "Set the RUN_ID environment variable or pass a `run_id` argument"

    baseline = get_baseline_run(entity=entity, project=project, tag=tag)
    report = wr.Report(
        entity=entity,
        project=project,
        title="Compare Runs",
        description=f"A comparison of runs, the baseline run name is {baseline.name}",
    )

    pg = wr.PanelGrid(
        runsets=[
            wr.Runset(entity, project, "Run Comparison").set_filters_with_python_expr(
                f"ID in ['{run_id}', '{baseline.id}']"
            )
        ],
        panels=[
            wr.RunComparer(diff_only="split", layout={"w": 24, "h": 15}),
        ],
    )
    report.blocks = report.blocks[:1] + [pg] + report.blocks[1:]
    report.save()

    if os.getenv("CI"):
        with open(os.environ["GITHUB_OUTPUT"], "a") as f:
            print(f"REPORT_URL={report.url}", file=f)
    return report.url


if __name__ == "__main__":
    print(f"Comparison report location: {compare_runs()}")
