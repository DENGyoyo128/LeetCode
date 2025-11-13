import pandas as pd

def total_time(employees: pd.DataFrame) -> pd.DataFrame:
    employees['spent_time']=employees["out_time"]-employees["in_time"]
    # total_time=employees.groupby(["emp_id",'event_day'])['spent_time'].sum()
    total_time=employees.groupby(['event_day',"emp_id"],as_index=False)['spent_time'].sum()
    total_time=total_time.rename(columns={'event_day':"day", "spent_time":"total_time"})

    return total_time