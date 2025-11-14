import pandas as pd

def students_and_examinations(students: pd.DataFrame, subjects: pd.DataFrame, examinations: pd.DataFrame) -> pd.DataFrame:
    # examinations=examinations.merge(students,on="student_id",how="left")
    # examinations["attended_exams"]=examinations.groupby(["student_id","subject_name"],as_index=False).transform("count")
    # return examinations

     # 所有学生 × 所有科目
    pairs = (
        students.assign(k=1)
        .merge(subjects.assign(k=1), on="k")
        .drop(columns="k")
    )

    # 每个 (student_id, subject_name) 出现次数
    cnt = (
        examinations
        .value_counts(["student_id", "subject_name"])
        .reset_index(name="attended_exams")
    )

    # 合并并补 0
    out = (
        pairs
        .merge(cnt, on=["student_id", "subject_name"], how="left")
        .fillna({"attended_exams": 0})
        .sort_values(["student_id", "subject_name"])
    )

    return out[["student_id", "student_name", "subject_name", "attended_exams"]]