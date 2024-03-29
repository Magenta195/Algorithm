-- 코드를 입력하세요
SELECT
    DISTINCT C.CAR_ID
FROM
    CAR_RENTAL_COMPANY_CAR AS C
JOIN
    (SELECT
        CAR_ID
     FROM
        CAR_RENTAL_COMPANY_RENTAL_HISTORY
     WHERE
        MONTH(START_DATE) = 10
    ) AS H
ON
    H.CAR_ID = C.CAR_ID
WHERE
    C.CAR_TYPE = "세단"
ORDER BY
    C.CAR_ID DESC;