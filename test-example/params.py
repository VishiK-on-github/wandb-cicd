WANDB_PROJECT = "mlops-course-001"
ENTITY = "vck281000"
BDD_CLASSES = {
    i: c
    for i, c in enumerate(
        [
            "background",
            "road",
            "traffic light",
            "traffic sign",
            "person",
            "vehicle",
            "bicycle",
        ]
    )
}
RAW_DATA_AT = "vck281000/mlops-course-001/bdd_simple_1k"
PROCESSED_DATA_AT = "vck281000/mlops-course-001/bdd_simple_1k_split"
