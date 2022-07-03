SELECT Treatement.id,
    Treatement.patient_fk,
    Treatement.treatment_date,
    Patient.date_of_birth,
    DATEDIFF(
        YEAR,
        patient.date_of_birth,
        treatment.treatment_date
    )
FROM Treatement
    INNER JOIN Patient ON Treatement.patient_fk = Patient.id;
WHERE Treatement.id = "treatment_id"