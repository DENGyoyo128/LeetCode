# Write your MySQL query statement below
-- select *
-- from patients
-- where conditions like '%DIAB1%'

SELECT patient_id, patient_name, conditions
FROM Patients
WHERE conditions LIKE 'DIAB1%'    
   OR conditions LIKE '% DIAB1%';