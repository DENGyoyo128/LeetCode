import pandas as pd

def count_unique_subjects(teacher: pd.DataFrame) -> pd.DataFrame:
    cnt=teacher.groupby("teacher_id", as_index=False)["subject_id"].nunique()
    cnt=cnt.rename(columns={"subject_id":"cnt"})
    return cnt