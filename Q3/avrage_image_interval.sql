SELECT *,
    DATEDIFF(
        MINUTE,
        Embryo.first_image_time,
        Embryo.last_image_time
    ) / COUNT(*)
FROM Embryo